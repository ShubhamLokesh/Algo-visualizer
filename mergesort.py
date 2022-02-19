import time
colorArray=[]
swapCount = 0

##---to reset swap count
def mergeSort(arr,displayArray,stepTime,start,end): 
    global colorArray
    colorArray=['black' for x in range(len(arr))]
    merge_sort(arr,displayArray,stepTime,start,end)
    colorArray=['green' for x in range(len(arr))]
    displayArray(arr,colorArray,swapCount)
    print("Sorted arr : ",arr)

# divides the array recursively into two parts then sorts
def merge_sort(arr,displayArray,stepTime,start,end):
    if start<end:
        mid = (start+end) // 2
        merge_sort(arr,displayArray,stepTime,start,mid)
        merge_sort(arr,displayArray,stepTime,mid+1,end)
        merge(arr,displayArray,stepTime,start,mid,end)
    print(" arr : ",arr)

def merge(arr,displayArray,stepTime,start,mid,end): 
    global swapCount

    #--highlight the left and the right parts of the array
    colorArray = []
    for i in range(len(arr)):
        if i>=start and i<=mid:
            colorArray.append('black')
        elif i>=mid+1 and i<=end:
            colorArray.append('black')
        else:
            colorArray.append('black')

    displayArray(arr,colorArray,swapCount)
    time.sleep(stepTime)

    arrL = arr[start:mid+1]
    arrR = arr[mid+1:end+1]

    i, j, k = 0, 0,start # i->arrL;   j->arrR;   k->arr

    while (i < len(arrL) and j < len(arrR)):
        colorArray[i]=colorArray[j]='white'
        displayArray(arr, colorArray, swapCount)
        time.sleep(stepTime)
        
        if arrL[i] < arrR[j]:
            arr[k] = arrL[i]
            swapCount+=1
            i+=1
            for x in range(start,k):
                colorArray[x] = 'blue'
            displayArray(arr, colorArray, swapCount)
            time.sleep(stepTime)
        else:
            arr[k] = arrR[j]
            swapCount+=1
            j+=1
            for x in range(start,k):
                colorArray[x] = 'blue'
            displayArray(arr, colorArray, swapCount)
            time.sleep(stepTime)

        k+=1

    while i<len(arrL):
        arr[k] = arrL[i]
        i += 1
        k += 1
        swapCount+=1
        for x in range(start, k ):
            colorArray[x] = 'white'
        displayArray(arr, colorArray, swapCount)
        time.sleep(stepTime)

    while j<len(arrR):
        arr[k] = arrR[j]
        j += 1
        k += 1
        swapCount+=1
        for x in range(start, k ):
            colorArray[x] = 'white'
        displayArray(arr, colorArray, swapCount)
        time.sleep(stepTime)

    