def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key.lower() < arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_strings = input("Enter a list of strings separated by commas: ").split(',')
input_strings = [s.strip() for s in input_strings]
sort(input_strings)
print("Alphabetical Order Sorting:", input_strings)
