import timeit
import random


# https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# https://www.geeksforgeeks.org/python-program-for-merge-sort/
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def hybridSort(arr, l, r, k):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        if len(arr) >= k:
            mergeSort(arr, l, m)
        else:
            insertionSort(arr)

        if len(arr) >= l:
            mergeSort(arr, m + 1, r)
        else:
            insertionSort(arr)

        merge(arr, l, m, r)


my_setup = '''
my_list = random.sample(range(1, 500), n)
'''

inserSort = '''
insertionSort(my_list)
'''

merSort = '''
mergeSort(my_list, 0, n-1)
'''

hybrSort = '''
hybridSort(my_list, 0, n-1, k)
'''

k = 80
max_times = 150
n = 10

open("hybrid_sort.txt", "w").close()
open("merge_sort.txt", "w").close()
open("insert_sort.txt", "w").close()

while n < max_times:
    hybrid_file = open("hybrid_sort.txt", "a")
    hybrid_time = (timeit.timeit(setup=my_setup, stmt=hybrSort, number=1, globals=globals()) * 1000)
    hybrid_file.write(str(hybrid_time))
    hybrid_file.write(", ")

    merge_file = open("merge_sort.txt", "a")
    merge_time = timeit.timeit(setup=my_setup, stmt=merSort, number=1, globals=globals()) * 1000
    merge_file.write(str(merge_time))
    merge_file.write(", ")

    insert_file = open("insert_sort.txt", "a")
    insert_time = timeit.timeit(setup=my_setup, stmt=inserSort, number=1, globals=globals()) * 1000
    insert_file.write(str(insert_time))
    insert_file.write(", ")

    n += 10
