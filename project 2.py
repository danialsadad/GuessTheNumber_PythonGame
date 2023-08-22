import random
randNum= random.randint(1, 100)
# print(randNum)
userguess=None
guess= 0

while userguess!= randNum:
    userguess=int(input("Enter your guess: "))
    guess += 1
    if userguess== randNum:
      print("You Guessed it right!")
    else:
      if userguess>randNum:
        print("You guessed wrong! Enter a smaller number: ")
      else:
        print("You guessed wrong! Enter a larger number: ")

print(f"You guessed the number in {guess} guesses")  
with open("highscore of p2.txt", "r") as f:
  highscore= int(f.read())

if guess<highscore:
  print("You have just broken the high score!")
  with open("highscore of p2.txt", "w") as f:
    f.write(str(guess))
  
  