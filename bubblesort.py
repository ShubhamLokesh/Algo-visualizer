from time import sleep
colorArray=[]

def bubbleSort(arr,displayArray,stepTime):
    swapcount=0
    colorArray=['black' for x in range(len(arr))]
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            colorArray[j]=colorArray[j+1]='white'
            displayArray(arr,colorArray,swapcount)
            colorArray[j]=colorArray[j+1]='black'
            sleep(stepTime)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapcount+=1
                colorArray[j]=colorArray[j+1]='red'
                displayArray(arr,colorArray,swapcount)
                colorArray[j]=colorArray[j+1]='black'
                sleep(stepTime)
        colorArray[len(arr)-1-i]='green'
        displayArray(arr,colorArray,swapcount)
    colorArray[0]='green'
    displayArray(arr,colorArray,swapcount)