#Wap to reverse an array
#Here i used the two pointer approach
def reverseArray(arr):
    L,R=0,len(arr)-1
    while L<R:
        arr[L],arr[R]=arr[R],arr[L]
        L=L+1
        R=R-1
            
    