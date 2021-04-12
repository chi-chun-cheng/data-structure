def QuickSort(input, left, right):
    if left >= right:
        return
    
    i = left
    j = right
    index = input[left]

    while i!=j:
        while input[j]>index and i<j:
            j -= 1
        while input[i]<=index and i<j:
            i += 1
        if i<j:
            input[i], input[j] = input[j], input[i]
    
    input[left] = input[i]
    input[i] = index

    QuickSort(input, left, i-1)
    QuickSort(input, i+1, right)

if __name__ == "__main__":
    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 23]
    QuickSort(data, 0, len(data)-1)
    print(data)