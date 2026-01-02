# Building Snake-Water-Gun game.

# Importing required python modules.
import random

# Variable block of the game.
comp= random.choice([-1,0,1])
youstr= input("enter your choice(s/w/g): ")
youdict={"s":-1,"w":0,"g":1}
reversedict={-1:"snake",0:"water",1:"gun"}
you=youdict[youstr]
print(f"you chose {reversedict[youdict[youstr]]} and the computer chose {reversedict[comp]}.")

# Logic block of the game.
if (comp == you):
    print("Its a draw")
elif (comp == -1 and you==0):
    print("You lose.Better luck next time.")
elif (comp == -1 and you==1):
    print("Yay!You win")
elif (comp == 0 and you==-1):
    print("Yay!You win")
elif (comp == 0 and you==1):
     print("You lose.Better luck next time.")
elif (comp == 1 and you==-1):
    print("You lose.Better luck next time.")
elif (comp == 1 and you==0):
    print("Yay!You win")
else :
    print("something went wrong")               

# You can now run the game.