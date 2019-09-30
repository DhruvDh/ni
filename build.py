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
                if not url.startswith(base_url):
                    print(f"[{thing}]\t..replaced {url} with {base_url + url}", file=sys.stderr)
                    text = text.replace(url, base_url + url)
            
            file.seek(0)
            file.write(text)
            file.close()

os.chdir('..')
os.system('mdbook build')