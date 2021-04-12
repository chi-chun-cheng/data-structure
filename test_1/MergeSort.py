#Recursive method
def MergeSort_0(input):
    
    # The last step of recursion will stop at here.
    if len(input) < 2:
        return input
    
    #Start Recursion.
    mid = len(input) // 2
    left = MergeSort_0(input[:mid])
    right = MergeSort_0(input[mid:])
    output = []

    #Pop out the smallest element into output
    #Warn:Pop cause more time
    while left and right:
        if left[-1] >= right[-1]:
            output.insert(0, left.pop())
        else:
            output.insert(0, right.pop())
    
    #The remain list with the larger element will add to output.
    if left:
        output = left + output
    if right:
        output = right + output
    return output

def MergeSort_1(input):
    if len(input) < 2:
        return input
    
    mid = len(input) // 2
    left = MergeSort_1(input[:mid])
    right = MergeSort_1(input[mid:])
    output = []
    l=r=0
    while r != len(right) and l != len(left):
        if left[l] <= right[r]:
            output.append(left[l])
            l+=1
        else:
            output.append(right[r])
            r+=1
    if r != len(right):
        output = output+right[r:]
    if l != len(left):
        output = output+left[l:]
    
    return output

if __name__ == "__main__":
    nums = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("Original list:", nums)
    print("After Sorted ver.0:", MergeSort_0(nums))
    print("After Sorted ver.1:", MergeSort_1(nums))
