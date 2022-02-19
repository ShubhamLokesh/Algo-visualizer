from time import sleep
def LinearSearch(arr, displayArray,search_element,stepTime):
    colorarr=['black'for i in range (len(arr))]
    for i in range(len(arr)):
        colorarr[i]='white'
        displayArray(arr,colorarr)
        sleep(stepTime)
        if arr[i]==search_element:
            colorarr[i]='green'
            displayArray(arr,colorarr)
            sleep(stepTime)
            return i
        else:
            colorarr[i]='red'
            displayArray(arr,colorarr)
            sleep(stepTime)
