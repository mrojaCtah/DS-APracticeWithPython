
class GallonFiller:

    # Potentially make newFourGalAmt global with first design
    # if so, find way  to make it not global
    
    def fillFourGalToSetAmt(self, fourGalAmt, threeGalAmt, fourGalFinalAmt):

        def fillFourGal():
            newFourGalAmt = 4
            return newFourGalAmt

        def emptyFourGal():
            newFourGalAmt = 0
            return newFourGalAmt

        def fillThreeGal():
            newThreeGalAmt = 3
            return newThreeGalAmt

        def emptyThreeGal():
            newThreeGalAmt = 0
            return newThreeGalAmt

        def fillThreeGalWithFourGal(threeGal, fourGal):
            
            if(fourGal == 0):
                if(threeGal == 0):
                    newThreeGalAmt = 0
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 1):
                    newThreeGalAmt = 1
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 2):
                    newThreeGalAmt = 2
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 3):
                    newThreeGalAmt = 3
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt

            if(fourGal == 1):
                if(threeGal == 0):
                    newThreeGalAmt = 1
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 1):
                    newThreeGalAmt = 2
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 2):
                    newThreeGalAmt = 3
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 3):
                    newThreeGalAmt = 3
                    newFourGalAmt = 1
                    return newThreeGalAmt, newFourGalAmt

            if(fourGal == 2):
                if(threeGal == 0):
                    newThreeGalAmt = 2
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 1):
                    newThreeGalAmt = 3
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 2):
                    newThreeGalAmt = 3
                    newFourGalAmt = 1
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 3):
                    newThreeGalAmt = 3
                    newFourGalAmt = 2
                    return newThreeGalAmt, newFourGalAmt

            if(fourGal == 3):
                if(threeGal == 0):
                    newThreeGalAmt = 3
                    newFourGalAmt = 0
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 1):
                    newThreeGalAmt = 3
                    newFourGalAmt = 1
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 2):
                    newThreeGalAmt = 3
                    newFourGalAmt = 2
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 3):
                    newThreeGalAmt = 3
                    newFourGalAmt = 3
                    return newThreeGalAmt, newFourGalAmt

            if(fourGal == 4):
                if(threeGal == 0):
                    newThreeGalAmt = 3
                    newFourGalAmt = 1
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 1):
                    newThreeGalAmt = 3
                    newFourGalAmt = 2
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 2):
                    newThreeGalAmt = 3
                    newFourGalAmt = 3
                    return newThreeGalAmt, newFourGalAmt
                if(threeGal == 3):
                    newThreeGalAmt = 3
                    newFourGalAmt = 4
                    return newThreeGalAmt, newFourGalAmt
                

            #print('check here: ' + str(newThreeGalAmt) + ' ' + str(newFourGalAmt)
            
        if(fourGalFinalAmt == 0):
            return True
        newFourGalAmtRecursive = fillFourGal()
        print('newFourGalAmt: ' + str(newFourGalAmtRecursive))
        print(fillThreeGalWithFourGal(threeGalAmt, newFourGalAmtRecursive))
        newThreeGalAmtRecursive, newFourGalAmtRecursive = fillThreeGalWithFourGal(threeGalAmt, newFourGalAmtRecursive)
        newThreeGalAmtRecursive = emptyThreeGal()
        print('newFourGalAmt: ' + str(newFourGalAmtRecursive))
        print('fourGalFinalAmt ' + str(fourGalFinalAmt))
        if(newFourGalAmtRecursive == fourGalFinalAmt):
            print('terminating condition')
            return True
        else:
            newThreeGalAmtRecursiveTwo, newFourGalAmtRecursiveTwo = fillThreeGalWithFourGal(newThreeGalAmtRecursive, newFourGalAmtRecursive)
            self.fillFourGalToSetAmt(newFourGalAmtRecursiveTwo, newThreeGalAmtRecursiveTwo, fourGalFinalAmt)
        

GallonFillerObject = GallonFiller()

GallonFillerObject.fillFourGalToSetAmt(2, 0, 4)
