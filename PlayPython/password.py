import random
import string
ajectives = ['stupid','big','idot','GAMER','brown','purple','questionable','evil','nice','Mean','irish','Canadian','Capitalist','Comunist']
nouns = ['GAMER','gamer','Gamer','Elephant','Lion','Stupid dog','Rabit','Lepricon','explosion','Commenter','Youtuber','Presidnet','Dictator']
print('Your making a mistake!')
A1 = random.choice(ajectives)
A2 = random.choice(nouns)
A3 = random.randrange(0,1000000)
special_char = random.choice(string.punctuation) 
password = A1 + A2 + str(A3) + special_char
print(f'Well your password is now: {password}')