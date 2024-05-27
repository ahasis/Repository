def quick_sort(arr):
    """Sorts an array using the quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def search_and_replace(arr, target, replacement):
    """Searches for a target element and replaces it with a replacement element in the array."""
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement
    return arr

def main():
    # Prompt the user to input an array of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    arr = list(map(int, user_input.split()))

    # Sort the array using quick sort
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")

    # Allow the user to specify a target element to search for in the sorted array
    target = int(input("Enter the element you want to search for: "))

    # If the target element is found, prompt the user to input a replacement element
    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))
        modified_arr = search_and_replace(sorted_arr, target, replacement)
        print(f"Modified array: {modified_arr}")
    else:
        print(f"Element {target} not found in the array.")

if __name__ == "__main__":
    main()
