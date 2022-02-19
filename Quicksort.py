from time import sleep
colorarr=[]
swapcount=0
def QuickSort(arr, displayArray,stepTime):
    global colorarr
    global swapcount
    swapcount=0
    colorarr=['black' for x in range(len(arr))]
    quickSort(arr,0,len(arr)-1,displayArray,stepTime)
    colorarr=['green' for x in range(len(arr))]
    displayArray(arr,colorarr,swapcount)

def quickSort(arr,start,end,displayArray,stepTime):
    if start>=end:
        return
    
    pivot=partition(arr,start,end,displayArray,stepTime)
    quickSort(arr,start,pivot-1,displayArray,stepTime)
    quickSort(arr,pivot+1,end,displayArray,stepTime)

def partition(arr,start,end,displayArray,stepTime):
    global swapcount
    global colorarr
    i=start-1
    pivot=arr[end]
    for x in range(start,end):
        colorarr[x]='white'
    for j in range(start,end):
        colorarr[j]=colorarr[end]='blue'
        displayArray(arr,colorarr,swapcount)
        sleep(stepTime)
        colorarr[j]=colorarr[end]='black'
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            swapcount+=1

    arr[i+1],arr[end]=arr[end],arr[i+1]
    colorarr[i+1]='Green'
    displayArray(arr,colorarr,swapcount)
    sleep(stepTime)
    swapcount+=1
    return i+1
