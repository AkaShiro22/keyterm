import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Shorcut for help you')
print(b+'\t    🧟‍♂卂nonymous Tips & Tricks🧟‍♂')
print('\t https://t.me/joinchat/AAAAAEtEH9fNBYvSkzAXNA')
print(a+'+'*40)
print('\nProcess..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nJoin Group https://t.me/joinchat/AAAAAEtEH9fNBYvSkzAXNA \nThanks :*\n\n')


# ini cuma shortcut buat bantu para nub
# 🧟‍♂卂nonymous Tips & Tricks🧟‍♂