
import os

scores = []

# Helper functions
def saveData():
    file = open("scores.dat", "w")
    str_scores = []
    for score in scores:
        str_scores.append(str(score))

    filedata = "\n".join(str_scores)
    file.write(filedata)
    file.close()

def loadData():
    file = open("scores.dat", "r")
    filedata = file.read().strip()
    file.close()

    str_scores = filedata.split("\n")
    if len(str_scores) > 0 and str_scores[0] == "":
        str_scores.pop(0)

    for str_score in str_scores:
        scores.append(float(str_score))


def displayMenuAndGetUserOption():
    print("===================================")
    print("Select your choice: ")
    print()
    print(" 1) Add a score")
    print(" 2) Calculate average")
    print()
    selected = input("Enter an option: ")
    print("===================================")
    return selected

def calculateAverage():
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores)
    print("The following scores")
    print(scores)
    print("average to")
    print(avg)

def getScoreFromUser():
    x = input("Enter a score between 0.0 and 100.0: ")
    x = float(x)
    scores.append(x)


# Main Program
if os.path.exists("scores.dat"):
    loadData()
else:
    saveData()


while True:
    selected = displayMenuAndGetUserOption()

    if selected == "1":
        getScoreFromUser()
        saveData()

    elif selected == "2":
        calculateAverage()
        break



print("Program done.")
