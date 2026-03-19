def hamming_dual_simplex_check(r):
    n = (1 << r) - 1
    H = []
    for i in range(1, n + 1):        
        col = [(i >> k) & 1 for k in range(r)] 
        H.append(col)
    H_rows = [[H[j][i] for j in range(n)] for i in range(r)]

    G_dual = H_rows
    print(f"\n=== r = {r}, n = {n} ===")
    print("Порождающая матрица дуального кода (размер {}x{}):".format(r, n))
    for row in G_dual:
        print(' '.join(map(str, row)))

    weights = []
    nonzero_codewords = []

    for u_int in range(1 << r): 
        u = [(u_int >> k) & 1 for k in range(r)]
        codeword = [0] * n
        for i in range(r):
            if u[i]:
                codeword = [ (codeword[j] ^ G_dual[i][j]) for j in range(n) ]
        weight = sum(codeword)
        if u_int != 0:      
            weights.append(weight)
            nonzero_codewords.append((u_int, codeword, weight))
        else:
            zero_weight = weight  

    unique_weights = set(weights)
    if len(unique_weights) == 1:
        const_weight = next(iter(unique_weights))
        print(f"\nВсе ненулевые слова имеют одинаковый вес: {const_weight}")

    print(f"\nВсе {len(nonzero_codewords)} ненулевых кодовых слов (информационный вектор -> слово, вес):")
    for u_int, cw, w in nonzero_codewords:
        cw_str = ''.join(map(str, cw))
        print(f"  u={u_int:0{r}b} -> {cw_str}  вес={w}")

if __name__ == "__main__":
    for r in (3, 4, 5):
        hamming_dual_simplex_check(r)