import math
import random
import time
from tkinter import *
from tkinter import ttk
from mergesort import mergeSort
from Quicksort import QuickSort
from bubblesort import bubbleSort
from selectionsort import selectionSort
from insertion import InsertionSort
from linear_search import LinearSearch
from binary_search import startBinarySearch
from tkinter import messagebox
class sortingalgorithm:
    def __init__(self,root) :
        self.root=root
        self.allAlgos = ('Bubble Sort','Merge Sort','Quick Sort','Selection Sort',"Insertion Sort")
        self.selectedAlgo = StringVar()
        self.arr = []

    def generateRandomArray(self):
        global arr
        self.arr = []
        n = int(self.dataSize.get())
        for i in range(1,n+1):
            self.arr.append(i)

            #random shuffle
        for i in range(n-1,0,-1):
            ind = math.floor(random.random()*(i+1))
            self.arr[i],self.arr[ind] = self.arr[ind],self.arr[i]

        self.arrayColor = ['BLACK' for i in range(n)]

        swapCount = 0
        self.displayArray(self.arr,self.arrayColor,swapCount)
            # return arr

    def normalizeArray(self,arr):
        return [i/max(arr) for i in arr]

    def displayArray(self,arr,arrayColor,opCount):

        self.outputCanvas.delete('all')
        n = len(arr)

        self.outputCanvasHeight = 400 - 10
        self.outputCanvasWidth = 950 - 20

        self.barWidth = self.outputCanvasWidth/(n+1)
        self.barspace = 8
        self.initialspace = 10
        normalizedArr =self.normalizeArray(arr)

        for i,h in enumerate(normalizedArr):
            #top - left                                          
            x0 = i*self.barWidth+self.initialspace+self.barspace                
            y0 = self.outputCanvasHeight - h*350                       
                
                #bottom-left                                          
            x1 = (i+1)*self.barWidth+self.initialspace                      
            y1 = self.outputCanvasHeight                               

            self.outputCanvas.create_rectangle(x0,y0,x1,y1, fill = arrayColor[i])

        ##display swapCount
        swapCountLabel = Label(self.outputCanvas,text = '#Swap Count : '+str(opCount),fg = 'white',bg = 'grey',font = ('Comic Sans MS',12))
        self.outputCanvas.create_window(80,20,window = swapCountLabel)

        self.root.update_idletasks()

    def startSort(self):
        self.arr

        if self.algoCombo.get() == 'Bubble Sort':
            bubbleSort(self.arr,self.displayArray,self.steptime.get())
        elif self.algoCombo.get() == 'Selection Sort':
            selectionSort(self.arr,self.displayArray,self.steptime.get())

        elif self.algoCombo.get() == 'Merge Sort':
            mergeSort(self.arr,self.displayArray,self.steptime.get(),0,len(self.arr)-1)

        elif self.algoCombo.get() == 'Quick Sort':
            QuickSort(self.arr,self.displayArray,self.steptime.get())

        elif self.algoCombo.get() == 'Insertion Sort':
            InsertionSort(self.arr,self.displayArray,self.steptime.get())
        else :
            messagebox.showerror("error", "algo not selected")
 
    def sorting(self):
        #----User Interface Section---------------------------------------------------------------------------------------------
        self.inputFrame = Frame(self.root,height = 200,width = 950,bg = 'GREY')
        self.inputFrame.grid(row = 0,column = 0,padx = 10,pady = 10)

        self.outputCanvas = Canvas(self.root,height = 400,width = 950,bg = 'GREY')
        self.outputCanvas.grid(row = 1,column = 0,padx = 10,pady = 10)

        #--input frame-------------------------------------------------------
        self.title= Label(self.inputFrame,text = 'SORTING ALGORITHMS VIZUALIZER',fg = 'black',bg = 'GREY',height = 1,width = 32,font = ('Ariel',14))
        self.title.grid(row = 0,column = 1,padx = 5,pady = 5)
        self.head = Label(self.inputFrame,text = 'ALGORITHM -> ',fg = 'black',bg = 'GREY',height = 1,width = 15,font = ('Ariel',14))
        self.head.grid(row = 2,column = 0,padx = 5,pady = 5)

        self.algoCombo = ttk.Combobox(self.inputFrame,values = self.allAlgos,width = 15,font = ('Ariel',14))
        self.algoCombo.grid(row = 2,column = 1,padx = 5,pady = 5)
        self.algoCombo.current()

        self.dataSize = Scale(self.inputFrame,from_ = 3,to = 100,resolution = 1,length = 400,width = 15,orient = HORIZONTAL,label = 'Data Size [n]',font = ('Ariel',10))
        self.dataSize.grid(row = 3,column = 0,padx = 5,pady = 5,columnspan = 2)

        self.steptime = Scale(self.inputFrame,from_ = 0.01,to = 1,resolution = 0.1,length = 400,width = 15,orient = HORIZONTAL,label = 'Step Delay [s]',font = ('Ariel',10))
        self.steptime.grid(row = 4,column = 0,padx = 5,pady = 5,columnspan = 2)

        self.generate = Button(self.inputFrame,text = 'GENERATE',fg = 'black',bg = '#ff0000',height = 1,width = 10,font = ('Ariel',14),command = self.generateRandomArray )
        self.generate.grid(row = 2,column = 3,padx = 5,pady = 5)

        self.play = Button(self.inputFrame,text = 'SORT',fg = 'black',bg = '#00ff00',height = 1,width = 10,font = ('Ariel',14),command = self.startSort )
        self.play.grid(row = 2,column = 4,padx = 5,pady = 5)

