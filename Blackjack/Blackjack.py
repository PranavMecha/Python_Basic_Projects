import random

cards = [11,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(user,computer):
    if len(user)<3:
        print("Your cards: ", user, "current score:", sum(user))
        print("Computer's First card : ",computer[0])
    maxm = sum(user)
    if maxm>21:
        if 11 in user:
            user.remove(11)
            user.append(1)
            maxm = sum(user)
        else:
            endgame(user,computer)
    if maxm==21:
        spotwin(user,computer)
    addon(user,computer)
def addon(user,computer):
    addon1 = input("Type 'y' to get another card, type 'n' to pass:")
    if addon1 == "y" :
        user.append(random.choice(cards))
        computer=compappend(computer)
        if sum(user)>21:   
            if 11 in user:
                user.remove(11)
                user.append(1)
            
        print("Your cards: ", user, "current score:", sum(user))
        print("Computer's First card : ", computer[0])
        blackjack(user, computer)
    if addon1=="n":
        computer=compappend(computer)
        print("Your final hand: ", user, " final score: ", sum(user))
        print("Computer's final hand: ", computer, " final score: ", sum(computer))
        diff1=21-sum(user)
        diff2=21-sum(computer)
        if diff1>=0 and diff2>=0:
            if diff1>diff2:
                print("You lose")
                gameon()
            elif diff1==diff2:
                print("Draw")
                gameon()
            else:
                print("You Win")
                gameon()
        else:
            print("Computer went over. You Win")
            gameon()

def endgame(user,computer):
    print("Your final hand: ",user , " final score: ",sum(user))
    print("Computer's final hand: ", computer, " final score: ", sum(computer))
    print("You went over. You lose")
    gameon()
def spotwin(user,computer):
    print("Your final hand: ", user, " final score: ", sum(user))
    print("Computer's final hand: ", computer, " final score: ", sum(computer))
    print("You got 21 that perfect score. You Won!!")
    gameon()
def compappend(computer):
    while sum(computer)<15 :
        computer.append(random.choice(cards))
    return computer
def gameon():
    user = []
    computer = []
    for i in range(0, 2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    game1="y"
    while game1=="y":
        game1=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if game1=="y":
            print(r""" 

            .------.            _     _            _    _            _    
            |A_  _ |.          | |   | |          | |  (_)          | |     
            |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
            | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
            |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < _
            `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\__|
                  |  \/ K|                            _/ |                
                  `------'                           |__/           

                """)
            blackjack(user,computer)
        else:
            print("Thanks ;)")


gameon()