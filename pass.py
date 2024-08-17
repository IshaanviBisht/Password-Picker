import random
import string

print("Want to be safe online? Make a secure password here!")

adjectives = [
    'Adroit', 'Arcadian', 'Cerulean', 'Comely', 'Equanimous',
    'Garrulous', 'Limpid', 'Luminous', 'Munificent', 'Risible',
    'Sagacious', 'Zealous', 'Sartorial'
] #different adjectives

nouns = [
    'Aurora', 'Elixir', 'Eudaemonia', 'Idyllic', 'Mellifluous',
    'Pristine', 'Sonorous', 'Wanderlust', 'Sumptuous', 'Sequoia',
    'Scintilla', 'Serendipity'
] #different nouns 

while True:
    adjective = random.choice(adjectives) #this will choose a random adjective by choice() func
    noun = random.choice(nouns)
    number = random.randrange(0, 100) #this will choose a random number between 0 to 100
    special_char = random.choice(string.punctuation)# this will choose a random special character!

    password = adjective + noun + str(number) + special_char #This variable will be the mix of all of them

    print("Your new password is:", password)

    reply = input("Would you like another password? (Reply with y or n)")
    if reply == "n":
        print("Thank you for trying the Password Picker!")
        break #breaking the while loop