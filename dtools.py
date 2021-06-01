try:
    import os, sys, time, requests, datetime, phonenumbers
except ImportError:
    try:
        os.system('pip3 install requests')
        os.system('pip3 install time')
        os.system('pip3 install datetime')
        os.system('pip3 install phonenumbers')
    except:
        if sys.platform == 'win32':
            os.system('python -m pip install requests')
            os.system('python -m pip install time')
            os.system('python -m pip install datetime')
            os.system('python -m pip install phonenumbers')
        if sys.platform == 'linux':
            os.system('sudo pip3 install requests')
            os.system('sudo pip3 install time')
            os.system('sudo pip3 install datetime')
            os.system('sudo pip3 install phonenumbers')
    
    

from phonenumbers import geocoder, carrier, timezone
from sys import platform



def bersih():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "darwin":
        os.system("clear")
    elif platform == "win32" or platform == "win64":
        os.system("cls")
    else:
        os.system("clear")


def cekupdate():
    r = requests.get("https://pastebin.com/raw/qyeD0ZEz")
    k = r.text
    if k == "1.1":
        print(f"-~=>Versi {r.text}")
    else:
        print("Tolong Update ke versi selanjutnya!")

def tools1():
    print("Masukan Nomor! \ncontoh +62123456789")
    nomor = input("-~=>")
    phone = phonenumbers.parse(nomor)
    a = geocoder.description_for_number(phone, "en")
    b = carrier.name_for_number(phone, "en")
    c = timezone.time_zones_for_number(phone)
    print("")
    print(f"-~=>Negara/Country > {a}")
    print(f"-~=>Provider > {b}")
    print(f"-~=>Time Zone > {c}")

def menu():
    bersih()
    cekupdate()
    date = datetime.datetime.now()
    print("-~=>Tools By Domino")
    print("-~=>Sector Tester")
    print(f"-~=>Sytem : {platform}")
    print(f'-~=>{date.strftime("%A %d %m %Y")}')
    print("|||||||||||||||||||||||||||||||||||")
    print("-~=>[1] Cek informasi nomor telfon")
    pilih = input("-~=>")
    if pilih == "1":
        tools1()
    else:
        menu()
menu()
