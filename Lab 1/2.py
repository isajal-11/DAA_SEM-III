#Find the largest in a given array
def largestSum(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]

    print (largest)
        

