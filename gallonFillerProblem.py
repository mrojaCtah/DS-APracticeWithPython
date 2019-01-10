# gallon filler problem
# given one four gallon jug, and one three gallon jug
# with no markings on either, fill the four gallon jug with
# exactly two gallons, recursively

def gallonFiller(fourGalAmt, threeGalAmt):

    # base case
    if(fourGalAmt == 2):
        print("terminating condition")
        return True

    if(fourGalAmt == 0 and threeGalAmt == 0):
        # fill 4 gallon with hose, empty 4 gallon into three gallon
        newFourGalAmt = 4
        newThreeGalAmt = 3
        newFourGalAmt = 1
        print("first condition")
    elif(fourGalAmt == 0):
        # fill 4 gallon, empty into 3 gallon
        # 4 gallon now filled with exactly two gallons
        # return true next recursion
        newFourGalAmt = 4
        newThreeGalAmt = 3
        newFourGalAmt = 2
        print("condition 1 line above terminating condition")

    if(fourGalAmt == 1):
        # fill 3 gallon with remainder of 4 gallon
        newThreeGalAmt = 1
        newFourGalAmt = 0
        print("second condition")

    gallonFiller(newFourGalAmt, newThreeGalAmt)

gallonFiller(0, 0)
