import os
import json
import shutil
from tqdm import tqdm
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Script : Manage files and folder edit by SIMO (^_^)")

main_name = str(str(__file__).split(chr(92))[-1]).split('.')[0]
print('[+] Start make' + main_name + '.json file ')

data = """{
    "zip" : "Compressed",
    "iso" : "Compressed",
    "rar" : "Compressed",
    "img" : "Compressed",
    "pdf" : "Documents",
    "xml" : "Documents",
    "odp" : "Documents",
    "txt" : "Documents",
    "log" : "Documents",
    "docx" : "Documents",
    "dotm" : "Documents",
    "accdb" : "Documents",
    "html" : "Documents",
    "php" : "Documents",
    "htm" : "Documents",
    "odt" : "Documents",
    "json" : "Documents",
    "ods" : "Documents",
    "rtf" : "Documents",
    "pub" : "Documents",
    "xls" : "Documents",
    "xlsx" : "Documents",
    "ppt" : "Documents",
    "csv" : "Documents",
    "pptx" : "Documents",
    "doc" : "Documents",
    "epub" : "Documents",
    "md5" : "Documents",
    "ini" : "Documents",
    "exe" : "Programs",
    "py" : "Programs",
    "vbs" : "Programs",
    "js" : "Programs",
    "bat" : "Programs",
    "msi" : "Programs",
    "lnk" : "Raccourci",
    "url" : "Raccourci",
    "png" : "Images",
    "jpg" : "Images",
    "jpeg" : "Images",
    "gif" : "Images",
    "ai" : "Images",
    "eps" : "Images",
    "psd" : "Images",
    "tif" : "Images",
    "svg" : "Images",
    "apk" : "App",
    "mp4" : "Video",
    "mov" : "Video",
    "avi" : "Video",
    "flv" : "Video",
    "wmv" : "Video",
    "mpeg" : "Video",
    "mkv" : "Video",
    "asf" : "Video",
    "rm" : "Video",
    "rmvb" : "Video",
    "vob" : "Video",
    "ts" : "Video",
    "dat" : "Video",
    "crdownload" :"Download",
    "torrent" :"Download"
}"""

with open(main_name + '.json', 'w') as a:
    a.write(data)

print('[+] End make',main_name,'.json file ')
print('[!] Now you can change',main_name+ '.json if you want...')
input('[!] If you end press [ENTER] to continue...')
print('[+] start read file')
with open(main_name + '.json','r') as read_file:
    data = json.load(read_file)

print('[+] end read file')
print('[+] start script')
x = input(r'[!] Enter path if you want : ')
if x:
    os.chdir(x)

repo = []

for i in tqdm(os.listdir()):
    try:
        if not i.startswith('@'):
            if os.path.isfile(i):
                if not i == str(main_name + '.py') and not i == str(main_name + '.json'):
                    ext = str(i.split('.')[-1]).lower()
                    if not os.path.exists('@Files') or not os.path.isdir('@Files'):
                        os.mkdir('@Files')
                    if ext in list(data.keys()):
                        if not os.path.exists('@Files/@' + data[ext]) or not os.path.isdir('@Files/@' + data[ext]):
                            os.mkdir('@Files/@' + data[ext])
                        if not os.path.exists('@Files/@' + data[ext] + '/'+ ext) or not os.path.isdir('@Files/@' + data[ext] + '/'+ ext):
                            os.mkdir('@Files/@' + data[ext] + '/'+ ext)
                        if not os.path.exists('@Files/@' + data[ext] + '/'+ ext + '/' + i):
                            shutil.move(i, '@Files/@' + data[ext] + '/' + ext + '/'+ i)
                            repo.append(str('[-] Success file : ' + str(i) + ' > ' + '@Files/@' + data[ext] + '/' + ext + '/' +'\n'))
                        else:
                            repo.append(str('[x] Error : this file [' + str(i) + '] exists in > '+ '@Files/@' + data[ext] + '/' + ext + '/' + '\n'))
                    else:
                        if not os.path.exists('@Files/@Incconu') or not os.path.isdir('@Files/@Incconu'):
                            os.mkdir('@Files/@Incconu')
                        shutil.move(i, '@Files/@Incconu/'+ i)
                        repo.append(str('[-] Success file : ' + str(i) + '> @Files/@Incconu/' + '\n'))
            else:
                if not os.path.exists('@Folder') or not os.path.isdir('@Folder'):
                    os.mkdir('@Folder')
                if os.path.exists('@Folder/' + i):
                    for g in os.listdir(i):
                        shutil.move(i + '/' + g, '@Folder/'+ i + '/'+ g)
                        repo.append(str('[-] Success folder: ' + str(g) + ' > @Folder/' + str(i) + '\n'))
                else:
                    shutil.move(i, '@Folder/'+ i)
                    repo.append(str('[-] Success folder: ' + str(i) + ' > @Folder/' + str(i) + '\n'))
    except:
        repo.append(str('[x] Error : ' + str(i) + '\n'))


with open('report.log' , 'w') as f:
    for i in repo:
        f.write(i)

print('[+] end read file')
os.remove(main_name+'.json')

input('Press [ENTER] to exit... ')
