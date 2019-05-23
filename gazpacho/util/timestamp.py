from time import time, localtime, strftime

def createTimestamp():
    """ Returns the current POSIX timestamp (time since epoch)

    Returns:
        float: the POSIX timestamp

    Notes:
        - Floats can be store in sqlite3 as INTEGER type
        - Epoch may differ between different systems. On most windows
        and unix systems, epoch time is January 1, 1970, 00:00:00 (UTC)
    """
    timestamp = time()
    # print(timestamp)
    return timestamp

def convertTimestamp(timestamp):
    """ Returns a string represenation of the timestamp given

    Args:
        timestamp (float): the posix timestamp

    Returns:
        str : string represenation of the timestamp

    Notes:
        - format can be change depending on what you want to display
        - ex. of '%Y-%m-%d %H:%M:%S %Z'
            - 2019-05-23 21:01:35 Eastern Daylight Time
    """
    format = '%Y-%m-%d %H:%M:%S %Z'
    formattedTime = strftime(format, localtime(timestamp))

    return formattedTime

def test():
    timestamp = createTimestamp()
    print(timestamp)

    localtime = convertTimestamp(timestamp)
    print(localtime)

test()
