# # guess the number 
# import random as r
# print("------------------- Greetings !! -----------------")
# ch=input("READY TO PLAY THE GAME\nEnter Yes or No : ").capitalize()
# if ch=="Yes":
#     lvl=input("Difficulty Level : \n1. Advance\n2. Moderate\n3. Beginner\nEnter difficulty level : ")
#     if lvl=="1":
#         print("Guess The Number between 1 to 100")
#         print("No. of Attempts : 5")
#         c=r.randint(1,100)
#         for i in range(5):
#             a=int(input("Enter your no. : "))
#             if a==c:
#                 print("-----------------Hurray!,you have guessed the number.")
#                 print("SCORE : ",2*(i+1),"/",10)
#                 break
#             elif a>c:
#                 print("Too High\nTry Again")
#                 print("No. of attempts left ",4-i)
#             elif a<c:
#                 print("Too Low\nTry Again")
#                 print("No. of attempts left ",4-i)
#         else:
#             print("SCORE : 0/10 \nOH! You have lost. BETTER LUCK NEXT TIME")
#     elif lvl=="2":
#         print("Guess The Number between 1 to 50")
#         print("No. of attempts : 10")
#         c=r.randint(1,50)
#         for i in range(10):
#             a=int(input("Enter your no. : "))
#             if a==c:
#                 print("-----------------Hurray!,you have guessed the number.")
#                 print("SCORE : ",i+1,"/",10)
#                 break
#             elif a>c:
#                 print("Too High\nTry Again")
#                 print("No. of attempts left ",9-i)
#             elif a<c:
#                 print("Too Low\nTry Again")
#                 print("No. of attempts left ",9-i)
#         else:
#             print("SCORE : 0/10 \nOH! You have lost. BETTER LUCK NEXT TIME")
#     elif lvl=="3":
#         print("Guess The Number between 1 to 100")
#         c=r.randint(1,100)
#         ct=0
#         while 1:
#             a=int(input("Enter your no. : "))
#             if a==c:
#                 print("-----------------Hurray!,you have guessed the number.")
#                 print("SCORE : ",ct%10,"/",10)
#                 break
#             elif a>c:
#                 print("Too High\nTry Again")
#                 c=c+1
#             elif a<c:
#                 print("Too Low\nTry Again")
#                 c=c+1
#     else :
#         print("Enter a valid choice.")

#----------------------------------------------####################------------------------------------------------#

# # Rock Paper Scissor:
# # import random module
# import random
# print()
# print("aayie kriya khele ".center(100))
# print()
# print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
# 	+ "Rock vs Paper -> Paper wins \n"
# 	+ "Rock vs Scissors -> Rock wins \n"
# 	+ "Paper vs Scissors -> Scissor wins \n")

# while True:
	
# 	print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	
# 	choice=int(input("Enter your choice :"))
	
	
# 	while choice > 3 or choice <1:
# 	    choice=int(input('Enter a valid choice please '))
# 	if choice == 1:
# 		choice_name= 'Rock'
# 	elif choice == 2:
# 		choice_name= 'Paper'
# 	else:
# 		choice_name= 'Scissors'
		
# 	print('User choice is \n',choice_name)
# 	print()
# 	print('Now its Computers Turn....')
# 	print()
# 	comp_choice = random.randint(1,3)


# 	while comp_choice == choice:
# 		comp_choice = random.randint(1,3)
		
	
# 	if comp_choice == 1:
# 		comp_choice_name = 'rocK'
# 	elif comp_choice == 2:
# 		comp_choice_name = 'papeR'
# 	else:
# 		comp_choice_name = 'scissoR'
# 	print("Computer choice is \n", comp_choice_name)
# 	print(choice_name,'Vs',comp_choice_name)
	
# 	if choice == comp_choice:
# 		print('Its a Draw',end="")
# 		result="DRAW"
	
# 	if (choice==1 and comp_choice==2):
# 		print('paper wins =>',end="")
# 		result='papeR'
# 	elif (choice==2 and comp_choice==1):
# 		print('paper wins =>',end="")
# 		result='Paper'
		
	
# 	if (choice==1 and comp_choice==3):
# 		print('Rock wins =>\n',end= "")
# 		result='Rock'
# 	elif (choice==3 and comp_choice==1):
# 		print('Rock wins =>\n',end= "")
# 		result='rocK'
		
# 	if (choice==2 and comp_choice==3):
# 		print('Scissors wins =>',end="")
# 		result='scissoR'
# 	elif (choice==3 and comp_choice==2):
# 		print('Scissors wins =>',end="")
# 		result='Rock'
	
# 	if result == 'DRAW':
# 		print("<== Its a tie ==>")
# 	if result == choice_name:
# 		print("<== User wins ==>")
# 	else:
# 		print("<== Computer wins ==>")
# 	print("Do you want to play again? (Y/N)")
	
# 	ans = input().lower
# 	if ans =='n':
# 		break

# print("thanks for playing")

#----------------------------------------------####################------------------------------------------------#

# # OTP Generator:

# import math, random
# def generateOTP() :
# 	digits = "0123456789"
# 	OTP = ""
# 	for i in range(4) :
# 		OTP += digits[math.floor(random.random() *10)]

