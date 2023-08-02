# Takes a text file and either formats the data or calculates the average of the numbers


# Main menu
def Main():
    print("D: Display grades ")
    print("C: Calculate average ")
    print("X: Exit Application ")

    userChoice = input("Pick an option: ")

    if userChoice == 'C' or userChoice == 'c':
        # Hold return value of CalculateAverage here and display to screen
        avgScore = CalculateAverage()
        print("The average is: " + str(avgScore))
        Main()
    elif userChoice == 'D' or userChoice == 'd':
        DisplayScores()
        Main()
    elif userChoice == 'X' or userChoice == 'x':
        print("Exiting application")

def DisplayScores():
    fileToOpen = input('Which file would you like to open?: ')
    # Keep track of the current line
    count = 0
    # Will contain the desired user text file
    scores = ''

    try:
        scores = open(fileToOpen)
    except:
        print("The file you are looking does not exist. Returning to main menu.")
        Main()

    for num in scores:
        # Remove \n from each line, so they aren't double spaced
        num = num.rstrip('\n')
        count += 1
        print(str(count) + ': ' + num)

def CalculateAverage():
    fileToOpen = input('Which file would you like to open?: ')
    count = 0
    # Add up all the numbers in the file and store here
    total = 0.0
    scores = ''

    try:
        scores = open(fileToOpen)
    except:
        print("The file you are looking does not exist. Returning to main menu.")
        Main()

    for num in scores:
        #num = num.rstrip('\n')
        # convert each num to a float before adding to total
        num = float(num)
        total = total + num
        count += 1
    # contains the average of all the numbers
    average = round((total/count), 2)

    return average

Main()









