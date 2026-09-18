#Implement Binary Search both iteratively and recursively


# Iterative Binary Search 
def binary_search_iter(arr, target):
    L, H = 0, len(arr) - 1
    while L <= H:
        mid = (L + H) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            L = mid + 1
        else:
            H= mid - 1
    return -1

#Recursive waala
def RBSearch(A, l, h, key):

    if l>h:
        return -1
    elif l == h:
        if A[l] == key:
            return l
        else:
            return -1
    else:
        mid = (l + h) // 2
        if key == A[mid]:
            return mid
        if key < A[mid]:
            return RBSearch(A, l, mid - 1, key)
        else:
            return RBSearch(A, mid + 1, h, key)




    
