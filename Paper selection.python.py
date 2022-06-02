import random
game =['R','P','S']
userOpt = 'R' 
compOpt = 'R' 
while (userOpt == comOpt):
print ()
print('Rock-Paper-Scissors')
print ()
print ('Use the following input methods for selection')
print ('Input R for Rock')
print ('Input P for Paper')
print ('Input S for Scissors')
print ()

userOpt = input('Pick a game option: ')
userOpt = userOpt.upper()

if userOpt in game:

compOpt = random.choice(game)

  if (compOpt=='R' and userOpt=='S'):
   print ('Computer wins')

  elif (compOpt=='P' and userOpt=='R'):
    print ('Computer wins')

  elif (compOpt=='S' and userOpt=='P'):
     print ('Computer wins')

  elif (compOpt == userOpt):
      print ('TIE')

   else:
       print("You Win")

    else:
        userOpt = 'R'
        print()
        print("Invalid Input")
        print ("Pick a Valid Selection")

    else:
        print ("Thank you for playing")
