import requests

url = "https://www.thestar.com"

try:
    response = requests.get(url, timeout=20)
    html = response.text
    
    headlines = []
    
    # Look for headlines in h1-h6 tags
    for i in range(1, 7):
        tag = f"h{i}"
        start = 0
        while True:
            # Find the start of the tag (case-insensitive)
            start_tag = html.find(f"<{tag}", start)
            if start_tag == -1:
                break
                
            # Find the end of the opening tag
            tag_end = html.find(">", start_tag)
            if tag_end == -1:
                break
                
            # Find the closing tag
            end_tag = html.find(f"</{tag}>", tag_end)
                
            # Extract content between tags
            if end_tag == -1:
                break
            content = html[tag_end+1:end_tag].strip()
            
            # Clean the content (remove any nested tags)
            while "<" in content and ">" in content:
                tag_start = content.find("<")
                tag_end = content.find(">", tag_start)
                if tag_end != -1:
                    content = content[:tag_start] + content[tag_end+1:]
            
                            # Add to headlines if not empty
            if content:
                headlines.append(content)
            
            # Move the search position forward 
            start = end_tag + len(f"</{tag}>")
    
    # Print all found headlines
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}: {headline}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")