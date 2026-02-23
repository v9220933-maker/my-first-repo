import requests #Getting stuff from the internet
URL=("https://www.thestar.com")#this is the website address
html = requests.get("URL").text 
headlines=[]#empty list
pos = 0 
for i in range(1, 7):
    s, end_tag = 0, f"</h{i}>"
    while True:
        start = html.find(f"<h{i}", s)
        if start == -1: break#the loop stops if nothing found
        start = html.find(">", start) + 1
        e = html.find(end_tag, start)
        text = html[start:e].strip()
        if text and "<" not in text: headlines.append(text)
        s = e + len(end_tag)
pos = 0
while True:
    start = html.find('<a', pos)
    if start == -1: break
    end_tag = html.find(">", start) + 1
    if 'headline' in html[start:end_tag].lower():
        e = html.find("</a>", end_tag)
        text = html[end_tag:e].strip()
        if text and "<" not in text: headlines.append(text)
    pos = end_tag
for h in list(dict.fromkeys(headlines)):
    print(h)