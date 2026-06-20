import random
l=['summer','winter','spring','autumn','python','idiom','aluminium','sodium','forest','chemistry','zoology']
guess=0
r=random.choice(l)
a=input("what is your name ?")
print("hello",a,"lets play a game")
print("you have to find the word with the given clues")
print("you have got only 4 chance")
print("all the best")
pt=0
gm=input("do u want to continue")
while gm=="yes" or gm=="s":
    if r=='summer':
        print("this is a season")
        print("this season is very hot")
        print("icecreams are the best solns")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='winter':
        print("this is a season")
        print("this season is very cold")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='spring':
        print("this is a season")
        print("this season comes after colder winter months")
        print("christmas comes during this period")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='autumn':
        print("this is a season")
        print("this season marks the transition in september to march")
        print("the daylight becomes shorter")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='python':
        print("this is used for coding")
        print("very feasible platform")
        print("high level programming language")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='chemistry':
        print("this is a subject")
        print("study of properties and behavior of matter")
        print("it is a branch of physical science")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='aluminium':
        print("this is a chemical element")
        print("it is a lightweight metal")
        print("it is used in kitchen utensils")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='sodium':
        print("this is a chemical element")
        print("it is a highly reactive metal")
        print("it is used as a binderand stabilizer")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
            else:
                guess+=1
    elif r=='forest':
        print("it is a region with high density of trees")
        print("it is a habitat for variety of living species")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
    elif r=='idiom':
        print("a characteristic mode of expression")
        print("these phrases cannot be understood just by looking")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
            else:
                guess+=1
    elif r=='zoology':
        print("this is a subject")
        print("it is the study of animals")
        while guess <3:
            a=input("what is your guess ?")
            if  a==r:
                pt+=10
                print("you found it !")
                break
            else:
                guess+=1
print(r)
print("                                 congratulations! your point is",pt)
