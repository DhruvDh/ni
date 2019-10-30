import os
import re
import sys

os.system('mdbook clean')
base_url = '/ni'
os.chdir('src')

img_tag = re.compile(r"([!]\[[\w\s]*\])\((.*)\)")

for thing in os.listdir('.'):
    path = os.path.join(os.getcwd(), thing)

    if thing.endswith('.md') or thing.endswith(".MD"):
        with open(path, 'r+', encoding='utf8') as file:
            text = file.read()

            for a_thing in img_tag.findall(text):
                url = a_thing[1]
                if not url.startswith(base_url):
                    print(f"[{thing}]\t..replaced {url} with {base_url + url}")
                    text = text.replace(url, base_url + url)

            file.seek(0)
            file.write(text)
            file.truncate()
            file.close()

os.chdir('img')
for thing in os.listdir('.'):
    path = os.path.join(os.getcwd(), thing)

    if thing.endswith('.svg'):
        print(f"found file {path}")
        with open(path, 'r+', encoding='utf8') as file:
            text = file.read()
            text = text.replace("font-family: 'DejaVu Sans Mono', monospace;",
                         'font-family: "CascadiaCode Nerd Font", "Source Code Pro", Consolas, "Ubuntu Mono", Menlo, "DejaVu Sans Mono", monospace; font-variant-ligatures: normal;' )
            text = text.replace("font-size: 14px;", "font-size: 0.875em;")

            file.seek(0)
            file.write(text)
            file.truncate()
            file.close()
os.chdir('..')

os.chdir('..')
os.system('mdbook build')


os.chdir('src')
count = 0

for thing in os.listdir('.'):
    path = os.path.join(os.getcwd(), thing)

    if thing.endswith('.md') or thing.endswith(".MD"):
        with open(path, 'r+') as file:
            text = file.read()

            # print(f"{path}: {len(text.split())} words.")
            count += len(text.split())

with open("../words", 'w') as f:
    f.write(str(count))
