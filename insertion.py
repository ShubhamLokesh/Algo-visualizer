import time


def InsertionSort(arr, displayArray,stepTime):
    swapCount = 0
    colorArray=['black' for x in range(len(arr))]
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        colorArray[i]='blue'
        displayArray(arr,colorArray,swapCount)
        time.sleep(stepTime)
        
        while j>=0 and arr[j]>key:

            colorArray[j]='white'
            displayArray(arr,colorArray,swapCount)
            time.sleep(stepTime)
            colorArray[j]='black'
            arr[j+1]=arr[j]
            j-=1
            swapCount +=1
        arr[j+1]=key

        colorArray[j+1]='red'
        displayArray(arr,colorArray,swapCount)
        time.sleep(stepTime)
        colorArray[j+1]='black'
        colorArray[i]='black'

    colorArray=['green' for x in range(len(arr))]
    displayArray(arr,colorArray,swapCount)