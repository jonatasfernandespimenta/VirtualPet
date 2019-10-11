import os
import time
from random import randrange
from random import randint
import asyncio
import ticking

os.system('color f0')

print('\nAvisos: Quanto maior os valores na tela maior a necessidade, exemplo, Fome = 10, ele está com muita fome, Diverçao = 10, ele está entediado...')
print('\nAlgumas artes foram pegas em https://www.asciiart.eu')

print('\n\n  _   ,_,   _')
print(" / `'=) (='` \            1 - Morcego")
print("/.-.-.\ /.-.-.\ ")
print('`      "      `')

print('\n\n /\ /\ ')
print('((ovo))                   2 - Coruja')
print('():::()')
print('  VVV')

print('\n\n   ___  ') 
print('  (o o) ')
print(' (  V  )                  3 - Passarinho') 
print('/--m-m-')

print("\n\n\    /\ ")
print(" )  ( ')")
print(" (  /  )                  4 - Gatinho")
print("  \(__)|")

print("\n\n  //")
print(" ('>")
print(" /rr                      5 - Coelhinho")
print("*\))_")

print("\n\n  /^ ^\ ")
print(" / 0 0 \ ")
print(" V\ Y /V                  6 - Cachorrinho")
print("  / - \ ")
print(" /    |")
print("V__) ||")

print('\n\nSelecione seu pet pelo número')
petsele = input('\n> ')
if petsele == '1':
	def pet():
		print('\n\t  _   ,_,   _')
		print("\t / `'=) (='` \ ")
		print("\t/.-.-.\ /.-.-.\ ")
		print('\t`      "      `')

	def petsleep():
		print('\n\t  _   -_-   _')
		print("\t / `'=) (='` \ ")
		print("\t/.-.-.\ /.-.-.\ ")
		print('\t`      "      `')

elif petsele == '2':
	def pet():
		print('\n\t /\ /\ ')
		print('\t((ovo))')
		print('\t():::()')
		print('\t  VVV')

	def petsleep():
		print('\n\t /\ /\ ')
		print('\t((-v-))')
		print('\t():::()')
		print('\t  VVV')	

elif petsele == '3':
	def pet():
		print('\n\t   ___  ') 
		print('\t  (o o) ')
		print('\t (  V  )') 
		print('\t/--m-m-')

	def petsleep():
		print('\n\t   ___  ') 
		print('\t  (- -) ')
		print('\t (  V  )') 
		print('\t/--m-m-')	

elif petsele == '4':
	def pet():
		print("\n\t\    /\ ")
		print("\t )  ( ')")
		print("\t (  /  )")
		print("\t  \(__)|")

	def petsleep():
		print("\n\t\    /\ ")
		print("\t )  ( -)")
		print("\t (  /  )")
		print("\t  \(__)|")

elif petsele == '5':
	def pet():
		print("\n\t  //")
		print("\t ('>")
		print(" \t/rr")
		print("\t*\))_")

	def petsleep():
		print("\n\t  //")
		print("\t (->")
		print(" \t/rr")
		print("\t*\))_")

elif petsele == '6':
	def pet():
		print("\n\t /^ ^\ ")
		print(" \t/ 0 0 \ ")
		print(" \tV\ Y /V")
		print(" \t / - \ ")
		print(" \t/    |")
		print("\tV__) ||")

	def petsleep():
		print("\n\t /^ ^\ ")
		print(" \t/ - - \ ")
		print(" \tV\ Y /V")
		print(" \t / - \ ")
		print(" \t/    |")
		print("\tV__) ||")

else:
	def pet():
		print('\n\t -------')
		print('\t| ° v ° |')
		print('\t -------')

	def petsleep():
		print('\t -------')
		print('\t| - v - |')
		print('\t -------')

os.system('cls')

print('\nInsira o nome do seu pet: ')
name = input('\n> ')
time.sleep(1)
os.system('cls')

