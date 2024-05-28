import os
import shutil

def fcr():
	os.system('mkdir 1сюда-SC > /dev/null 2>&1')
	os.system('mkdir 2отсюда-PNG > /dev/null 2>&1')
	os.system('mkdir 3сюда-PNG > /dev/null 2>&1')
	os.system('mkdir 4отсюда-SC > /dev/null 2>&1')

of = "./1сюда-SC"
tf = "./2отсюда-PNG"
rf = "./3сюда-PNG"
ff = "./4отсюда-SC"

def lbl2():
    print("Очистить все папки от файлов?")
lbl2()

def cm2():
    try:
        nema = int(input("нажми Enter для подтверждения: "))
    except:
        shutil.rmtree(of)
        shutil.rmtree(tf)
        shutil.rmtree(rf)
        shutil.rmtree(ff)
        fcr()
cm2()