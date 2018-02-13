import random
list=["A","B","C","D","E","F","G","H","I","J","A","B","C","D","E","F","G","H","I","J"]
random.shuffle (list)
z=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print ("welcome: " , z)
score1=0
score2=0
while (z!=["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]):
    a=int(input("player1 please,choose the first number between 1 and 20 "))
    b=int(input("player1 please,choose the second number between 1 and 20 "))
    z[a-1]=list[a-1]
    z[b-1]=list[b-1]
    print (z)
    if (z[a-1]==z[b-1]):
        z[a-1]=z[b-1]=list[a-1]=list[b-1]="*"
        score1=score1+1
        print ("the score of player1= ", score1)
        print (z)
    else:
        z[a-1]=a
        z[b-1]=b
        print ("player1 score= ",score1)
        print (z)
    c=int(input("welcome player2 please,choose the first number between 1 and 20 "))
    d=int(input("welcome player2 please,choose the second number between 1 and 20 "))
    z[c-1]=list[c-1]
    z[d-1]=list[d-1]
    print (z)
    
    if (z[c-1]==z[d-1]):
        z[c-1]=z[d-1]=list[c-1]=list[d-1]="*"
        score2=score2+1
        print ("the score of player2= ", score2)
        print (z)
    else:
        z[c-1]=c
        z[d-1]=d
        print ("the score of player2= ", score2)
        print (z)
if (score1>score2):
    print ("player1 won! ")
else:
    print ("player2 won! ")
        






                
