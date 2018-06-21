import csv
import sys


file = sys.argv[1]
velocity = int(sys.argv[2])
taskIDs = []
storyPoints = []
KPSs = []
listOfTasks = [ ]
ratio = []

def CreatingLists():
    """ This function creates the lists for each column, ignoring the header"""
    with open('task.csv') as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')
        header = next(readCSV)
        for row in readCSV:
            taskIDs.append(int(row[0]))
            storyPoints.append(int(row[1]))
            KPSs.append(int(row[2]))
            ratio.append(int(row[2])/int(row[1]))
    return taskIDs, storyPoints, KPSs, ratio


def CreatingListOFTasks():
    """ This function creates the list of tasks that were choosen for sprint"""
    velocityCounter = 0
    for x in range(len(ratio)):
        index = ratio.index(float(max(ratio)))
        maxSP = int(storyPoints[index])
        velocityCounter += maxSP
        if velocityCounter <=  velocity:
            listOfTasks.append(taskIDs[index])
            del KPSs[index],storyPoints[index],taskIDs[index],ratio[index]
        else:
            break
    return listOfTasks

def PrintingListOfTasks():
    """ This function prints the list of tasks that were choosen for sprint"""
    listOfTasks.sort();
    print(listOfTasks)

CreatingLists()
CreatingListOFTasks()
PrintingListOfTasks()
