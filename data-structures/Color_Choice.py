import random

print("Welcome to Color Choice Game \n"
      "Let's compare Computer and You !! \n")

player1 = 0
player2 = 0

print("Below are Colors with values : \n"
      " 1. Red \n"
      " 2. Yellow \n"
      " 3. Green \n"
      " 4. Blue \n"
      " 5. Black \n"
      " Quit : any other value \n")

while True:
    choice1 = str(input("\nEnter Your Color Choice : "))
    choice2 = random.randint(1,5)
    match choice1.lower():
        case 'red' | '1':
            choice1 = 1
        case 'yellow' | '2':
            choice1 = 2
        case 'green' | '3':
            choice1 = 3
        case 'blue' | '4':
            choice1 = 4
        case 'black' | '5':
            choice1 = 5
        case default:
            if player1 == player2 :
                print("\nMatch Tied")
            elif player1 > player2 :
                print("\nCongratulations You won !")
            else:
                print("\nComputer Won !")
            break

    print(f"computer choice is {choice2}")
    if choice1 > choice2 :
        player1 += 1
        print("you won this round !")
    elif choice1 < choice2:
        player2 += 1
        print("computer won this round !")
    else:
        print("same values for both")

    print(f"Values of player1 and player2 are {player1} and {player2}\n")

print("Thank you for playing !")









