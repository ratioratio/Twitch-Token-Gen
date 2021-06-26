import random, string
from os import system
import time
import ctypes
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("Awsome's Token Gen")
print(f"{Fore.RED}")
print("""
  _______       _ _       _       _______    _                 _____            
 |__   __|     (_) |     | |     |__   __|  | |               / ____|           
    | |_      ___| |_ ___| |__      | | ___ | | _____ _ __   | |  __  ___ _ __  
    | \ \ /\ / / | __/ __| '_ \     | |/ _ \| |/ / _ \ '_ \  | | |_ |/ _ \ '_ \ 
    | |\ V  V /| | || (__| | | |    | | (_) |   <  __/ | | | | |__| |  __/ | | |
    |_| \_/\_/ |_|\__\___|_| |_|    |_|\___/|_|\_\___|_| |_|  \_____|\___|_| |_|
                                                                                
                                                                                
""")
time.sleep(2)
print("Owner: Awsome#0001 ")
time.sleep(0.5)
print("follow the instructions below   \n")
time.sleep(0.2)

num=input('how many tokens to gen?: ')


f=open("tokens.txt","w", encoding='utf-8')

print("Wait a bit!")
for n in range(int(num)):
   y = ''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(30))
   f.write(y)
   f.write("\n")


a_file = open("tokens.txt")

lines = a_file.readlines()
for line in lines:
    print(line)


a_file.close()