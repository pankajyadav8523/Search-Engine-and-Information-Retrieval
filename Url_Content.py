import requests

inp = input("Please enter the url of the webpage: ")

def htmlTag(url):
    html_tag = requests.get(url=url).text
    return html_tag

def parseTag(s):
    start = s.index('>')
    end = s.index('<', start)
    return s[start + 1:end]

with open('output.txt', 'w') as file:
    file.write(htmlTag(inp))


with open('output.txt', 'r') as file:
    
    for line in file:
        try:
            print(parseTag(line))
            
        except:
            continue
        
            
            
            
