class BinarySearch:
    def binary_search(self, array, lb, ub, val):
        if lb <= ub:
            mid_index = (lb + ub) // 2
            mid_value = array[mid_index]
            if mid_value == val:
                return mid_index
            elif mid_value > val:
                return self.binary_search(array, lb, mid_index - 1, val)
            else:
                return self.binary_search(array, mid_index + 1, ub, val)
        else:
            return -1

if __name__ == "__main__":
    res = BinarySearch()
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 10
    result = res.binary_search(arr, 0, n - 1, x)
    if result == -1:
        print("Element not present")
    else:
        print("Element found at index", result)
