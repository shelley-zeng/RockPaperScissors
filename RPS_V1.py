"""
Name:       General Knowledge Quiz
Purpose:    This is a quiz on general knowledge
Author:     Shelley Zeng
Created:     30.06.2021
"""

#List on statements 
STATEMENT_LIST = [
    "The colours on Germany's flag is black, red and yellow.",
    "Morocco is in North Africa.",
    "James Madison was the 3rd American President.",
    "Poseidon is the Greek god of the sea",
    "1 Direction dispanded in 2015",
    "the area of a triangle is A = bh",
    "The Nile river is the longest river on Earth.",
    "The Industrial Revolution started in the 1800's.",
    "NASA was founded in 1958.",
    "Snow White and The Seven Dwarfs was the first fully animated featured film to be released by Disney.",
    "The Storm on the Sea of Galilee was painted by Leonardo da Vinci."
]

#List for if statement is true or false
ANSWERS_LIST = ["t", "t", "f", "t", "f", "f", "t", "f", "t", "t", "f"] 
#This is a welcome message for the user when they first go on the game so they know what to do
print("""Hello! This is a true or false quiz on General Knowledge.\n 
There will be 10 randomly generated questions. \n
If you think the statement is true type "t".\n
If you think the statement is false type "f".\n
Let's begin! Good luck and have fun :)
""")

#prints statements from the statement list.
#not random and is numbered from 1-11\
# first trial

for index in range (len(STATEMENT_LIST)):
    print("{})\n{}".format(index+1, STATEMENT_LIST[index]))
