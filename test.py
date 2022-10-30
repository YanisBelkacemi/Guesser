import random
import keyboard
import os
from colorama import init
from colorama import Fore
#startup process and needed variables
init(autoreset=True)
points = 0
os.system('cls')
os.system('clear')

print (Fore.BLUE + """
	 ██████╗ ██╗   ██╗███████╗███████╗███████╗███████╗██████╗ 
	██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
	██║  ███╗██║   ██║█████╗  ███████╗███████╗█████╗  ██████╔╝
	██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██╔══╝  ██╔══██╗
	╚██████╔╝╚██████╔╝███████╗███████║███████║███████╗██║  ██║
	 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                          
""")
print(Fore.RED + 'Press "Enter" Then "Ctrl+q" to exit ')



	



#function
def rando():
	global num
	num = random.randint(100,200)



def guesser():
	R = random.randint(1,5)
	bigger = num+ R
	smaller = num-R
	devided = num/2
	print(Fore.GREEN + "Your points are : " + str(points))
	print('--> |the number is beetween ' + str(bigger) + " and " + str(smaller) + "\n--> |devided by 2 Eqaul to " + str(devided) )

def inputs():
	global inpu
	inpu = input('what is this number : ')

#calls th functions for the first time
rando()
guesser()
inputs()
while True:
	#checks your input
	if inpu == str(num):
		points +=1
		rando()
		guesser()
		inputs()
	elif inpu == "":
		break
	
	else:	
		print(Fore.RED + f"""
------------------------------
																						
incorrect 																				
you have lost all your points															
lost points : {points}
The right answer was : {num}																						
------------------------------
			""")
		points = 0
		rando()
		guesser()
		inputs()

# to keep the script
while True:
	if keyboard.is_pressed('ctrl'):
		if keyboard.is_pressed("q"):
			print('Leaving The script...')
			break
	else:
		pass