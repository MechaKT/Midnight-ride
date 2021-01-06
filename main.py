# main.py
# midnight rider
# A text adventure game that is riveting
# IGN gives it 4 stars out of 100.

import random
import textwrap
import sys
import time

INTRODUCTION = """

WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THE GOVERNMENT WANTS IT FOR THEIR GAIN.

WE CAN'T LET THAT HAPPEN.

ONE GOAL: SURVIVAL... and THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.

"""

WIN = """

You pressed the button to open the gate.
This isn't the first time you've done this,
so you know how to time it exactly.
Just as the doors close, you slide right into HQ.
You know you did the right thing, the government would have just torn the car apart.
They don't know its secrets...
that it holds the key to different worlds.
As you step out of the vehicle, Fido runs up to you.
"Thank you for saving me," he says.
As you take a couple of steps away from the car,
it makes a strange sound.
It changes its shape.
You've seen it before, but only on TV.
"...Bumblebee???"



------ Game Over ------
"""

CHOICES = """
    ----
    A. Chompers
    B. Drive at moderate speed
    C. Speed ahead full throttle
    D. Stop for fuel at a refuelling station.
    (No food available)
    E. Status check
    Q. QUIT
    ----
"""
def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL = 50
    MAX_TOFU = 3
    MAX_DISTANCE_TRAVELED = 100
    # Variables
    done = False
    km_traveled = 99         # 100km is the goal
    agents_distance = -20.0
    turns = 0               # amount of turns taken
    tofu = MAX_TOFU
    fuel = MAX_FUEL
    hunger = 0              # hunger increases with num


    while not done:
        # TODO: Random events
        # Fido
        if random.random() < 0.03:
            # Fido pops up says something and refills tofu
            tofu = MAX_TOFU
            print()
            print("******** Your tofu is magically refilled! ")
            print("******** \"You're welcome!\" a voice says.")
            print("******** It's Fido.")
            print("******** He's using his tofu cooking skills.")

        if hunger > 35:
            print("******** Your stomach rumbles. You need to eat something soon.")
        elif hunger > 20:
            print("******** Your hunger is small but manageable.")
        # Check if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELED:
            # WIN
            # Print win scenario (typing way)
            time.sleep(2)
            type_text_output(WIN)
            # Break from while loop
            break
        # TODO: Complete hunger ending
        elif hunger > 45:
            # LOSER - TOO HUNGRY
            # Print losing scenario
            break
        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")
        if users_choice == "a":
            # Eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmmm. Soybean goodness.")
                print("-------- Your hunger is sated.")
            else:
                print()
                print("-------- You have none left.")
                print()
        elif users_choice == "b":
            player_distance_now = random.randrange(7, 15)
            agents_distance_now = random.randrange(7, 15)
            fuel -= random.randrange(2, 7)

            km_traveled += player_distance_now
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()
            agents_distance -= (player_distance_now - agents_distance_now)
        elif users_choice == "c":
            # Drive Fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)
            # Burn fuel
            fuel -= random.randrange(5,11)

            # Player distance traveled
            km_traveled += player_distance_now
            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)
            # Player feedback
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()
        elif users_choice == "d":
            # Refuel
            fuel = MAX_FUEL
            # Fill the fuel tank
            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)
            # Give the user feedback
            print("--------- You refilled your tank.")
            print("--------- The agents got closer.")
        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm traveled: {km_traveled} kms")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind you.")
            print(f"\tYou have {tofu} tofu left.")
            print("\t------\n")
        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5,13)
        time.sleep(1)

    # Outroduction
    print("Thanks for playing! Please play again. =)")
if __name__ == '__main__':
    main()
