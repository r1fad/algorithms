from helper_functions import genList

#log n complexity
def findPeak(aList):
    print aList

    length = len(aList)

    midIndex = length/2

    #if mid position less than element to its left look at left
    #half of list
    if aList[midIndex] < aList[midIndex-1]:
        findPeak(aList[:midIndex-1])

    #if mid positon less than element to its right look at right
    #half of list
    elif aList[midIndex] < aList[midIndex+1]:
        findPeak(aList[midIndex+1:])

    #else mid position is the peak
    else:
        return aList[midIndex]

aList = genList()
print findPeak(aList)
