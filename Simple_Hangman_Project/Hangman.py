import random
import diagram
import Words
select_word=random.choice(Words.list1)
blank=""
for i in range(0,len(select_word)):
    blank+="_"
print("Your word is :",blank)

game= False
points=6
correct_one=[]
while(game==False):
    display=""
    guess=input("Enter your guess:").lower()
    for letter in select_word:
        if letter == guess:
            display+=letter
            correct_one.append(guess)
        elif letter in correct_one:
            display+=letter
        else:
            display+="_"
    
    print("Your word is :",display)
    
    if guess not in select_word:
        points-=1
    diagram.diagram(points)
    if points==0:
        print("You Lose")
        game=True
    if display==select_word:
        print("You won")
        game=True