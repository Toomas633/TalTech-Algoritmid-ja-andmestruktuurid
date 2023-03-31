# KT 1 21.10.2022
def ÜL3():
# Python program for implementation of Insertion Sort
    def insertionSort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    arr = [44, 25, 27, 16, 32, 50, 37] #! Adnmed
    insertionSort(arr)
    for i in range(len(arr)):
        print("% d" % arr[i])
    
def ÜL5():
    # Python 3 program for recursive binary search.
    import time
    start_time = time.time()
    def binary_search(arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
            else:
                return binary_search(arr, mid + 1, high, x)
        else:
            return -1
    arr = [11,13,16,20,25,29,32,34,35,37,40,44,49,53,56,58,59,61,64,68] #! Andmed
    x = 51                                                              #! Punkt
    result = binary_search(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

def ÜL6():
    # Python3 program to find maximum and minimum in a Binary Tree
    class newNode:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None
    def findMax(root):
        if (root == None):
            return float('-inf')
        res = root.data
        lres = findMax(root.left)
        rres = findMax(root.right)
        if (lres > res):
            res = lres
        if (rres > res):
            res = rres
        return res
    if __name__ == '__main__':
        root = newNode(2)
        root.left = newNode(7)
        root.right = newNode(5)
        root.left.right = newNode(6)
        root.left.right.left = newNode(1)
        root.left.right.right = newNode(11)
        root.right.right = newNode(9)
        root.right.right.left = newNode(4)
        print("Maximum element is", findMax(root))

def ÜL8():
    #15%2
    a = 15  #! Andmed
    b = 2   #! Andmed
    try:
        c = a -b
        while(c >= 0):
            c -= b
    finally:
        c += b
        print(c)
    print(15%2)
    
def ÜL12():
    a = 31%9    #! Andmed
    print(a)

ÜL12()