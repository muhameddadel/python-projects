class Game:
    ##############################################################
    # Constructor Fucntion
    def __init__(self):
        print("Welcome In The Full Game....")
        print("Choose Your Game From Our Colloction")
        print("[1]: Will Play Even-Odd Game")
        print("[2]: Will Play Sum Avrage Game")
        print("[3]: Will Play Multiplication Game")
        self.Choices()
    ######################################################
    # Avilable Choices
    def Choices(self):
        user_choice = input("Enter Your Choice: ")
        
        try:
            user_choice = int(user_choice)
            if user_choice == 1:
                self.Even_Odd_Game()
            elif user_choice == 2:
                self.Sum_Ave_Game()
            elif user_choice == 3:
                self.Mul_Game()
            else:
                print("Invalid Game")
        except ValueError:
            print("Please Enter A Valid Number")
    ##########################################################
    # Even_Odd_Game 
    def Even_Odd_Game(self):
        print("Welcome In the Even Odd Game")
        print("Please Enter A Number ... And I Will If It Even Or Odd")
        print("If You Want To Close The Game Enter x")
        while True:
            num = input("Enter A Number: ")
            if num == "x":
                print("Close The Game")
                print("Thanks...")
                break
            try:
                num = int(num)
                if num % 2 == 0:
                    print("Even Number")
                else: 
                    print("Odd Number")
            except ValueError:
                print("Please Enter A Valied Number")
            print("------------------------------------")
    ###################################################################
    # Sum_Ave_Game
    def Sum_Ave_Game(self):
        print("This Game Will Take Several Number And Print Average")
        count = int(input("How Many Number Would You Like To Sum: "))
        crr = 0
        summ = 0
        while crr < count:
            num = float(input("Enter the Number: "))
            summ += num
            crr += 1
        print(summ)
    ############################################################
    # Mul_Game
    def Mul_Game(self):
        start = int(input("Enter the first number: "))
        end = int(input("Enter the last number: "))
        for x in range(start,end+1):
            for y in range(1, 13):
                print(f"{x} * {y} = {x * y}")
            print("-------------------------")

game_one = Game()