import url.requests
url=("https://www.thestar.com")
def fetch_text_from_url(url):
    # Fetch the HTML content
    response = url.request.urlopen(url)
    html = response.read().decode('utf-8', errors='ignore')

    # Manually remove tags (very basic HTML stripper)
    text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
            text += ' '
        elif not inside_tag:
            text += char

    # Clean up extra spaces and newlines
    lines = [line.strip() for line in text.splitlines()]
    text = '\n'.join(line for line in lines if line)

    return text

text = fetch_text_from_url(url)
print(text)
