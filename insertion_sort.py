from helper_functions import genList

def insSort(aList):

    n = len(aList)

    '''assume that list[0:key-1] is sorted and insert
    list[key] in to list[0:key-1] at the right position
    using pair wise swaps'''

    for key in range(1,n):
        currentElement = aList[key]
        position = key

        while position>0 and aList[position-1]>currentElement:
            aList[position] = aList[position-1]
            position -= 1
            #print aList
        #print "_________________________"
        aList[position] = currentElement
        #print aList
        #print "-----------------------------------------"

aList = genList()
print aList
insSort(aList)
print aList
