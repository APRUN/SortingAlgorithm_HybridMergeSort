
import random
import time

#Function to write data to csv file
def WriteDatatoFile(array,path):
    file=open(file=path,mode="w")
#Write data to file
    for i in array:
        i=str(i)
        file.write(i+"\n")


#Function to generate a Random array
def RandomArray(size):
    Numbers=[] #Array to store random numbers
    for i in range(size):
        rand_number=random.randint(-50000,50000) #Generating Random Ints
        Numbers.append(rand_number)
    return Numbers



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    a1 = [0] * n1
    a2 = [0] * n2
    
    for i in range(n1):
        a1[i] = array[p + i]
    for i in range(n2):
        a2[i] = array[q + i + 1]
    
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if a1[i] < a2[j]:
            array[k] = a1[i]
            i = i + 1
        else:
            array[k] = a2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        array[k] = a1[i]
        k = k + 1
        i = i + 1
    while j < n2:
        array[k] = a2[j]
        k = k + 1
        j = j + 1

def MergeSort(array, p, r, threshold=10):
    if r - p <= threshold:
        insertion_sort(array[p:r + 1])
    else:
        q = (p + r) // 2
        MergeSort(array, p, q, threshold)
        MergeSort(array, q + 1, r, threshold)
        Merge(array, p, q, r)

arr = RandomArray(100)
print("Original array:", arr)
start_time=time.time()
MergeSort(arr, 0, len(arr) - 1)
end_time=time.time()
print("Time ",end_time-start_time)
print("Sorted array:", arr)

