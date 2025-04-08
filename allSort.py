from random import randint
import math

def selectionSortMin(arr):
    size = len(arr)
    selectionSortMin2(arr, 0, size-1)
    return arr
    
def selectionSortMin2(arr, start, end):
    size = end-start+1
    if size < 2:
        return
        
    while start < end:
        indexMin = start
        
        for i in range(start+1, end+1):
            if arr[i] < arr[indexMin]:
                indexMin = i
                
        if indexMin != start:
            arr[start], arr[indexMin] = arr[indexMin] , arr[start]
                
        start += 1
    return arr
    
def selectionSortMinMax(arr):
    size = len(arr)
    selectionSortMinMax2(arr, 0, size-1)
    return arr

def selectionSortMinMax2(arr, start, end):
    size = end-start+1
    if size < 2:
        return arr
        
    while start < end:
        indexMin = start
        indexMax = start
        
        for i in range(start+1, end+1):
            if arr[i] < arr[indexMin]:
                indexMin = i
            elif arr[indexMax] < arr[i]:
                indexMax = i
        
        #~ mini = arr[indexMin]
        #~ maxi = arr[indexMax]
        #~ oldStart = arr[start]
        #~ oldEnd = arr[end] 
        if indexMin != start:
            arr[start], arr[indexMin] = arr[indexMin] , arr[start]
            if indexMax == start:    #special case
                indexMax = indexMin     #take the element which was moved from start to indexMin
        if indexMax != end:
            arr[end], arr[indexMax] = arr[indexMax], arr[end]
                
        start += 1
        end -= 1
        
        #~ print(arr, start-1, end+1,  "   ", indexMin, arr[start-1], indexMax, arr[end+1], "   ", mini, maxi, oldStart, oldEnd
        #~ if arr[start-1] > arr[end+1]:
            #~ print("problem"
    return arr

