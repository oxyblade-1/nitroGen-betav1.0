from bs4 import BeautifulSoup
import os
import time
import random
import requests
import ascii_magic
os.system("cls")

#ASCII ART

output = ascii_magic.from_image_file("wumpus.png",columns=50)
ascii_magic.to_terminal(output)

print("\033[35m███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗")
print("\033[35m████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║")
print("\033[35m██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║")
print("\033[35m██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║")
print("\033[35m██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║")
print("\033[35m╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝")



#code = "htpps://lien.test"
#print("\033[0;31m[invalid] " + f"\033[1;30m{code}")
#API CHECKER = https://discord.com/api/v8/entitlements/gift-codes/
# CTP32GURUwYJd6zV = 16 valeur random

print("\033[1;30m__________________________________________________________\n\n")

#system code:

#"https://discord.gift/PReTFZwxDwgZCXYC"
print("\033[1;30msystem created by \033[35moxyblade")
print("\033[1;30mv1.0 \033[0;31malfa 1.0")

#nitro number
caracter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
gift_number = int(input("\033[1;30mnitro number generate: \033[1;35m"))

print("\n\033[1;30m__________________________________________________________\n")

package = 0
repeat = 0

while True:
	nitrocaracter = ""
	limit_pack = 10

	for i in range(16):
		nitrocaracter = f"{nitrocaracter}{random.choice(caracter)}"
		giftcode = f"https://discord.gift/{nitrocaracter}"


	link = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitrocaracter}"

	#delais de requête
	time.sleep(12)

	page = requests.get(link) #obtenir le code de la page
	json = page.json()
	api = json.get("message")

	if api == "Unknown Gift Code":
		print("\033[0;34m[LOG] \033[35minvalid")

	elif api == "The resource is being rate limited.":
		package += 1
		print("\033[0;34m[LOG] \033[0;31mmany request")

		if package == limit_pack:
			print("\033[0;34m[LOG] \033[0;31msystem out [change IP]") # changer l'ip
			break

	else:
		print(f"\033[0;34m[LOG] \033[0;32m{giftcode}")
		gift_file = open("giftcode.txt","w")
		gift_file.write(f"{giftcode}") # affichage du code nitro (si fonctionne ...)
		repeat += 1 # ajout d'un warning IP 

	

print("\n")