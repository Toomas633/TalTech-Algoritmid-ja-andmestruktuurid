from random import randint
from time import time

""" Bubble sort. 
Käib massiivi järjest läbi, kui leiab eelmisest väiksema liikme vahetab nende kohad. 
Jätkab sorteerimist kuni pole midagi enam ümber tõsta.
"""
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		if not swapped:
			return

""" Bucket Sort
Elemendid jaotatkse väiksematesse gruppidesse kokku ning seejärel sorteeritakse gruppide kaupa.
"""
# https://www.programiz.com/dsa/bucket-sort

def bucketSort(array):
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    for j in array:
        index_b = int(j)
        bucket[index_b].append(j)
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

""" Quicksort
Valib punkti massiivis, jaotab ümber selle massiivi alamosadeks ja sorteerib.
"""
# https://www.geeksforgeeks.org/quick-sort/

def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)

""" Timsort
Leiab juba õiges järjestuses olevad osad massiivist ning liigutab neid.
"""
# https://www.geeksforgeeks.org/timsort/

MIN_MERGE = 32
 
def calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

array_n = [randint(0, 1000) for _ in range(5000)]
avg_bubble = avg_bucket = avg_quick = avg_tim = 0

print(f'{"     "} {"Bubble sort:":^15}{"Bucket sort:":^15}{"Quicksort:":^15}{"Timsort:":^15}')
for _ in range(10):
    # Bubble sort
    start_time_bubble = time()
    temp_array = array_n.copy()
    bubbleSort(temp_array)
    end_time_bubble = time()
    avg_bubble += end_time_bubble - start_time_bubble
    #Bucket sort
    start_time_bucket = time()
    temp_array = array_n.copy()
    bucketSort(temp_array)
    end_time_bucket = time()
    avg_bucket += end_time_bucket - start_time_bucket
    #Quicksort
    start_time_quick = time()
    temp_array = array_n.copy()
    quick_sort(temp_array, 0, len(temp_array) - 1)
    end_time_quick = time()
    avg_quick = end_time_quick - start_time_quick
    #Timsort
    start_time_tim = time()
    temp_array = array_n.copy()
    timSort(temp_array)
    end_time_tim = time()
    avg_tim += end_time_tim - start_time_tim
    #Prindi tulemused
    print(f'{"     "} {end_time_bubble - start_time_bubble:^15f}{end_time_bucket - start_time_bucket:^15f}{end_time_quick - start_time_quick:^15f}{end_time_tim - start_time_tim:^15f}')
print(f'Avg: {avg_bubble/10:^15.4f}{avg_bucket/10:^15.4f}{avg_quick/10:^15.4f}{avg_tim/10:^15.4f}')