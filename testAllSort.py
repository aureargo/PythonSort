import allSort	
from random import randint
import time

nbElem = 2000000

testBubbleSort = False
testBubbleSortSpecial1 = False
testBubbleSortSpecial2 = False
testSelectionSortMin = False
testSelectionSortMinMax = False
testCycleSort = False
testCountSort = False
testInsertionSort = False

testMergeSort = False
testShellSort = False
testHeapSort = False
testQuickSort = False
testQuickSort2 = False
testIntroSort = False
testIntroSortV2 = False
testTimSort = False
testIntroSortWithDifferentsPack = False

testBucketSort = True
testBucketSortBinary =  True


testN2Sort = False
testNLogNSort = False
testBucketSortWithDifferentsPack = True

if(testN2Sort):
	testBubbleSort = True
	testBubbleSortSpecial1 = True
	testBubbleSortSpecial2 = True
	testSelectionSortMin = True
	testSelectionSortMinMax = True
	testCycleSort = True
	testCountSort = True
	testInsertionSort = True

if(testNLogNSort):
	testMergeSort = True
	testShellSort = True
	testHeapSort = True
	testQuickSort = True
	testQuickSort2 = True
	testIntroSort = True
	testIntroSortV2 = True
	testTimSort = True
	testBucketSort = True
	testBucketSortBinary = True


def copy(arr):
	arrCopy = []
	for val in arr:
		arrCopy.append(val)
	return arrCopy
	
def isSorted(arr):
	res = True
	val = arr[0]
	for i in range(1, len(arr)):
		val2 = arr[i]
		if val > val2:
			res = False
			break
		val = val2
	return res ,i, val, val2
	
arrInit = []
if True:
	for i in range(0, nbElem):
		val = randint(0,10*nbElem)
		arrInit.append(val)

#~ arrInit = [8, 5, 2, 8]	#selectionSort trap
#~ arrInit = [3,9,1,2,7, 4, 3]
#~ arrInit = [3,9,1,2,7,3,8,7,3,1,5,4,6,26,9,854,64,3,4,5,6,5,7,3,5,7,1,2,3,8,4,10, 12, 6, 2]
#arrInit = [193, 39, 39, 155, 213, 176, 84, 409, 180, 54, 451, 351, 202, 400, 307, 432, 340, 425, 106, 272, 33, 186, 304, 97, 412, 300, 392, 316, 485, 324, 207, 187, 194, 25, 341, 307, 438, 268, 80, 476, 0, 349, 469, 444, 285, 480, 428, 273, 417, 281]

timeWait = 0.1
#~ print(arrInit

tac = time.perf_counter()
correctOrder = copy(arrInit)
tic = time.perf_counter()
correctOrder.sort()
toc = time.perf_counter()
sort, i, val, val2 = isSorted(correctOrder)
tuc = time.perf_counter()
print("correctOrder :", toc - tic)
print("copy : ", tic - tac)
print("isSorted :", tuc - toc)


def test(func):
	arr = copy(arrInit)
	time.sleep(timeWait)
	tic = time.perf_counter()
	func(arr)
	toc = time.perf_counter()
	#print("bubbleSort :", arr
	sort, i, val, val2 = isSorted(arr)
	print(func.__name__, ":", sort)
	if not sort:
		print(arr, i, val, val2	)	
	if correctOrder != arr:
		print("error")
	print(func.__name__, ":", toc - tic)

def test2(func, param):
	arr = copy(arrInit)
	time.sleep(timeWait)
	tic = time.perf_counter()
	func(arr, param)
	toc = time.perf_counter()
	#print("bubbleSort :", arr
	sort, i, val, val2 = isSorted(arr)
	print(func.__name__, ":", sort)
	if not sort:
		print(arr, i, val, val2	)	
	if correctOrder != arr:
		print("error")
	print(func.__name__, ":", toc - tic)


#Long calculation
#if testN2Sort:
	
if testBubbleSort:
	test(allSort.bubbleSort)

if testBubbleSortSpecial1:
	test(allSort.bubbleSortSpecial1)

if testBubbleSortSpecial2:
	test(allSort.bubbleSortSpecial2)

