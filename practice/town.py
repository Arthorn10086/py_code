import sys


def handle(_string):
    if _string.startswith("combine|"):
        string = "".join(_string[8:].split(","))
        return string
    else:
        return "quit"


if __name__ == '__main__':
    """waiting for input """
    while 1:
        _stream = sys.stdin.readline()
        if not _stream:
            break
        inString = _stream.strip("\r\n")
        outString = handle(inString)
        if outString == "quit":
            sys.stdout.write("%s\n" % (outString,))
            sys.exit(0)
        else:
            sys.stdout.write("%s\n" % (outString,))
