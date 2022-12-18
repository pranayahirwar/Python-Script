import random 
def userGuess(x):

    secret = random.randint(1, x)
    userValue = 0
    while userValue != secret:
        userValue = int(input(f'Enter Please, between Range 1 - {x}: '))
        if userValue < secret:
            print(f'You are just there, a little bit higher!!!')
            print()
            
        else:
            print(f'Almost, a little bit lower :) ')
            print()
    print(f'Good Job you mate it. The number was: {userValue}')
    # return secret

def computerGuess(x):
    low = 1
    high = x
    userDecision = 's'

    while userDecision != 'c' and low < high:
        secret = random.randint(low, high)
        print(f"Hey this is PC, is your number was --> {secret}")
        userDecision = input("Users Inputs \n --> C = Correct \n --> H = Too High \n --> L = Too Low \nUser's Decision: ")
        if userDecision == 'h':
            high = secret - 1
        elif userDecision == 'l':
            low = secret + 1
        
    if low >= high:
        print(f"OPPSI !!! User is Dump, sorry PC :( ")
        print(f"PC's Last gussed number was: {secret}")
    else:
        print(f'You did it PC !!! - The number was : {secret}')
        
# userGuess(10)
computerGuess(10)