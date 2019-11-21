import sys
import re
import requests
from bs4 import BeautifulSoup

def main():

    if len(sys.argv) == 2:
        path = sys.argv[1]
        if path[-1] == "/": path = path[:-1]
        with open(path+"/.git/config") as f:
            line = f.readline()
            for line in line:
                print(line)
                line = f.readline()

            f.close()
    else:
        with open("./.git/config") as f:
            line = f.readline()
            while line:
                url = re.search("^\s*url",line)
                if url:
                    print(line[7:])
                line = f.readline()

            f.close()

main()
