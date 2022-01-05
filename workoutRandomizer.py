import csv
import time
import sys
import random
# Full Credit To Seamus Moore for the idea to use a naming convention in the premade csv files

def main():
    while True:
        print("\n********** Workout Randomizer **********")
        print("             by Evan Rafuse             \n")
        print("         Please Choose an Option:     ")
        print("       Option 1: Pre-made Workouts  ")
        print("       Option 2: Workout Randomizer ")
        print("       Option 3: Quit")
        choice = getInput()
        if choice == 1:
            preMade()
        elif choice == 2:
            rando()
        elif choice == 3:
            time.sleep(2)
            sys.exit("Shutting down...")
        else:
            print("Please choose one of the available options")
        

def preMade():
    print("         Please Choose an Option:     \n")
    print("      1: Arms     |      5: Shoulders")
    print("      2: Legs     |      6: Chest")
    print("      3: Abs      |      7: Hips")
    print("      4: Back     |      8: Full Body - Power")
    print("\n      9: Back to Top Menu")
    
    # Pull out correct workout file
    errorCheck = False
    while errorCheck == False:
        choice = getInput()
        if choice >= 1 and choice <= 8:
            # load option
            fileName = "workoutFiles/premade/" + str(choice) + ".csv"
            preMadePrinter(fileName)
            errorCheck = True
        elif choice == 9:
            break
        else:
            print("Please choose one of the available options")

def preMadePrinter(fileName):
        # Create the workout list and use rowNumb to find out how many workouts are in the list
        rowNumb = 0
        infile = open(fileName, "r")
        workoutsFile = csv.reader(infile)
        workoutList = []
        for row in workoutsFile:
            workoutList.append(row)
            rowNumb = rowNumb + 1
        workoutNumb = random.randint(0,len(workoutList))
        workout = workoutList[workoutNumb - 1]

        # Print the Workout
        exercise = 0
        for x in range(len(workout)):
            print("Exercise #" + str(exercise + 1) +": " + workout[exercise])
            exercise = int(exercise) + 1
        print("\n\n Please press enter to return to previous menu.")
        # Return to upper menu
        input()


def rando():
    print("\n\n")
    print("         You feelin' Lucky Punk?     ")
    print("         Please Choose an Option:     \n")
    print("Option 1: Randomize Upper Body Exercises")
    print("Option 2: Randomize Lower Body Exercises")
    print("Option 3: Randomize All Exercises")
    print("Option 4: Back to Top Menu \n\n")
    # Create the Workout List
    errorCheck = False
    while errorCheck == False:
        choice = getInput()
        if choice == 1 or choice == 2 or choice == 3:
            errorCheck = True
            keepGoing = True
            rowNumb = 0
            infile = open("workoutFiles/exerciseList.csv","r")
            workoutsFile = csv.reader(infile)
            workoutList = []
            for row in workoutsFile:
                workoutList.append(row)
                rowNumb = rowNumb + 1
        elif choice == 4:
            errorCheck = True
            keepGoing = False
        else:
            print("Please choose one of the available options")

    # I used this while loop to end the program from option 4, and give the option to stop at any time
    while keepGoing == True:
        # Create list as you go to make sure no repeats
        usedEx = []
        # Create a counter to display
        exNumb = 1
        # Set choice to be fully random on each pass
        if choice == 3:
            str(choice)
            choice = random.randint(0,1)
        else:
            pass
        while keepGoing == True:
            exercise = workoutList[choice][random.randint(0, len(workoutList[choice]))]
            if exercise in usedEx:
                pass
            else:
                usedEx.append(exercise)
                print("\n\n Exercise #" + str(exNumb) + ":  " + exercise + "\n\n")
                exNumb = int(exNumb) + 1
                print("           Still feelin' Lucky?     ")
                print("         Please Choose an Option:     \n")
                print("           Option 1: Another!")
                print("    Option 2: I'm too weak, I give up :(")
                choice2 = getInput()
                errorCheck = False
                while errorCheck == False:
                    if choice2 == 1:
                        print("MOAR\n")
                        errorCheck = True
                    elif choice2 == 2:
                        print("Pathetic!\n\n")
                        keepGoing = False
                        errorCheck = True
                    else:
                        print("Please choose one of the available options")

def getInput():
    errorCheck = False
    while errorCheck == False:
        choice = input(">")
        if choice.isdigit() == False:
            print("Please enter a digit to choose.")
        else:
            errorCheck = True
            return int(choice)

main()