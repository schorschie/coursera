def binary_search(keys, query):
    # write your code here
    low = 0
    high = len(keys) - 1
    
    not_found = -1
    
    while low <= high:
        mid = (low + high) // 2

        if keys[mid] == query:
            return mid
        elif query < keys[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return not_found


if __name__ == '__main__':
    DEBUG = not True
    
    if DEBUG:
        input_keys = [1, 5, 8, 12, 13]
        input_queries = [8, 1, 23, 1, 11]
    else:
        num_keys = int(input())
        input_keys = list(map(int, input().split()))
        assert len(input_keys) == num_keys
    
        num_queries = int(input())
        input_queries = list(map(int, input().split()))
        assert len(input_queries) == num_queries
        
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
