from random import randint

#this is how I can make my own comments
#available weapons => store this in an array 
choices = ["Rock", "Paper", "Scissors"] # creating the variables/choices 

# make the computer pcick one item at random 
computer_choice = choices[randint(0, 2)] #setting a variable 

# show the computers choice in the terminal window 
print("Comptuter chooses: ", computer_choice)
