import random 

secret = random.randint(1, 10)
guess = 0
tries = 0

print("Guess my number! It's between    1    and    10")

while guess != secret:
    guess = int(input("Your guess:  "))
    tries = tries+ 1  
    
    if guess    <    secret:
        print("Too low! Try again")
    elif guess > secret:
        print("Too high! Try again")
    else:
          print("YOU GOT IT! ")
          print ("It took you", tries, "tries")
