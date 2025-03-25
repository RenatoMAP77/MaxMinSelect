def max_min_select(arr, left, right):
    # Caso base: um único elemento
    if left == right:
        return arr[left], arr[left]
    
    # Caso base: dois elementos
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    # Divide o array ao meio
    mid = (left + right) // 2
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)
    
    # Combina os resultados
    return min(min1, min2), max(max1, max2)
