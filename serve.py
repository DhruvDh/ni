import os
import re
import sys

base_url = '/ni'
os.chdir('src')

img_tag = re.compile(r"([!]\[[\w\s]*\])\((.*)\)")

for thing in os.listdir('.'):
    path = os.path.join(os.getcwd(), thing)

    if thing.endswith('.md') or thing.endswith(".MD"):
        with open(path, 'r+') as file:
            text = file.read()
            
            for a_thing in img_tag.findall(text):
                url = a_thing[1]
                if url.startswith(base_url):
                    print(f"[{thing}]\t..replaced {url} with {url.replace(base_url, '')}", file=sys.stderr)
                    text = text.replace(url, url.replace(base_url, ''))
            
            file.seek(0)
            file.write(text)
            file.truncate()
            file.close()

os.chdir('..')
os.system('mdbook serve')