import time
import random
import copy

arr1 = random.sample(range(100000), 500)
arr2 = copy.deepcopy(arr1)
arr3 = copy.deepcopy(arr1)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def quick_sort(arr2):
    if len(arr2) <= 1:
        return arr2
    pivot = len(arr2) - 1
    i = 0
    j = len(arr2) - 2
    while (i < j):
        while (arr2[i] < arr2[pivot]):
            i += 1
        while (arr2[j] > arr2[pivot]):
            j -= 1
        if (i < j):
            arr2[i], arr2[j] = arr2[j], arr2[i]
    if (arr2[i] > arr2[pivot]):
        arr2[i], arr2[pivot] = arr2[pivot], arr2[i]
    return quick_sort(arr2[:pivot]) + [arr2[pivot]] + quick_sort(arr2[pivot+1:])


def merge_sort(arr3):
    if len(arr3) < 2:
        return arr3
    mid = len(arr3)//2
    low_arr = merge_sort(arr3[:mid])
    high_arr = merge_sort(arr3[mid:])

    merged_arr = []
    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


start1 = time.time()
bubble_sort(arr1)
print("버블 정렬 시간: %.8f" % (time.time() - start1))

start2 = time.time()
quick_sort(arr2)
print("퀵 정렬 시간: %.8f" % (time.time() - start2))

start3 = time.time()
merge_sort(arr3)
print("병합 정렬 시간: %.8f" % (time.time() - start3))
