from maxminselect import max_min_select
def main():
    # Teste com diferentes arrays
    test_cases = [
        [3, 1, 5, 9, 2, 8],
        [10, 20, 30, 40, 50],
        [100],
        [7, -2, 4, 0, 9, 1],
        [-5, -10, -3, -1, -7]
    ]
    
    for i, arr in enumerate(test_cases):
        min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
        print(f"Teste {i+1}: {arr}")
        print(f"  Mínimo: {min_val}, Máximo: {max_val}\n")

if __name__ == "__main__":
    main()