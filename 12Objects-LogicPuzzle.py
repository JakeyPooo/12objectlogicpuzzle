#Author: Jacob Anderson
#Date: 29 March 2023
#Description: Logic puzzle finding the object that is either heavier or lighter in 3 moves.
#Status: LOGIC IS GOOD! I'd like to have it iterate 100 times and save to a .csv so I can see data in one sheet and then confirm that it's logically sound. DONE
#        Need to start adding graphics since the logic is done too. Need to rename all variables and groups to be generic to follow GUI

import numpy as np
import random as r
import csv

def groupWeight(*x):
    return sum(x)

with open('12Objects-LogicPuzzle.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Iteration", "Odd Object", "Weight", "All Objects", "", "TEST"])
    for h in range(1, 10001):

        print("You are given 12 objects, one of the objects is either heavier or lighter than the rest.")
        print("You have 3 uses of a fair scale to determine the one object that is heavier or lighter.")
        print("How do you determine the one object and it's weight?")
        print("The objects are labelled 1 to 12.")

        theObjects = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

        flag = 0
        while flag < 1:
            theObjects[r.randrange(0, 12)] = r.randrange(1, 4)
            for i in range(0,12):
                if(theObjects[i] != 2):
                    flag = 1

        print("\nFirst step: divide objects into 3 even groups: A, B, C.")
        groupA = np.array([theObjects[0], theObjects[1], theObjects[2], theObjects[3]])
        groupB = np.array([theObjects[4], theObjects[5], theObjects[6], theObjects[7]])
        groupC = np.array([theObjects[8], theObjects[9], theObjects[10], theObjects[11]])

        weightA = groupWeight(*groupA)
        weightB = groupWeight(*groupB)
        weightC = groupWeight(*groupC)

        #starting comparison here
        print("Then compare group A to group B.\n")
        #CASE 1:
        if(weightA == weightB):
            print("Group A is equal to group B in weight.")
            print("Now compare any three from group A or B to the first three in group C")
            C1g1 = np.array([groupA[0], groupA[1], groupA[2]])
            C1g2 = np.array([groupC[0], groupC[1], groupC[2]])
            weightG1 = groupWeight(*C1g1)
            weightG2 = groupWeight(*C1g2)
            #CASE 1.1:
            if(weightG1 == weightG2):
                print("The scale is level.")
                print("Since the scale is level, object 12 is the odd one out.")
                print("Now determine the weight of 12.")
                if(groupC[3] > groupA[0]):
                    print("\n12 is heavier than 1.")
                    print("Therefore, the odd object is 12 and it is heavier.")
                    oddObject = 12
                    oddObjectWeight = 'Heavier'
                else:
                    print("\n12 is lighter than 1.")
                    print("Therefore, the odd object is 12 and it is lighter.")
                    oddObject = 12
                    oddObjectWeight = 'Lighter'
            #CASE 1.2:
            elif(weightG1 < weightG2):
                print("\nThe scale is leaning toward the group of three of C.")
                print("That means that either 9, 10, or 11 is heavier.")
                print("Now compare 9 against 10")
                if(C1g2[0] == C1g2[1]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 11 and it is heavier.")
                    oddObject = 11
                    oddObjectWeight = 'Heavier'
                elif(C1g2[0] < C1g2[1]):
                    print("\nThe scale is leaning toward 10.")
                    print("Therefore, the odd object is 10 and it is heavier.")
                    oddObject = 10
                    oddObjectWeight = 'Heavier'
                else:
                    print("\nThe scale is leaning toward 9.")
                    print("Therefore, the odd object is 9 and it is heavier.")
                    oddObject = 9
                    oddObjectWeight = 'Heavier'
            #CASE 1.3:
            elif(weightG1 > weightG2):
                print("\nThe scale is leaning toward the group of three of A.")
                print("That means that either 9, 10, or 11 is lighter.")
                print("Now compare 9 against 10.")
                if(C1g2[0] == C1g2[1]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 11 and it is lighter.")
                    oddObject = 11
                    oddObjectWeight = 'Lighter'
                elif(C1g2[0] > C1g2[1]):
                    print("\nThe scale is leaning toward 9.")
                    print("Therefore, the odd object is 10 and it is lighter.")
                    oddObject = 10
                    oddObjectWeight = 'Lighter'
                else:
                    print("\nThe scale is leaning toward 10.")
                    print("Therefore, the odd object is 9 and it is lighter.")
                    oddObject = 9
                    oddObjectWeight = 'Lighter'
                
        #CASE 2:
        if(weightA > weightB):
            print("\nGroup A is weighing less than group B")
            print("Therefore, group C is good, but the odd object is still unknown.")
            print("Split group A and B into two different groups: g1(1, 5, 6) & g2(9, 7, 8)")
            C2g1 = np.array([groupA[0], groupB[0], groupB[1]])
            C2g2 = np.array([groupC[0], groupB[2], groupB[3]])
            weightG1 = groupWeight(*C2g1)
            weightG2 = groupWeight(*C2g2)
            #CASE 2.1:
            if(weightG1 == weightG2):
                print("\nThe scale is level.")
                print("Since the scale is level, the odd object is 2, 3, or 4.")
                print("Now compare 2 against 3.")
                if(groupA[1] == groupA[2]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 4 and it is heavier.")
                    oddObject = 4
                    oddObjectWeight = 'Heavier'
                elif(groupA[1] > groupA[3]):
                    print("\nThe scale is leaning toward 2.")
                    print("Therefore, the odd object is 2 and it is heavier.")
                    oddObject = 2
                    oddObjectWeight = 'Heavier'
                else:
                    print("\nThe scale is leaning toward 3.")
                    print("Therfore, the odd object is 3 and it is heavier.")
                    oddObject = 3
                    oddObjectWeight = 'Heavier'
            #CASE 2.2:
            elif(weightG1 > weightG2):
                print("\nThe scale is leaning toward group 1.")
                print("That means that 1 is heavier or 7 or 8 is lighter.")
                print("Now compare 7 against 8.")
                if(groupB[2] == groupB[3]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 1 and it is heavier.")
                    oddObject = 1
                    oddObjectWeight = 'Heavier'
                elif(groupB[2] > groupB[3]):
                    print("\nThe scale is leaning toward 7.")
                    print("Therefore, the odd object is 8 and it is lighter.")
                    oddObject = 8
                    oddObjectWeight = 'Lighter'
                else:
                    print("\nThe scale is leaning toward 8.")
                    print("Therefore, the odd object is 7 and it is lighter.")
                    oddObject = 7
                    oddObjectWeight = 'Lighter'
            #CASE 2.3:
            elif(weightG1 < weightG2):
                print("\nThe scale is leaning toward group 2.")
                print("That means that 1, 5, or 6 is lighter.")
                print("Now compare 5 against 6.")
                if(groupB[0] == groupB[1]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 1 and it is lighter.")
                    oddObject = 1
                    oddObjectWeight = 'Lighter'
                elif(groupB[0] > groupB[1]):
                    print("\nThe scale is leaning toward 5.")
                    print("Therefore, the odd object is 6 and it is lighter.")
                    oddObject = 6
                    oddObjectWeight = 'Lighter'
                else:
                    print("\nThe scale is leaning toward 6.")
                    print("Therefore, the odd object is 5 and it is lighter.")
                    oddObject = 5
                    oddObjectWeight = 'Lighter'

        #CASE 3:
        if(weightA < weightB):
            #print("%s > %s" % (weightA, weightB))     #TEST: Verify the weight difference between groups
            print("\nGroup A is weighing more than group B")
            print("Therefore, group C is good, but the odd object is still unknown.")
            print("Split group A and B into two different groups: g1(5, 1, 2) & g2(9, 3, 4)")
            C3g1 = np.array([groupB[0], groupA[0], groupA[1]])
            C3g2 = np.array([groupC[0], groupA[2], groupA[3]])
            weightG1 = groupWeight(*C3g1)
            weightG2 = groupWeight(*C3g2)
            #CASE 3.1:
            if(weightG1 == weightG2):
                print("\nThe scale is level.")
                print("Since the scale is level, the odd object is 6, 7, or 8.")
                print("Now compare 6 against 7.")
                if(groupB[1] == groupB[2]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 8 and it is heavier.")
                    oddObject = 8
                    oddObjectWeight = 'Heavier'
                elif(groupB[1] > groupB[3]):
                    print("\nThe scale is leaning toward 6.")
                    print("Therefore, the odd object is 6 and it is heavier.")
                    oddObject = 6
                    oddObjectWeight = 'Heavier'
                else:
                    print("\nThe scale is leaning toward 7.")
                    print("Therfore, the odd object is 7 and it is heavier.")
                    oddObject = 7
                    oddObjectWeight = 'Heavier'
            #CASE 3.2:
            elif(weightG1 > weightG2):
                print("\nThe scale is leaning toward group 1.")
                print("That means that 5 is heavier or 3 or 4 is lighter.")
                print("Now compare 3 against 4.")
                if(groupA[2] == groupA[3]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 5 and it is heavier.")
                    oddObject = 5
                    oddObjectWeight = 'Heavier'
                elif(groupA[2] > groupA[3]):
                    print("\nThe scale is leaning toward 3.")
                    print("Therefore, the odd object is 4 and it is lighter.")
                    oddObject = 4
                    oddObjectWeight = 'Lighter'
                else:
                    print("\nThe scale is leaning toward 4.")
                    print("Therefore, the odd object is 3 and it is lighter.")
                    oddObject = 3
                    oddObjectWeight = 'Lighter'
            #CASE 3.3:
            elif(weightG1 < weightG2):
                print("\nThe scale is leaning toward group 2.")
                print("That means that 5, 1, or 2 is lighter.")
                print("Now compare 1 against 2.")
                if(groupA[0] == groupA[1]):
                    print("\nThe scale is level.")
                    print("Therefore, the odd object is 5 and it is lighter.")
                    oddObject = 5
                    oddObjectWeight = 'Lighter'
                elif(groupA[0] > groupA[1]):
                    print("\nThe scale is leaning toward 1.")
                    print("Therefore, the odd object is 2 and it is lighter.")
                    oddObject = 2
                    oddObjectWeight = 'Lighter'
                else:
                    print("\nThe scale is leaning toward 2.")
                    print("Therefore, the odd object is 1 and it is lighter.")
                    oddObject = 1
                    oddObjectWeight = 'Lighter'

        if(theObjects[oddObject - 1] == 1):
            TEST = 'PASS'
        elif(theObjects[oddObject - 1] == 3):
            TEST = 'PASS'
        else:
            TEST = 'FAIL'

        writer.writerow([h, oddObject, oddObjectWeight, theObjects, '', TEST])