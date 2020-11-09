from dataclasses import dataclass


## Goal, guess the password in as few attempts as possible. 

@dataclass
class GuessPasswordReturn:
    IsHacked: bool
    Password: str
    PasswordsTried: int

def GuessPassword(password):
    print (f"The passed in password is {password}")
    r = GuessPasswordReturn(IsHacked=False, Password="", PasswordsTried=0)
    for i in range (999):
        if password == i: 
            r.IsHacked = True



    return r

def GuessPasswordAnimal(password):
    print (f"The passed in password is {password}")
    r = GuessPasswordReturn(IsHacked=False, Password="", PasswordsTried=0)
    r.PasswordsTried += 1
    if password == "cat":
        r.IsHacked = True
        return r
    
    r.PasswordsTried += 1
    if password == "dog":
        r.IsHacked = True

    return r

users_password = input(f"Enter a password\n")
ret = GuessPassword(users_password)

print (f"Hack Success: {ret.IsHacked} : Number of Tries {ret.PasswordsTried}")

#cool a object
#lightbulb?





           