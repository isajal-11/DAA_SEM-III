#Sum of all the elements in an array and average of it
def sumAvg(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(f"Sum: {sum}")
