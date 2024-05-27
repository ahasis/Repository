def bubble_sort_2d(arr):
    """Sorts a 2D array in ascending order as if it was a 1D list, maintaining the 2D structure."""
    rows = len(arr)
    cols = len(arr[0])
    total_elements = rows * cols

    for i in range(total_elements - 1):
        for j in range(total_elements - i - 1):
            r1, c1 = divmod(j, cols)
            r2, c2 = divmod(j + 1, cols)

            if arr[r1][c1] > arr[r2][c2]:
                arr[r1][c1], arr[r2][c2] = arr[r2][c2], arr[r1][c1]

def search_element(arr, target):
    """Searches for a specific element in the 2D array and prints its position if found."""
    rows = len(arr)
    cols = len(arr[0])

    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == target:
                print(f"Element {target} found at position ({r}, {c})")
                return
    print(f"Element {target} not found in the array.")

# Sample usage
arr = [
    [64, 34, 25],
    [12, 22, 11],
    [90, 88, 42]
]

print("Original array:")
for row in arr:
    print(row)

bubble_sort_2d(arr)

print("Sorted array:")
for row in arr:
    print(row)

search = int(input("Enter the element you want to search for: "))
search_element(arr, search)
