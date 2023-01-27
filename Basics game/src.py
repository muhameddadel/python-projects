print("Welcome to my fundamental game..!")
name = input('What is your name: ').capitalize()
age = int(input('What is your age: '))
print(f'Hello {name} your age is {age} years old..')

health = 10

if age >= 18:
    print('You are old enough to play ^_^')

    wants_to_play = input('Do you want to play: ').lower()
    if wants_to_play == 'yes':
        print("Let's paly ^_^")

        left_or_right = input("Left or Right: ")
        if left_or_right == "left":
            answer = input("Nice, do you swin across or go around: ").lower()

            if answer == "around":
                print("Well done!!, you reached the other side of lake safly..")

            elif answer == "across":
                print("You go across the lake, but you lost 5 health..")
                health -= 5

                answer = input("You notice a house and river, which do you go to: ").lower()

                if answer == 'house':
                    print("You reach the house but his owner don't like.. you lost a 5 health")
                    health -= 5
                    if health <= 0:
                        print("Game Over -_-")
                    else:
                        print('You survived..')
                else:
                    print("You fell in the lake and die......")

        else:
            print("You lost, you can try again..")
    else:
        print("Good bye..")
else:
    print('You are not old enough to play..')
    