import random, string
import webbrowser
import time
import requests
from colorama import Fore



print("""
Nictro gen""")
time.sleep(2)
print("Creator  -  cqbra ")
time.sleep(0.3)
print("https://github.com/ghostydev   \n")
time.sleep(0.2)

num=input('Input How Many Codes to Generate and Check: ')

f=open("Codes.txt","w", encoding='utf-8')

print("Wait, Generating for you!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
            exit()
        else:
        	print(f"{Fore.RED}Invalid".format(line.strip("\n")))
          

input("The end! Press Enter 5 times to close the program.")
input("4")
input("3")
input("2")
input("1")
