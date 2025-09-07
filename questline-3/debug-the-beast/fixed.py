#Program: Find the second largest number in a list

def second_largest(arr):
    largest = second = -9999999
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num!=largest:
            second = num
        else:
            continue
    return second



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

print("Second largest:", second_largest(arr))