def bubbleSort(arr):
    size = len(arr)
    end = size - 1
    corrected = True
    
    while 0 < end and corrected:
        corrected = False
        for i in range(0, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        
        end -=1 #the last element is at the correct position, it is the max of all elements of array before its index.
        
        #We sort a smaller and smaller array at each turn of the loop. 1 element correctly sort in the array at turn of loop.
        #O(N*N/2)
    return arr

def bubbleSortSpecial1(arr):
    size = len(arr)
    start = 0
    end = size - 1
    corrected = True
    
    while start < end and corrected:
        corrected = False
        indexMin = start
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
                if arr[i] < arr[indexMin]:
                    indexMin = i
                
        if indexMin != start:
            arr[indexMin], arr[start] = arr[start], arr[indexMin]
                
        start += 1
        
        end -=1 #the last element is at the correct position, it is the max of all elements of array before its index.
        
        #We sort a smaller and smaller array at each turn of the loop. 2 elements correctly sort in the array at turn of loop.
        #O(N*N/3)
    return arr

def bubbleSortSpecial2(arr):
    size = len(arr)
    start = 0
    end = size - 1
    corrected = True
    
    while start < end and corrected:
        corrected = False
        indexSecondMax = start
        indexMin = start
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
                if arr[indexSecondMax] < arr[i]:
                    indexSecondMax = i
                if arr[i] < arr[indexMin]:
                    indexMin = i
            else:
                indexSecondMax = i
                
        if indexMin != start:
            arr[indexMin], arr[start] = arr[start], arr[indexMin]
            if indexSecondMax == start:    #special case
                indexSecondMax = indexMin
                
        start += 1
        
        end -=1 #the last element is at the correct position, it is the max of all elements of array before its index.
        
        if indexSecondMax != end:
            arr[end], arr[indexSecondMax] = arr[indexSecondMax], arr[end]
        end -= 1
        
        #We sort a smaller and smaller array at each turn of the loop. 3 elements correctly sort in the array at turn of loop.
        #O(N*N/4)
    return arr

    
def cycleSort(arr):
    cycleSort2(arr, 0, len(arr)-1)
    return arr
    
def cycleSort2(arr, start, end):
    size = end-start+1
    if size < 2:
        return
    
    arrIsSorted = [False]*size
    
    start2 = start
    end2 = end
    while start2 < end2:
        pos = start2-start
        if arrIsSorted[pos] == True:
            start2+=1
            continue
            
        val = arr[start2]
        nbInf = 0
        for j in range(start2+1, end2+1):
            if val > arr[j]:
                nbInf+=1
                
        #~ print(nbInf
        
        pos = start2-start+nbInf
        arrIsSorted[pos] = True
        
        if nbInf == 0:
            start2+=1
        else:
            while nbInf < end2-start2 and val == arr[start2+nbInf]:
                nbInf+=1
                arrIsSorted[start2-start+nbInf] = True
            arr[start2+nbInf], arr[start2] = arr[start2], arr[start2+nbInf]
            while start+pos < end2 and arrIsSorted[end2] == True:
                end2-=1    
        
        #~ print(start2, end2, arr
    
def countSort(arr):
    size = len(arr)
    if size < 2:
        return
    
    arrCount = [0]*size
    
    for i in range(1,size):
        val = arr[i]
        for j in range(0,i):
            if val < arr[j]:
                arrCount[j]+=1
            else:
                arrCount[i]+=1
    
    for j in range(0, size):
        i = j
        val = arr[i]
        #cycle
        while arrCount[i] != size : # do while loop not exist in Python :( , simulate it
            newIndex = arrCount[i]
            oldVal = arr[newIndex]
            arr[newIndex] = val
            
            arrCount[i] = size
            i = newIndex
            val = oldVal
    
    #~ print(arr
    return arr
    
def mergeSort(arr):
    size = len(arr)
    arrTemp = [0]*size
    mergeSort2(arr, 0, size-1, arrTemp)
    return arr

def mergeSort2(arr, start, end, arrTemp):
    if start >= end:    #1 element or stranger case
        return
    elif start+1 == end:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return
    
    middle = (start + end) // 2
    mergeSort2(arr, start, middle, arrTemp)
    mergeSort2(arr, middle+1, end, arrTemp)
    
    i = start
    j = middle+1
    k = 0
    while i <= middle and j <= end:
        if arr[i] <= arr[j]:
            arrTemp[k] = arr[i]
            i+=1
        else:
            arrTemp[k] = arr[j]
            j+=1
        k+=1
    
    while i <= middle:
        arrTemp[k] = arr[i]
        i+=1
        k+=1
        
    #not need to add arr[j] at arrTemp, they are already correctly sort at correct index between arr[j] an arr[end]
        
    if j > middle+1:
        tempEnd = k
        for k in range(0, tempEnd):
            arr[k+start] = arrTemp[k]


def insertionSort(arr):
    size = len(arr)
    insertionSort2(arr, 0, size-1)
        
    return arr
    
def insertionSort2(arr, start, end):
    insertionSort3(arr, start, end, start+1)
    return arr

#necessite des elements ordonnes entre start et iStart-1 
#Si on sait que tous les elements sont ordonnes sauf le dernier, alors on set le iStart a end 
# pour placer l'element desordonne dans la liste deja ordonnee
def insertionSort3(arr, start, end, iStart):
    size = end-start +1 
    if (size < 2):
        return arr
        
    for i in range(iStart, end+1):
        insertionSortOneElem(arr, start, i)
        
    return arr
    
def insertionSortOneElem(arr, start, i):    
    val = arr[i]
    while i > start and val < arr[i-1]:
        arr[i] = arr[i-1]
        i-=1
    
    arr[i] = val
    
def shellSort(arr):
    size = len(arr)
    shellSort2(arr,0, size-1)
    return arr
        
def shellSort2(arr, start, end):
    size = end - start +1
    if size < 2:
        return arr
    
    step = size//2
    while step > 2:
        i = start
        while i+step <= end:
            j = i
            val = arr[j+step]
            while j >= start and  arr[j] > val:
                arr[j+step] = arr[j]
                j-=step
            if j != i:
                arr[j+step] = val
            i+=1
        step = step//2+1
    
    insertionSort2(arr, start, end)
    
def heapSort(arr):
    size = len(arr)
    heapSort2(arr, 0, size-1)
            
    
def heapSort2(arr, start, end):
    size = end - start + 1
    if size < 2:
        return arr
        
    for i in reversed(range(0, size//2)): 
        tamiser(arr, i, start, end)
    
    for i in reversed(range(1, size)):
        arr[start+i], arr[start] = arr[start], arr[start+i]
        tamiser(arr, 0, start, start+i-1)
    
def tamiser(arr, noeud, start, end):
    size = end - start + 1
    k = noeud
    j = 2*k + 1
    while j < size:
        if j < size-1 and arr[start+j] < arr[start+j+1]:
            j+=1
        if arr[start+k] < arr[start+j]:
            arr[start+k], arr[start+j] = arr[start+j], arr[start+k]    # lower at the end of heap
            k = j
            j = 2*k+1
        else:
            break
    
def quickSort(arr):
    size = len(arr)
    if size < 2:
        return arr
    
    quickSort2(arr, 0, size-1)
    return arr
    
def quickSort2(arr, start, end):
    nb = end - start + 1
    if nb <= 2:
        if nb == 2 and arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return
    
    #is already sorted?
    i = start
    while i < end:
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            break
        i += 1
    
    if i == end: #isSorted
        return
    elif i == end-1:
        #only 1 element not sorted, the element precedentally at the end (and at end-1 now)
        #mini insertionSort of this element
        insertionSortOneElem(arr, start, i)
        return
            
    #~ print("mid : ", start, end, arr
    
    #pivot choice 
    pivot = randint(start, end)
    
    valPivot = arr[pivot]
    
    if pivot != end:
        arr[pivot] = arr[end]
    
    j = start
    for i in range(start, end):
        if arr[i] < valPivot:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
    arr[end] = arr[j]
    arr[j] = valPivot #at correct index
    
    quickSort2(arr, start, j-1)
    quickSort2(arr, j+1, end)
    
    #~ print("end : ", start, j , end, arr)
    
#quicksort avec moins d'ecriture memoire lors de la separation 
# entre les elements plus petits et plus grands que le pivot
def newQuickSort(arr):
    size = len(arr)
    if size < 2:
        return arr
    
    #~ print(arr)
    newQuickSort2(arr, 0, size-1)
    return arr
    
def newQuickSort2(arr, start, end):
    nb = end - start + 1
    if nb <= 2:
        if nb == 2 and arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return
    
    #is already sorted?
    i = start
    while i < end:
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            break
        i += 1
    
    if i == end: #isSorted
        return
    elif i == end-1:
        #only 1 element not sorted, the element precedentally at the end (and at end-1 now)
        #mini insertionSort of this element
        insertionSortOneElem(arr, start, i)
        return
        
    #~ print("mid : ", start, end, arr
    
    #pivot choice
    pivot = randint(start, end)
    
    valPivot = arr[pivot]
    #~ print("pivot : ", pivot, valPivot, arr)
    arr[pivot], arr[end] = arr[end], arr[pivot]
    
    #~ print(arr
    
    i = start
    j = end-1
    while i < j:
        while arr[i] < valPivot:
            i+=1
        while arr[j] >= valPivot and i < j:
            j-=1
        if i < j:
            #~ print("a : ", i, j, arr
            arr[i], arr[j] = arr[j], arr[i]
            #~ print("b : ", i, j, arr
            i+=1
            j-=1
    
    while arr[i] < valPivot:
        i+=1
    
    #~ print("c : ", i, j, arr)
    if arr[i] != valPivot:
        arr[end] = arr[i]
        arr[i] = valPivot    #at correct index
    #~ print("d : ", arr)
    
    newQuickSort2(arr, start, i-1)
    newQuickSort2(arr, i+1, end)
    
    #~ print("end : ", start, end, i, j, arr)
    
#introSort: QuickSort + HeapSort (si recursion trop profonde) + InsertionSort (si petite zone a trier)
def introSort(arr, nbMin):
    size = len(arr)
    if size < 2:
        return arr
    
    levelMax = 2*math.ceil(math.log(size,2))
    #~ print(levelMax)
    
    introSort2(arr, 0, size-1, levelMax, nbMin)
    return arr
    
def introSort2(arr, start, end, level, nbMin):
    nb = end - start + 1
    if nb <= 2:
        if nb == 2 and arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return
            
    #is already sorted?
    i = start
    while i < end:
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            break
        i += 1
    
    if i == end: #isSorted
        return
    elif i == end-1:
        #only 1 element not sorted, the element precedentally at the end (and at end-1 now)
        #mini insertionSort of this element
        insertionSortOneElem(arr, start, i)
        #~ print(start, i)
        return
    
    #insertionSort
    if nb <= nbMin:
        #~ if nb > 5 and shell:
            #~ shellSort2(arr, start, end)
        #~ else:
        insertionSort3(arr, start, end, i)    #I know all elements before 'i' are sorted.
        return

    #urgence: HeapSort
    if level == 0:
        print(start, end)
        heapSort2(arr, start, end)
        return
    
    #pivot choice 
    pivot = randint(start, end)
        
    valPivot = arr[pivot]
    
    if pivot != end:
        arr[pivot] = arr[end]
    
    j = start
    #~ indexMin = start    #slower, strangely
    #~ indexMax = start
    for i in range(start, end):
        if arr[i] < valPivot:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
            
    arr[end] = arr[j]
    arr[j] = valPivot #at correct index
    
    
    level -= 1
    
    #~ introSort2(arr, start+1, j-1, level, shell, nbMin)    #with indexMin, but slower
    introSort2(arr, start, j-1, level, nbMin)
    introSort2(arr, j+1, end, level, nbMin)
    


def newIntroSort(arr, nbMin):
    size = len(arr)
    if size < 2:
        return arr
    
    levelMax = 2*math.ceil(math.log(size,2))
    #print(arr)
    newIntroSort2(arr, 0, size-1, levelMax, nbMin)
    return arr
    
def newIntroSort2(arr, start, end, level, nbMin):
    nb = end - start + 1
    if nb <= 2:
        if nb == 2 and arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        return
            
    #is already sorted?
    i = start
    while i < end:
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            break
        i += 1
    
    if i == end: #isSorted
        return
    elif i == end-1:
        #only 1 element not sorted, the element precedentally at the end (and at end-1 now)
        #mini insertionSort of this element
        insertionSortOneElem(arr, start, i)
        #print(start, i)
        return
    
    #insertionSort
    if nb <= nbMin:
        insertionSort3(arr, start, end, i)    #I know all elements before 'i' are sorted.
        return

    #urgence: HeapSort
    if level == 0:
        #print(start, end)
        heapSort2(arr, start, end)
        return
    
    #pivot choice 
    pivot = randint(start, end)
        
    valPivot = arr[pivot]
    
    if pivot != end:
        arr[pivot], arr[end] = arr[end], valPivot
    
    i = start
    j = end-1
    while i < j:
        while arr[i] < valPivot:
            i+=1
        while arr[j] >= valPivot and i < j:
            j-=1
        if i < j:
            #print("a : ", i, j, arr)
            arr[i], arr[j] = arr[j], arr[i]
            #print("b : ", i, j, arr)
            i+=1
            j-=1
    
    while arr[i] < valPivot:
        i+=1
    
    #print("c : ", i, j, arr)
    if arr[i] != valPivot:
        arr[end] = arr[i]
        arr[i] = valPivot    #at correct index
    #print("d : ", arr)
    
    level -= 1
    
    #~ introSort2(arr, start+1, j-1, level, shell, nbMin)    #with indexMin, but slower
    newIntroSort2(arr, start, i-1, level, nbMin)
    newIntroSort2(arr, i+1, end, level, nbMin)
    

#timSort: MergeSort + InsertionSort (si petite zone a trier)
def timSort(arr):
    size = len(arr)
    if size < 16:
        insertionSort(arr);
    arrTemp = [0]*size
    timSort2(arr, 0, size-1, arrTemp)
    return arr

def timSort2(arr, start, end, arrTemp):
    if start >= end:    #1 element or strange case
        return
    size = end - start + 1
    if size <= 16:
        insertionSort2(arr, start, end)
        return
    
    middle = (start + end) // 2
    timSort2(arr, start, middle, arrTemp)
    timSort2(arr, middle+1, end, arrTemp)
    
    i = start
    j = middle+1
    k = 0
    while i <= middle and j <= end:
        if arr[i] <= arr[j]:
            arrTemp[k] = arr[i]
            i+=1
        else:
            arrTemp[k] = arr[j]
            j+=1
        k+=1
    
    while i <= middle:
        arrTemp[k] = arr[i]
        i+=1
        k+=1
        
    #not need to add arr[j] at arrTemp, they are already correctly sort at correct index between arr[j] an arr[end]
        
    if j > middle+1:
        tempEnd = k
        for k in range(0, tempEnd):
            arr[k+start] = arrTemp[k]
    

    
########################################################################
########################################################################
########################################################################
########################################################################
########################################################################    


def bucketSort(arr, initNbBuckets=100):
    bucketSort2(arr, 0, len(arr)-1, initNbBuckets)
    return arr

def bucketSort2(arr, start, end, initNbBuckets=100):
    size = end-start+1
    if size < 2:
        return arr
    
    indexMin = start
    indexMax = start
    isAlreadySorted = True
    #selectionSortMinMax to find mini and maxi
    for i in range(1, size):
        if arr[i] < arr[indexMin]:
            indexMin = i
            isAlreadySorted = False
        elif arr[i] > arr[indexMax]:
            indexMax = i
        elif isAlreadySorted and arr[i] != arr[indexMax]:
            isAlreadySorted = False

    if isAlreadySorted:
        return arr
    
    mini = arr[indexMin]
    maxi = arr[indexMax]

    diff = maxi-mini
    #~ print(mini, maxi)

    if indexMin != start:
        arr[start], arr[indexMin] = arr[indexMin] , arr[start]
        if indexMax == start:    #special case
            indexMax = indexMin     #take the element which was moved from start to indexMin
    if indexMax != end:
        arr[end], arr[indexMax] = arr[indexMax], arr[end]
                
    start += 1
    end -= 1

    
    if size < 20:
        if size > 3:
            insertionSort2(arr, start, end)
        return arr

    # if 64 elems in [0..64] => 3 elems per bucket and 22 buckets
    sizeBucket = (diff//initNbBuckets) + 1
    nbBuckets = (diff//sizeBucket) + 1     

    arrBucket = [[] for _ in range(nbBuckets)]   #2D array of nbBucket empty arrays 
    
    for i in range(start, end+1):
        index = (arr[i]-mini)//sizeBucket
        arrBucket[index].append(arr[i])
    
    #~ print(arrBucket)
    k = start
    for i in range(0, nbBuckets):
        bucket = arrBucket[i]
        bucketSort(bucket, initNbBuckets)
        for j in range(0, len(bucket)):
            arr[k] = bucket[j]
            k+=1
        arrBucket[i].clear()
    
    return arr


def bucketSortBinary(arr):
    bucketSortBinary2(arr, 0, len(arr)-1)
    return arr

def bucketSortBinary2(arr, start, end):
    size = end-start+1
    if size < 2:
        return arr
    
    indexMin = start
    indexMax = start
    isAlreadySorted = True
    #selectionSortMinMax to find mini and maxi
    for i in range(1, size):
        if arr[i] < arr[indexMin]:
            indexMin = i
            isAlreadySorted = False
        elif arr[i] > arr[indexMax]:
            indexMax = i
        elif isAlreadySorted and arr[i] != arr[indexMax]:
            isAlreadySorted = False

    if isAlreadySorted:
        return arr
    
    mini = arr[indexMin]
    maxi = arr[indexMax]

    if indexMin != start:
        arr[start], arr[indexMin] = arr[indexMin] , arr[start]
        if indexMax == start:    #special case
            indexMax = indexMin     #take the element which was moved from start to indexMin
    if indexMax != end:
        arr[end], arr[indexMax] = arr[indexMax], arr[end]
                
    start += 1
    end -= 1

    if size <= 3:  #all elements are equals
        return arr
    
    bitNum = int(math.log2(maxi)) #find the bit MSB of the max value
    mask = 1 << bitNum;
    while(mask & mini) == (mask & maxi):    #find the first bit of mini and max which are different
        bitNum -= 1
        mask = mask >> 1
    bucketSortBinary3(arr, start, end, bitNum)

    return arr

# [1000,0110,0101,0011,1101] -> mask 1000 bit 0: [0011,0110,0101] and bit 1: [1000,1101]
# [0011,0110,0101] -> mask 0100 bit 0: [0011]* and bit 1: [0110,0101]
# [0110,0101] -> mask 0010 bit 0: [0101]* and bit 1: [0110]*
# [1000,1101] -> mask 0100 bit 0: [1000]* and bit 1: [1101]*
# sort res : [0011, 0101,0110,1000,1101]
def bucketSortBinary3(arr, start, end, bitNum):
    size = end-start+1
    if size < 2:
        return arr

    mask = 1 << bitNum
    end0 = start
    start1 = end
    while end0 < start1:
        while (arr[end0] & mask) == 0 and end0 < start1:    #find first element with bit 1 at this numBit
            end0+=1
        while (arr[start1] & mask) != 0 and end0 < start1:  #find first element with bit 0 at this numBit
            start1-=1
        if end0 < start1:
            # swap in order to have all elements with bit 0 before elements with bit 1
            arr[end0], arr[start1] = arr[start1], arr[end0] 
            end0+=1
            start1-=1

    if (arr[end0] & mask) != 0:
        end0-=1
    if (arr[start1] & mask) == 0:
        start1+=1

    bitNum -= 1
    if bitNum < 0:
        return arr
    bucketSortBinary3(arr, start, end0, bitNum)
    bucketSortBinary3(arr, start1, end, bitNum)
