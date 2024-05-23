def find_max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        return (max(arr[low], arr[high]), min(arr[low], arr[high]))
    
    mid = (low + high) // 2
    max_left, min_left = find_max_min(arr, low, mid)
    max_right, min_right = find_max_min(arr, mid + 1, high)
    
    return (max(max_left, max_right), min(min_left, min_right))

if __name__ == "__main__":
    n = int(input("Enter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))
    
    max_val, min_val = find_max_min(arr, 0, n - 1)
    
    print(f"Maximum Element: {max_val}")
    print(f"Minimum Element: {min_val}")