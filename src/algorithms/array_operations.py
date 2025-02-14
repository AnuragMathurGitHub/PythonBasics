def find_max(arr):
    """Find the maximum element in an array."""
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def find_min(arr):
    """Find the minimum element in an array."""
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

def sum_array(arr):
    """Calculate the sum of all elements in an array."""
    total = 0
    for num in arr:
        total += num
    return total

def reverse_array(arr):
    """Reverse the elements of an array."""
    return arr[::-1]

def array_average(arr):
    """Calculate the average of elements in an array."""
    if not arr:
        return None
    return sum(arr) / len(arr)

# Example usage
if __name__ == "__main__":
    sample_array = [1, 2, 3, 4, 5]
    print("Max:", find_max(sample_array))
    print("Min:", find_min(sample_array))
    print("Sum:", sum_array(sample_array))
    print("Reversed:", reverse_array(sample_array))
    print("Average:", array_average(sample_array))