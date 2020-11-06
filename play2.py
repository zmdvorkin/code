import random
    
print ("Hello World ")
name = input ("What is your name?\n")

# lines starting with a lbs sign are comments

countTimes = 5 # comments are good! Use them well
answer = "notsetyet"
cheese = "notsetyet"
if name.lower() == "apple":
    print ("Hello Secret Agent")
    answer = input(f"Would you like a cookie {name}\n")
    cheese = input("Did you cut the cheese?\n")
else:
      print (f"Good Bye {name}")

if answer == "no" or answer == "nein":
    print (f"Too bad n00b cookies for all agents")
else:
  print ("Yay!")
  if cheese.upper() == "YES":
      print ("Nothing happened")