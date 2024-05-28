import subprocess
import os
import platform
import time
import pip._internal as pip

global sysname
sysname = platform.system()
fp = "./1сюда-SC"
fp2 = "./2отсюда-PNG"
fp3 = "./3сюда-PNG"
fp4 = "./4отсюда-SC"

def chf(file):
    if os.path.isdir(file):
        print("проверка")
    else:
        if sysname == 'Windows':
            os.system(f'mkdir {file} > nul 2>&1')
        else:
            os.system(f'mkdir {file} > /dev/null 2>&1')
chf(fp)
chf(fp2)
chf(fp3)
chf(fp4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    from PIL import Image
except:
    if sysname == 'Windows':
        os.system('pip3 install pillow > nul 2>&1')
    else:
        os.system('pip3 install pillow > /dev/null 2>&1')

def lbl():
    clear()
    print("©Dich Rumpany™ - TrixCoder v1.2.1")
    print(""" команды:
  SC файлы в PNG - 1
  PNG файлы в SC - 2
  удалить из папки файлы - 3
  разработчики - 0""")
lbl()

def cm():
    try:
        name = int(input("впишите команду: "))
    except:
    	print(" упс! такой команды нет ¯\_(ツ)_/¯)")
    	time.sleep(1.7)
    	lbl()
    	cm()
    
    if name == 0:
        print("1 разработчик - Rejzi[Dich]")
        lbl()
        cm()
    
    if name == 1:
        subprocess.run(["python", "SC-PNG.py"])
        lbl()
        cm()
    
    if name == 2:
        subprocess.run(["python", "PNG-SC.py"])
        lbl()
        cm()    

    if name == 3:
        subprocess.run(["python", "dltf.py"])
        print("успешно!")
        time.sleep(1.4)
        lbl()
        cm()    
cm()