class searchingalgorithm:
    def __init__(self,root):
        
        self.root=root
        self.allAlgos = ('linear search','binary_search')
        self.selectedAlgo = StringVar()
        
        self.arr = []

    def generateRandomArray(self):
            #random array of non-repeating n elements
            self.arr = []
            n = int(self.dataSize.get())
            for i in range(1,n+1):
                x=random.randint(0,100)
                if x in self.arr:
                    pass
                else:
                    self.arr.append(x)
            arrayColor = ['BLACK' for i in range(n)]
            self.displayArray(self.arr,arrayColor)
  
    def normalizeArray(self,arr):
            return [i/max(arr) for i in arr]
    
    def displayArray(self,arr,arrayColor):

            self.outputCanvas.delete('all')
            n = len(arr)

            outputCanvasHeight = 400 - 10
            outputCanvasWidth = 950 - 20

            barWidth = outputCanvasWidth/(n+1)
            barspace = 8
            initialspace = 10
            normalizedArr = self.normalizeArray(arr)

            for i,h in enumerate(normalizedArr):
                #top - left                                          
                x0 = i*barWidth+initialspace+barspace                
                y0 = outputCanvasHeight - h*350                       
                
                #bottom-left                                          
                x1 = (i+1)*barWidth+initialspace                      
                y1 = outputCanvasHeight                               

                self.outputCanvas.create_rectangle(x0,y0,x1,y1, fill = arrayColor[i])

            
                label_value = Label(self.outputCanvas, text=arr[i], bg="sandy brown", fg="BLACK", font=("Ariel", 12))
                self.outputCanvas.create_window(x0,y0, window=label_value)

            self.root.update_idletasks()
    
    def start_searching(self):
        self.arr
        if self.search_element.get()=="":
            messagebox.showerror("error", "Element not found")
        if self.algoCombo.get() == 'linear search':
            k=LinearSearch(self.arr,self.displayArray,int(self.search_element.get()),self.steptime.get())
            print(self.search_element.get())
            messagebox.showinfo("Element Found", "Element found at index "+str(k))
        if self.algoCombo.get()=='binary_search':
            k=startBinarySearch(self.arr,self.displayArray,int(self.search_element.get()),self.steptime.get())
            messagebox.showinfo("Element Found", "Element found at index "+str(k))
        if self.algoCombo.get()=='' :
            messagebox.showerror("error", "algo not selected")
                
    def searching(self):
        self.inputFrame = Frame(self.root,height = 200,width = 950,bg = 'GREY')
        self.inputFrame.grid(row = 0,column = 0,padx = 10,pady = 10)

        self.outputCanvas = Canvas(self.root,height = 400,width = 950,bg = 'GREY')
        self.outputCanvas.grid(row = 1,column = 0,padx = 10,pady = 10)
        self.title= Label(self.inputFrame,text = 'SEARCHING ALGORITHMS VIZUALIZER',fg = 'black',bg = 'GREY',height = 1,width = 32,font = ('Ariel',14))
        self.title.grid(row = 0,column = 1,padx = 5,pady = 5)
        self.head = Label(self.inputFrame,text = 'ALGORITHM -> ',fg = 'black',bg = 'GREY',height = 1,width = 15,font = ('Ariel',14))
        self.head.grid(row = 1,column = 0,padx = 5,pady = 5)
        self.algoCombo = ttk.Combobox(self.inputFrame,values = self.allAlgos,width = 15,font = ('Ariel',14))
        self.algoCombo.grid(row = 1,column = 1,padx = 5,pady = 5)
        self.algoCombo.current()

        self.dataSize = Scale(self.inputFrame,from_ = 3,to = 100,resolution = 1,length = 400,width = 15,orient = HORIZONTAL,label = 'Data Size [n]',font = ('Ariel',10))
        self.dataSize.grid(row = 2,column = 0,padx = 5,pady = 5,columnspan = 2)
        self.steptime = Scale(self.inputFrame,from_ = 0.1,to = 1,resolution = 0.1,length = 400,width = 15,orient = HORIZONTAL,label = 'Step Delay [s]',font = ('Ariel',10))
        self.steptime.grid(row = 3,column = 0,padx = 5,pady = 5,columnspan = 2)

        self.generate = Button(self.inputFrame,text = 'GENERATE',fg = 'black',bg = 'red',height = 1,width = 10,font = ('Ariel',14),command = self.generateRandomArray )
        self.generate.grid(row = 2,column = 3,padx = 5,pady = 5)
        self.search= Button(self.inputFrame,text = 'SEARCHING',fg = 'black',bg = 'green',height = 1,width = 10,font = ('Ariel',14),command=self.start_searching)
        self.search.grid(row = 2,column = 4,padx = 5,pady =5)
        self.search_element = Entry(self.inputFrame, width=24, bd=3, bg='grey')
        self.search_element.pack_propagate(0)
        self.search_element.grid(row=4,column=0,padx=5,pady=5)
