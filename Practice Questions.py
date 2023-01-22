# Snake Water Gun Game or Rock Paper Scissor
import random as rand

def game(comp,you) : 
    if comp == you : 
        return None
    elif comp == 's' : 
        if you == 'w' : 
            return False
        elif you == 'g' : 
            return True
    elif comp == 'w' : 
        if you == 'g' : 
            return False
        elif you == 's' : 
            return True
    elif comp == 'g' : 
        if you == 's' : 
            return False
        elif you == 'w' : 
            return True
n = int(input("Enter the Number of times you wish to play : "))
p = 0
c = 0
t = 0
while n > 0 : 
    randNo = rand.randint(1,3)
    if randNo == 1 : 
        comp = 's'
    elif randNo == 2 : 
        comp = 'w'
    elif randNo == 3 : 
        comp = 'g'
    you = input("Player's Turn : Snake(s) Water(w) or Gun(g)? : ")
    if you == "Score" or you == "score" or you == "SCORE" :
        print(f"Score : {p} to player and {c} to the computer and the number of ties are {t}")
    if you == "Score" or you == "score" or you == "SCORE" :
        a = ''
        n = n + 1
    elif you == 'exit' or you == "Exit" or you == "EXIT" : 
        break
    else : 
        a = game(comp,you)
        print(f"Computer Chose {comp}")
        print(f"You Chose {you}")
        if a == None : 
            print("The Game is a Tie")
            t = t + 1
        elif a == True : 
            print("You Win")
            p = p + 1
        elif a == False : 
            print("You Lost Lol!!! (>|<)!!")
            c = c + 1
    n = n - 1
print(f"Score : {p} to player and {c} to the computer and the number of ties are {t}")