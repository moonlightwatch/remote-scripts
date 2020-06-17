import re
import sys
import requests

def query_title(target: str) -> str:
    url = target
    if not url.startswith("http"):
        url = "http://" + url
    resp = requests.get(url=url, headers={
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
    m = re.findall("<title>.*?<", resp.content.decode("utf8"))
    if m is None or len(m)==0:
        return ""
    return m[0][7:-1]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(query_title(sys.argv[1]))
    else:
        print("")
