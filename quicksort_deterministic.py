import random
import time

# Function to perform the partitioning step in Quicksort
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1  # Index for the smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to its correct position
    return i + 1

# Function to implement the deterministic Quicksort
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition the array
        quicksort(arr, low, pi - 1)  # Recursively sort the left part
        quicksort(arr, pi + 1, high)  # Recursively sort the right part

# Performance analysis of Quicksort
def analyze_performance(arr):
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Example usage
if __name__ == "__main__":
    # Test with an example list
    arr = [random.randint(1, 1000) for _ in range(1000)]  # Generating a random array
    print("Deterministic Quicksort")
    print("Time taken for sorting:", analyze_performance(arr))

