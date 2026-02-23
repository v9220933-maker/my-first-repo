import requests
url=("https://www.thestar.com")#this is the website address

 
response=requests.get(url,timeout=20)
html=response.text
headlines=[]
for i in range(1,7):
 start=html.find(f"<h{i}>")
 end=html.find(f"</h{i}>")   
    
start=0 
while True:
    start=html.find(f"<h{i}>",start)
    if start==-1:
       break
    end=html.find(f"</h{i}>",start)
    if end==-1:
       break
content=html[start + len(f"<h{i}>:end")]
headlines.append(content.strip())
start=end + len(f"</h{i}>")
for idx ,headline in enumerate(headlines):
 print(f"{idx}:{headline}")