class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title(' Main Window')
        self.root_width = 3000
        self.root_height = 1650
        self.root.maxsize(self.root_width,self.root_height)   #(width,height)
        self.root.config(bg='BLACK')
        self.sort=sortingalgorithm(self.root)
        self.search=searchingalgorithm(self.root)
    def screen(self):
        self.main=Canvas(self.root,height = 300,width = 950,bg = 'GREY')
        self.main.grid(row = 1,column = 0,padx = 10,pady = 10)
        self.title= Label(self.main,text = 'ALGORITHMS VIZUALIZER',fg = 'black',bg = 'GREY',height = 1,width = 50,font = ('Ariel',24))
        self.title.grid(row = 0,column = 1,padx = 5,pady = (40,20))
        self.head = Label(self.main,text = 'SELECT ALOGRITHM TYPE-> ',fg = 'black',bg = 'GREY',height = 1,width = 50,font = ('Ariel',14))
        self.head.grid(row = 1, column = 1,padx = 5,pady = (20,40))
        self.sorting = Button(self.main,text = 'SORTING',fg = 'black',bg = 'Grey',height = 1,width = 10,font = ('Ariel',14),command=self.sort.sorting  )
        self.sorting.grid(row = 2,column = 1,padx = 5,pady = (20,40))
        self.searching = Button(self.main,text = 'SEARCHING',fg = 'black',bg = 'Grey',height = 1,width = 10,font = ('Ariel',14),command=self.search.searching)
        self.searching.grid(row = 3,column = 1,padx = (5,10),pady = (20,40))
        self.root.mainloop()

if __name__=='__main__':

    main=MainWindow()
    main.screen()