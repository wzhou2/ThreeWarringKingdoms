//will add d3 timeline and button elements
let data = [
  { assessment_date: "2017-11-20T09:51:36.035983Z", id: 2 },
  { assessment_date: "2018-04-19T00:31:03.153000Z", id: 1 },
  { assessment_date: "2018-02-15T09:51:36.035983Z", id: 3 },
  { assessment_date: "2018-02-20T09:51:36.035983Z", id: 4 },
  { assessment_date: "2018-03-19T17:48:44.820000Z", id: 5 }
];

data = data
  .map(d => { d.date = new Date(d.assessment_date); return d; })
  .sort(d => d.assessment_date);

const NODE_RADIUS = 6;
const WIDTH = 600;
const HEIGHT = 30;

const svg = d3.select("#timeline").append("svg")
  .attr("width", WIDTH).attr("height", HEIGHT)
  .attr("padding-top", "10px");

let xScale = d3.scaleTime()
  .domain(d3.extent(data.map(d => d.date)))
  .range([0, WIDTH])
  .nice();

const xAxis = d3.axisBottom(xScale);

const axisSelector = svg.append("g").attr("class", "x axis").call(xAxis);

svg.call(
  d3.zoom()
    .on("zoom", function() {
      newScale = d3.event.transform.rescaleX(xScale);
      axisSelector.call(xAxis.scale(newScale));
      updateCircles(newScale);
    })
);

function updateCircles(newScale) {

  const mergedData = merge(
    data.map(d => { return { date: d.date, count: 1 }; }),
    newScale
  );

  var circles = svg.selectAll("circle").data(mergedData);

  circles.enter().append("circle")
    .attr("r", NODE_RADIUS)
    .merge(circles)
    .attr("cx", d => newScale(d.date));

  circles.exit().remove();

  var counts = svg.selectAll("text.count").data(mergedData);

  counts.enter().append("text")
    .attr("class", "count")
    .merge(counts)
    .attr("transform", d => "translate(" + (newScale(d.date) - 3) + ",-10)")
    .text(d => d.count);

  counts.exit().remove();
}

function merge(data, scale) {

  let newData = [data[0]];

  let i;
  for (i = 1; i < data.length; i++) {
    const previous = newData[newData.length - 1];
    const distance = scale(data[i].date) - scale(previous.date);
    if (Math.abs(distance) < 2 * NODE_RADIUS) {
      const averageDate = new Date(
        (data[i].date.getTime() * data[i].count + previous.date.getTime() * previous.count)
        / (data[i].count + previous.count)
      );
      const count = previous.count;
      newData.pop();
      newData.push({ date: averageDate, count: data[i].count + count });
    }
    else
      newData.push(data[i]);
  }

    return newData;
}

updateCircles(xScale);
