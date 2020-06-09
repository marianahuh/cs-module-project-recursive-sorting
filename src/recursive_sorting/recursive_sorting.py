# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # check if one or both lists are empty
    if len(arrA) == 0:
        return arrB
    elif len(arrB) == 0:
        return arrA
    # initialize left and right lists
    L, R = 0, 0

    for i in range(0, elements):
        if L >= len(arrA):
            merged_arr[i] = arrB[R]
            R += 1
        elif R >= len(arrB):
            merged_arr[i] = arrA[L]
            L += 1
        elif arrA[L] < arrB[R]:
            merged_arr[i] = arrA[L]
            L += 1
        else:
            merged_arr[i] = arrB[R]
            R += 1

    return merged_arr


# l1 = [2, 3, 6, 8, 10]
# l2 = [1, 3, 5, 7, 8, 9]
# print(f'Merged list: {merge(l1,l2)}')

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    # return arr


list = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(merge_sort(list))


# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    pass
    return arr


def merge_sort_in_place(arr, l, r):
    pass

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
