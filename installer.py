import urllib.request
import requests
import os
cwd = os.getcwd()
os.mkdir("install")
copy = cwd + "/" + "install"
os.chdir(copy)
url = r"https://github.com/isaacmaker/Future-Linked-Ai/raw/main/Future%20Linked/future%20linked%20start%20up%20.png"
path = "future linked start up .png"
urllib.request.urlretrieve(url, path)
url = r"https://github.com/isaacmaker/Future-Linked-Ai/raw/main/Future%20Linked/icon_future%20linked.ico"
path = "icon_future linked.ico"
urllib.request.urlretrieve(url, path)
url = r"https://github.com/isaacmaker/Future-Linked-Ai/raw/main/Future%20Linked/enter%20sound.mp3"
response = requests.get(url)
print("hello")
with open("enter sound.mp3", "wb") as f:
    f.write(response.content)
url = r"https://github.com/isaacmaker/Future-Linked-Ai/raw/main/Future%20Linked/sound.mp3"
response = requests.get(url)

with open("sound.mp3", "wb") as f:
    f.write(response.content)
current_folder = os.path.basename(os.getcwd())
url = r"https://raw.githubusercontent.com/isaacmaker/Future-Linked-Ai/main/Future%20Linked%20Ai.py"
try:
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8').strip()
    print(data)
    #file_path = r'{}\update.json'.format(current_folder)
    f = open("e.json",'w')
    import json
    json.dump(data, f)

    #file_path = r'{}\update.json'.format(current_folder)
    f = open("e.json","r")

    data = json.load(f)
except:
    print("update","not online error git")
with open("update_encoded", 'w') as f:
    f.write(data)

    with open("update_encoded", 'r') as futurelinkedupdate:
        import base64
        from base64 import encode,decode
        future_decoded = ""
        update = futurelinkedupdate.read()
        future_encode = update
        future_encode = base64.a85decode(future_encode)
        future_encode = future_encode.swapcase()
        future_encode = future_encode.decode(encoding="utf-8")
        lenth_future = len(future_encode)
        future_num = reversed(future_encode)
        for i in range(lenth_future):
            future_decoded = future_decoded + next(future_num)
        file = open("Future Linked Ai.py","w")
        file.write(future_decoded)
with urllib.request.urlopen("https://raw.githubusercontent.com/isaacmaker/Future-Linked-Ai/main/verson.json") as url3:
        save = json.load(url3)
        with open("verson.json","w") as v:
            json.dump(save,v)
os.remove('update_encoded')
os.remove("e.json")
#create a varible that is named asd that has a value of 1
os


