import random
file="words.txt"
print("WELCOME TO THE GAME WORLD")
print("      HANGMAN                  ")
print("Enter Your Name : ")
name=str(input())
def loadwords():
    infile=open(file,'r')
    line=infile.read()
    words=line.split()
    return words
def choosewords(words):
    return random.choice(words)
def getgword(sword,gword):
    string=""
    for k in sword:
        if k in gword:
            string+=k
        else:
            string+='_'
    return string
def getavailableletters(gword):
    string=""
    c=0
    s="abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i in gword:
            c+=1
        else:
            string+=i
    return string
def hangman(sword):
    length=len(sword)
    print("I am thinking a word of length : ",length)
    chances=2*length
    gword=[]
    while(chances!=0):
        if sword!=getgword(sword,gword):
            print(getgword(sword,gword))
            print("You have ",chances," chances left")
            print("Available letters are : "+getavailableletters(gword))
            guess=input("Enter the letter which is guessed : ")
            guess=guess.lower()
            if guess in gword:
                print("OOPS!!!! you have already guessed the letter")
            elif guess not in sword:
                print("OOPS!!!! you entered a wrong letter ",getavailableletters(gword))
                chances=chances-1
            elif len(guess)==0:
                print("You didnt enter any letter..")
            else:
                print("GOOD GUESS ",name)
            gword.append(guess)
        else:
            print("CONGRATULATIONS "+name+"!!!! You Nailed it!!!")
            break
    else:
        print("SORRY "+name+" !!!! you lost....")
        print("The secret word is : ",sword)


words=loadwords()
sword=choosewords(words).lower()
hangman(sword)