if testSelectionSortMin:
	test(allSort.selectionSortMin)

if testSelectionSortMinMax:
	test(allSort.selectionSortMinMax)

if testCycleSort:
	test(allSort.cycleSort)
	
if testCountSort:
	test(allSort.countSort)
	
if testInsertionSort:
	test(allSort.insertionSort)
	
#Optimised calculation
#if testNLogNSort:
print("")
if testMergeSort:
	test(allSort.mergeSort)



if testShellSort:
	test(allSort.shellSort)

if testHeapSort:
	test(allSort.heapSort)

if testQuickSort:
	test(allSort.quickSort)

if testQuickSort2:
	test(allSort.newQuickSort)

if testIntroSort:
	test2(allSort.introSort, 18)
	
if testIntroSortV2:
	test2(allSort.newIntroSort, 18)

if testTimSort:
	test(allSort.timSort)


if testBucketSort:
	test(allSort.bucketSort)

if testBucketSortBinary:
	test(allSort.bucketSortBinary)

if testIntroSortWithDifferentsPack:
	print("")

	#best: 18 not shell
	#best: 19 not shell
	bestTime = 10000
	nbTest = 1
	for i in range(6, 35):
		#~ time.sleep(timeWait)
		#~ timer = 0
		#~ sort = True
		#~ for j in range(0,nbTest):
			#~ arr = copy(arrInit)
			#~ tic = time.perf_counter()
			#~ allSort.introSort(arr, True, i)
			#~ toc = time.perf_counter()
			#~ #print("introSort :", arr
			#~ sort &= isSorted(arr)
			#~ timer += toc - tic
			
		#~ if timer < bestTime:
				#~ bestTime = timer
		#~ print("introSort shell " , i, sort, " :", timer/nbTest, "new best time" if bestTime == timer else ""
		
		time.sleep(timeWait)
		timer = 0
		sort = True
		for j in range(0,nbTest):
			arr = copy(arrInit)
			tic = time.perf_counter()
			allSort.introSort(arr, False, i)
			toc = time.perf_counter()
			#print("introSort :", arr
			s,_,_,_ = isSorted(arr)
			sort &= s
			timer += toc - tic			
			if correctOrder != arr:
				print("error")
		 	
		if timer < bestTime:
			bestTime = timer
		
		print("introSort inser " , i, sort, " :", timer/nbTest, "new best time" if bestTime == timer else "")
		
	print("")

if testBucketSortWithDifferentsPack:
	print("")

	#best: 121 for 50000 and 100 tests
	#bucketSort inser  65 True  :     0.03037727131992142    new best time 
	#bucketSort inser  94 True  :     0.027860864320027757   new best time 
	#bucketSort inser  121 True  :    0.027766434980003397   new best time 
	#best: 114 for 100000 and 200 tests
	#bucketSort inser  94 True  :     0.06076697548504853    new best time 
	#bucketSort inser  113 True  :    0.0585573403950093     new best time 
	#bucketSort inser  114 True  :    0.058552081495026866   new best time 
	bestTime = 10000
	secondTime = 10001
	nbTest = 2

	print(" nbElem :", nbElem, "\tnbTest :", nbTest)
	i = 10
	while(i < 1000):
		time.sleep(timeWait)
		timer = 0
		sort = True
		for j in range(0,nbTest):
			arr = copy(arrInit)
			tic = time.perf_counter()
			allSort.bucketSort(arr, i)
			toc = time.perf_counter()
			#print("bucketSort :", arr
			s,_,_,_ = isSorted(arr)
			sort &= s
			timer += toc - tic			
			if correctOrder != arr:
				print("error")
			
		if(timer < secondTime):
			if timer < bestTime:
				secondTime = bestTime
				bestTime = timer
			else:
				secondTime = timer
		
		print("bucketSort config " , i, sort, " :\t", timer/nbTest,
				"\t*" if bestTime*1.05 > timer else "",
				"***new best time***" if bestTime == timer else "",
				"second time"  if secondTime == timer else "")
		
		if(timer < secondTime*1.1):
			i += 1
		else:
			sup = ((timer/secondTime)-1)*20

			if sup > 20:
				sup*= 2
			i += int(sup)

	
	print("")