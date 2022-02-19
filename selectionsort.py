from time import sleep
colorArray=[]

def selectionSort(arr, displayArray,stepTime):
    swapCount=0
    colorArray=['black' for x in range(len(arr))]
    for i in range(len(arr)):
        min=arr[i]
        min_index=i
        colorArray[i]='blue'
        for j in range(i+1,len(arr)):
            colorArray[j]='white'
            displayArray(arr,colorArray,swapCount)
            colorArray[j]='black'
            sleep(stepTime)
            if arr[j]<min:
                colorArray[min_index]='black'
                min=arr[j]
                min_index=j
                swapCount+=1
                colorArray[j]='blue'
                if j!=len(arr)-1:
                    colorArray[j+1]='white'
                displayArray(arr,colorArray,swapCount)
                colorArray[j]='blue'
                sleep(stepTime)
        arr[min_index],arr[i]=arr[i],arr[min_index]
        swapCount+=1
        colorArray[i+1:]=['black' for x in range(i+1,len(arr))]
        colorArray[i]='green'
        displayArray(arr,colorArray,swapCount)
        sleep(stepTime)