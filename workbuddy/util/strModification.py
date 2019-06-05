def stringToList(str, seperator=","):
    """ Takes a string and converts it to a list

    Args:
        str (str): string represenation of a list
        seperator (str): the string that seperates the values of the list

    Returns:
        list: the list represenated by str

    >> stringToList("")
    []
    >> stringToList("0")
    ["0"]
    >> stringToList("0,cow")
    ["0", "cow"]
    """
    if str=="":
        return []
    if seperator not in str:
        return [str]
    a=[]
    i=0
    start=0
    str+=","
    while i<len(str):
        if str[i]==seperator:
            a.append(str[start:i])
            start=i+1
        i+=1
    return a

def listToString(list, seperator=","):
    """ Converts a list to a string

    Args:
        list (list): list of strings
        seperator (str): the string that seperates the values of the list

    Returns:
        str: the string representation of a list

    >> listToString([])
    ""
    >> listToString(["0"])
    "0"
    >> listToString(["0","cow"])
    "0,cow"
    """
    a=""
    if len(list)==0:
        return a
    if len(list)==1:
        return str(list[0])
    for i in list:
        a+=str(i)
        a+=","
    return a[:-1]
        