gold = 0
cama = '0'

player = False
t = ["Pedra", "Papel", "Tesoura"]
computer = t[randint(0,2)]

stats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
energia = stats[randint(0, 9)]
fun = stats[randint(0, 9)]
fome = stats[randint(0, 9)]

while True:

	if time.clock() > 23:
		stats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		energia = stats[randint(0, 9)]
		fun = stats[randint(0, 9)]
		fome = stats[randint(0, 9)]

	def comer():
		global fome
		print('\nDeseja alimenta-lo?(s/n) ')
		darcomida = input('\n> ')
		if darcomida == 's':
			fome = fome - 1

	def dormir():
		global energia
		global cama
		print('\nDeseja faze-lo dormir?(s/n)')
		dormir = input('\n> ')
		if dormir == 's':
			if cama == '0':
				energia = energia - 1
			elif cama == '1':
				energia = energia - 2
			elif cama == '2':
				energia = energia - 5

	def loja():
		global cama
		global gold
		os.system('cls')
		print('\n Numero no catalogo: 1')
		print('   .         .')
		print('  /|________/|')
		print(' // /      //| "R$ 2000,00"')
		print('|/_/______|//!  "Esta cama diminuirá a energia de seu pet em 2"')
		print('|_________|/')
		print('!         !')

		print('\n Numero no catalogo: 2')
		print('  ()___')
		print('()//__/)_________________()')
		print('||(___)//#/_/#/_/#/_/#()/||  "R$ 5000,00"')
		print('||----|#| |#|_|#|_|#|_|| || "Esta cama irá diminuir a energia de seu pet em 5"')
		print('||____|_|#|_|#|_|#|_|#||/||')

		print('\n\nQual item você deseja??')
		select = input('\n> ')
		if select == '1':
			if gold > 1999:
				gold = gold - 2000
				cama = '1'
			else:
				print('\nVocê não possui dinheiro suficiente')

		elif select == '2':
			if gold > 4999:
				gold = gold - 5000
				cama = '2'
			else:
				print('\nVocê não possui dinheiro suficiente')

	print('Oi, eu me chamo ', name, '\n\nSeu dinheiro atual é R$ ', gold, '  \nEnergia: ', energia, '\nFome: ', fome, '\nDiversão: ', fun)
	pet()

	if fun > 5:
		print('\nAh, que tédio')

	if fun > 7:
		print('\nEstou muito entediado, brinca comigo por favor')

	if fun == 8:
		print('\nVocê não liga pra mim ;-;')

	if fun == 9:
		print('\nSeu pet ficou muito desapontado com você e preferiu ir encontrar outro dono')
		os.system('pause')
		break

	if energia > 5:
		print('\nAi ai, que soninho')

	if energia > 7:
		print('Estou com muito sono, me faça dormir por favor')

	if energia == 8:
		print('Vou acabar morrendo de sono')

	if energia == 9:
		print('\nSeu pet morreu de sono')
		os.system('pause')
		break

	if energia == 0:
		print('Eu estou sem sono')

	if energia == -1:
		print('Eu não quero mais dormir, PARA! ;-;')

	if energia < -2:
		print('Seu pet foi embora por sua culpa, PARABENS SEU MONSTRO')
		os.system('pause')
		break

	if fome > 5:
		print('\nEstou com fome, me alimente ;-;')

	if fome > 7:
		print('\nEu vou morrer de fome ;-;')

	if fome == 8:
		print('\nMe alimenta por favor!!!! ;-;-;-;-;')

	if fome == 9:
		print('\nSeu pet morreu de fome')
		os.system('pause')
		break

	if fome == 0:
		print('\nEstou muito cheio')

	if fome == -1:
		print('\nChega por favor ;-;-;-;')

	print('\nOpções: 1 = Alimentar, 2 = Fazer dormir, 3 = Jogar, 4 = Lojinha')
	x = input('\n> ')
	if x == '1':
		comer()
		print('\nHmmm, que delicia :D')
		time.sleep(1)
		os.system('cls')

	elif x == '2':
		dormir()
		os.system('cls')
		os.system('color 0f')
		print('\tZ\n\t\tZ\n\t\t\tZ')
		petsleep()
		time.sleep(5)
		os.system('cls')
		os.system('color f0')

	elif x == '3':
		fun = fun - 1
		os.system('cls')
		while player == False:
			print('pedra, papel ou tesoura?')
			player = input('\n> ')
			if player == computer:
				print('Empate!!\n')
			elif player == 'Papel' or 'papel' or 'PAPEL':
				if computer == 'Tesoura':
					print('Derrota :c')
				else:
					print('Você ganhou :D')
					gold = gold + 5
			elif player == 'Tesoura' or 'TESOURA' or 'tesoura':
				if computer == 'Pedra':
					print('Derrota :c')
				else:
					print('Você ganhou :D')
					gold = gold + 5
			elif player == 'Pedra' or 'PEDRA' or 'pedra':
				if computer == 'Papel':
					print('Derrota :c')
				else:
					print('Você ganhou :D')
					gold = gold + 5
			else:
				print('Esta não é uma entrada válida')

			player = False
			computer = t[randint(0,2)]
			time.sleep(2)
			os.system('cls')
			break

	elif x == '4':	
		os.system('cls')
		loja()
		time.sleep(2)
		os.system('cls')

	elif x == 'money':
		gold = 9999999999999999
		os.system('cls')

	elif x == 'ilovezelda':
		os.system('cls')
		print("                                   /@")
		print("		                     __        __   /\/ ")
		print("		                    /==\      /  \_/\/    ")
		print("		                  /======\    \/\__ \__ ")
		print("		                /==/\  /\==\    /\_|__ \ ")
		print("		             /==/    ||    \=\ / / / /_/ ")
		print("		           /=/    /\ || /\   \=\/ /      ")
		print("		        /===/   /   \||/   \   \===\ ")
		print("		      /===/   /_________________ \===\ ")
		print("				   /====/   / |                /  \====\ ")
		print("		 /====/   /   |  _________    /  \   \===\    THE LEGEND OF  ")
		print("		 /==/   /     | /   /  \ / / /  __________\_____      ______       ___ ")
		print("		|===| /       |/   /____/ / /   \   _____ |\   /      \   _ \      \  \ ")
		print("		 \==\             /\   / / /     | |  /= \| | |        | | \ \     / _ \ ")
		print("		 \===\__    \    /  \ / / /   /  | | /===/  | |        | |  \ \   / / \ \ ")
		print("		   \==\ \    \\ /____/   /_\ //  | |_____/| | |        | |   | | / /___\ \ ")
		print("		   \===\ \   \\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  | ")
		print("		     \==\/     \\\\/ / //////   \| |/==/ \| | |        | |   | | | /   \ | ")
		print("		     \==\     _ \\/ / /////    _ | |==/     | |        | |  / /  | |   | | ")
		print("		       \==\  / \ / / ///      /|\| |_____/| | |_____/| | |_/ /   | |   | | ")
		print("		       \==\ /   / / /________/ |/_________|/_________|/_____/   /___\ /___\ ")
		print("		         \==\  /               | /==/ ")
		print("		         \=\  /________________|/=/    OCARINA OF TIME ")
		print("		           \==\     _____     /==/  ")
		print("		          / \===\   \   /   /===/ ")
		print("		         / / /\===\  \_/  /===/ ")
		print("		        / / /   \====\ /====/ ")
		print("		       / / /      \===|===/ ")
		print("		       |/_/         \===/ ")
		print("		                      = ")
		time.sleep(3)
		os.system('cls')

	if fome < -1:
		print('\nSeu pet morreu de má digestão')
		os.system('pause')
		break