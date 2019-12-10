import sys
import re
import requests
from bs4 import BeautifulSoup

def main():
    path = "./.git/config"
    if len(sys.argv) == 2:
        path = sys.argv[1]
        if path[-1] == "/": path = path[:-1]
        path += "/.git/config"

    with open(path) as f:
        line = f.readline()
        while line:
            url = re.search("^\s*url",line)
            if url:
                url = line[7:]
                break
            line = f.readline()

        f.close()

    url_split = url.split("/")
    url = ""

    for i in url_split[:-1]:
        url += i
        url += "/"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    svg = soup.find("svg",{"class": "js-calendar-graph-svg"})

    result = []

    num = 0
    for g in svg.find_all("g"):
        result.append([])
        for rect in g.find_all("rect",{"class": "day"}):
            color = rect.get("fill")
            if color == "#ebedf0":
                result[-1].append("□ ")
            elif color == "#c6e48b":
                result[-1].append("\033[38;2;198;226;123m{}\033[0m".format("■ "))
            elif color == "#7bc96f":
                result[-1].append("\033[38;2;95;177;99m{}\033[0m".format("■ "))
            elif color == "#239a3b":
                result[-1].append("\033[38;2;31;136;63m{}\033[0m".format("■ "))
            elif color == "#196127":
                result[-1].append("\033[38;2;23;85;35m{}\033[0m".format("■ "))
                

    for i in range(7):
        for j in range(len(result)):
            if result[j][i:i+1]:
                print(result[j][i],end="")
                
        print("\n")


