#import random and time to use them later
import random
import time
#welcome player
username = input("Enter username:")
print("Welcome to Adventure Game!, " + username)
#function of intro
def intro():
    print("!")
    time.sleep(2)
    print("You are in an open field.")
    time.sleep(2)
    print("You see a cave (1) and a house (2) in front of you.")
    time.sleep(2)
#defining for process of choose
def choose_path():
    while True:
        choice = input("Do you want to enter the cave (1) or the house (2)? Enter 1 or 2: ")
        time.sleep(2)
#if condition of choices
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please type 1 for cave or 2 for house.")
#defining for cave
def cave(score, has_magic_stick):
    print("\nYou enter the cave...")
    time.sleep(2)

    if not has_magic_stick:
        print("You find a magic stick!")
        time.sleep(2)

        has_magic_stick = True
        score += 100
        print("Your score increased! Current score:", score)
        time.sleep(2)

    else:
        print("The cave is empty. You've already taken the magic stick.")
        time.sleep(2)

    return score, has_magic_stick
#defining for house
def house(score, has_magic_stick):
    monsters = ["monster", "dinosaur", "lion"]
    current_monster = random.choice(monsters)
    print("\nYou enter the house...")
    time.sleep(2)

    print(f"A {current_monster} appears!")
    time.sleep(2)
#if condition for magic stick 
    if has_magic_stick:
        print(f"You use the magic stick to defeat the {current_monster}. You WIN!")
        time.sleep(2)

        win = True
    else:
        print(f"You have no magic stick. The {current_monster} defeats you. You LOSE!")
        time.sleep(2)

        win = False
    return win

def show_result(win, score):
    print("\n--- Game Over ---")
    if win:
        print("Result: WIN")
        time.sleep(2)

    else:
        print("Result: LOSE")
        time.sleep(2)

    print("Your final score is:", score)

def main():
    while True:
        score = 0
        has_magic_stick = False

        intro()
        while True:
            path = choose_path()
            if path == '1':
                score, has_magic_stick = cave(score, has_magic_stick)
                # After cave, go back to choice
            else:
                win = house(score, has_magic_stick)
                break  # Game ends after entering the house

        show_result(win, score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
#Thanks for watching my project , i wish you like it