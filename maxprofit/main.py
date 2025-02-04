def max_profit(arr: list[int]) -> int:
    min_index, min_value = min(enumerate(arr), key=lambda x: x[1])
    head = arr[:min_index]
    tail = arr[min_index + 1 :]
    max_head = max(head)
    max_tail = max(tail)

    return max_head - min_value + max_tail


if __name__ == "__main__":
    arr = [2, 4, 1, 5, 7]
    result = max_profit(arr)
    print(result)
