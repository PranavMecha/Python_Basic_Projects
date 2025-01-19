import game_data
import random
import art

c=len(game_data.data)
n=0
a = random.randint(0, c-1)
def game_on(a):
    print(art.logo)
    print("\n")
    score = 0
    while True:
        print("Compare A :")
        print(game_data.data[a]['name'], ", a", game_data.data[a]['description'], ", from", game_data.data[a]['country'])
        print(art.vs)
        b = random.randint(0, c - 1)
        print("With B :")
        print(game_data.data[b]['name'], ", a", game_data.data[b]['description'], ", from", game_data.data[b]['country'])
        follow=input("Who has more followers? Type 'A' or 'B': ").lower()
        if follow=="a" and (game_data.data[a]['follower_count']>game_data.data[b]['follower_count']):
            
            score+=1
            print(f"You're right! Current score: {score}")
            a=b

        elif follow == "b" and (game_data.data[a]['follower_count'] < game_data.data[b]['follower_count']):
            N
            score += 1
            print(f"You're right! Current score: {score}")
            a = b

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            again=input("Do You Want To Play again ?? (Y/N) :").lower()
            if again=="y":
                
                a = random.randint(0, c - 1)
                game_on(a)
                
            else:
                print("Thanks for Playing")
                break



game_on(a)