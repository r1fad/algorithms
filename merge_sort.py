from helper_functions import genList

def merge_sort(array):

    if len(array) == 1:
        return array
    else:
        middle = len(array)//2

        leftArray = array[:middle]
        rightArray = array[middle:]

        merge_sort(leftArray)
        merge_sort(rightArray)

        i = 0
        j = 0
        k = 0

        while i<len(leftArray) and j<len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i = i + 1
            else:
                array[k] = rightArray[j]
                j = j + 1
            k = k + 1

        while i < len(leftArray):
            array[k] = leftArray[i]
            i+=1
            k+=1

        while j<len(rightArray):
            array[k] = rightArray[j]
            j+=1
            k+=1


aList = genList()
print aList
merge_sort(aList)
print aList
