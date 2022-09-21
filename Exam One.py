from random import randint
y = randint(1,5)
hscore = 0
cscore = 0
print("Winners and Losers - Human is Even, Computer is Odd")
for i in range (1, 6) :
    print("Round: {}".format(i))
    x = int(input("Enter Your Guess: "))
    print ("Human Guess: {} - Computer Guess: {}".format(x , y))
    sum = x + y
    if sum % 2 :
        print("Sum is Even")
        hscore = hscore + 1
    else:
        print("Sum is Odd")
        cscore = cscore + 1
    print ("Human Score: {} - Computer Score: {}".format (hscore, cscore))
if hscore > cscore :
        print ("Human Wins")
else :
        print ("Computer Wins")