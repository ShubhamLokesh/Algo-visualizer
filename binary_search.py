from time import sleep
colorarr=[]

def startBinarySearch(arr, displayArray,search_element,stepTime):
    arr=sorted(arr)
    colorarr=['black' for x in range(len(arr))] 
    displayArray(arr,colorarr)
    sleep(stepTime)
    start=0
    end=len(arr)-1

    while start<end:
        mid = int((start+end)/2)
        displayArray(arr,colorarr)
        sleep(stepTime)
        if search_element>arr[mid]:
            colorarr[start:mid+1]=['red' for x in range(mid-start+1)]
            displayArray(arr,colorarr)
            sleep(stepTime)
            start=mid+1
        elif search_element<arr[mid]:
            colorarr[mid:end+1]=['red' for x in range(end-mid+1)]
            displayArray(arr,colorarr)
            sleep(stepTime)
            end=mid-1
        else:
            break
    colorarr[arr.index(search_element)]='green'
    displayArray(arr,colorarr)
    sleep(stepTime)
    return arr.index(search_element)
    