# 	return OTP


# if __name__ == "__main__" :
	
# 	print("OTP of 4 digits:", generateOTP())

#----------------------------------------------####################------------------------------------------------#

# # a game of dice
# import random


# x = "y"

# while x == "y":
	
# 	no = random.randint(1,6)
	
# 	if no == 1:
# 		print("[-----]")
# 		print("[	 ]")
# 		print("[  0  ]")
# 		print("[	 ]")
# 		print("[-----]")
# 	if no == 2:
# 		print("[-----]")
# 		print("[  0  ]")
# 		print("[	 ]")
# 		print("[  0  ]")
# 		print("[-----]")
# 	if no == 3:
# 		print("[-----]")
# 		print("[	 ]")
# 		print("[0 0 0]")
# 		print("[	 ]")
# 		print("[-----]")
# 	if no == 4:
# 		print("[-----]")
# 		print("[ 0 0 ]")
# 		print("[	 ]")
# 		print("[ 0 0 ]")
# 		print("[-----]")
# 	if no == 5:
# 		print("[-----]")
# 		print("[ 0 0 ]")
# 		print("[  0  ]")
# 		print("[ 0 0 ]")
# 		print("[-----]")
# 	if no == 6:
# 		print("[-----]")
# 		print("[0 0 0]")
# 		print("[	 ]")
# 		print("[0 0 0]")
# 		print("[-----]")
		
# 	x=input("press y to roll again and n to exit:")
# 	print("\n")


#----------------------------------------------####################------------------------------------------------#

# # secure password generater
# import random as r
# import string as s
# print("------------------- Greetings !! -----------------")
# while 1:
#     le=r.randint(8,12)
#     u=s.ascii_uppercase
#     l=s.ascii_lowercase
#     d=s.digits
#     sp=s.punctuation
#     a=u+l+d+sp
#     p=list(r.choice(u)+r.choice(l)+r.choice(d)+r.choice(sp)+''.join(r.choices(a,k=le-4)))
#     r.shuffle(p)
#     print()
#     print('Your password is : ',*p,sep='')
#     print()
#     print("----------------------------------------------------")
#     ch=input("Do you want to generate another password ( Yes or No ) : ").capitalize()
#     if ch=="Yes":
#         continue
#     else:
#         break

#----------------------------------------------####################------------------------------------------------#

# # hangman game
# import random as r
# def hang(a):
#     if a==0:
#         print('''
#              +------+ 
#              O      |
#                     |
#                     |
#                     |
#                 +=======+
# ''')
#     if a==1:
#         print('''
#              +------+ 
#              O      |
#              |      |
#                     |
#                     |
#                 +=======+
# ''')
#     if a==2:
#         print('''
#              +------+ 
#              O      |
#             /|      |
#                     |
#                     |
#                 +=======+
# ''')
#     if a==3:
#         print('''
#              +------+ 
#              O      |
#             /|\     |
#                     |
#                     |
#                 +=======+
# ''')
#     if a==4:
#         print('''
#              +------+ 
#              O      |
#             /|\     |
#             /       |
#                     |
#                 +=======+
# ''')
#     if a==5:
#         print('''
#              +------+ 
#              O      |
#             /|\     |
#             / \     |
#                     |
#                 +=======+
# ''')
# s=("fox","rocket","cat","table","laser","computer","python","maths","straw","space","egypt","jaipur","hotel","chair","brinjle","lichi","cashew","temple")
# print("------------------- Greetings !! -----------------")
# ch=input("READY TO PLAY THE GAME\nEnter Yes or No : ").capitalize()
# def hangmangame():
#     if ch=="Yes":
#         a=r.choice(s)
#         m=r.randint(0,len(a))
#         n=r.randint(0,len(a))
#         k=[]
#         for i in range (len(a)):
#             if i==m:
#                 print(a[i],end='')
#                 k.append(a[i])
#             elif i==n:
#                 print(a[i],end='')
#                 k.append(a[i])
#             else:
#                 print("_",end='')
#                 k.append("_")
#         print()
#         ms=[]
#         c=0
#         while True:
#             b=input("Enter the missing alphabet : ").lower()
#             if b in a:
#                 ct=0
#                 for i in range (len(a)):
#                     if b==a[i]:
#                         ct=i
#                 k[ct]=a[ct]
#                 for j in k:
#                     print(j,end=' ')
#                 print()
#                 hang(c)
#                 if k==list(a):
#                     print("---------------Hurray! you have guessed it")
#                     break
#             else:
#                 c=c+1
#                 ms.append(b)
#                 print("Missed letters : ",ms)
#                 for j in k:
#                     print(j,end=' ')
#                 print()
#                 hang(c)
#                 if c==5:
#                     print("Correct answer is : ",a.capitalize(),"\n-------------- Better Luck Next Time")
#                     break
#                 if k==list(a):
#                     print("--------------- Hurray! you have guessed it")
#                     break
#     rec=input("Do you want to play again ( Yes or No ) : ").capitalize()
#     if rec=="Yes":
#         hangmangame()
# hangmangame()
