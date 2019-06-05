var update = function(dom, name) {
    console.log(dom)
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            doucument.getElementById(this.id)
        }
    }
}
