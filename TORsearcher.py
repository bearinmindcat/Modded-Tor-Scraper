def torSearcher(url):
    
    import requests
    import random
    def get_tor_session():
        session = requests.session()
        session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'}
        return session

    session = get_tor_session()



    print("Getting ...", url)
    result = session.get(url).text

    
    import string
# added some changes here to create a new file folder so the txt files don't all generate in the same file here
    import os
    folder = "crawled_onions"
    os.makedirs(folder, exist_ok=True)
    base_filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    txt_filename = os.path.join(folder, f"{base_filename}.txt")
    html_filename = os.path.join(folder, f"{base_filename}.html")
    with open(txt_filename, "w+", encoding="utf-8") as newthing:
        newthing.write(result)
    with open(html_filename, "w+", encoding="utf-8") as newthing:
        newthing.write(result)


#JK Added in some code that just lets you enter the filepath of the onion txt files you want to run this on

import sys
import os
programname = os.path.basename(sys.argv[0])

if len(sys.argv) > 1:
    thelist = sys.argv[1]
else:
    thelist = input("Enter the path to the newline separated list file: ")

print("Opening ...", thelist)
with open(thelist, "r", encoding="utf-8") as newfile:
    data = newfile.readlines()
#JK Added in some code to make sure if you get a "unreachable/failed" request it keeps going instead of stopping
for k in data:
        k = k.replace("\n","")
        k = "http://" + k
        try:
            torSearcher(k)
        except Exception as E:
            print(f"Error fetching {k}: {E}")
