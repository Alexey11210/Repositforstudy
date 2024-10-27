def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        i = [n]
        if n == 5:
            matrix.append(i)
            if n== 5:
                matrix.append(i)
        for j in range(m):
            j = [m]
            if m == 42:
                matrix.append(j)
            for k in range(value):
                k = [value]
                if value == 10:
                    k = [[value]*2]*2
                    matrix.append(k)
                if value == 42:
                    k = [[value]*5]*3
                    matrix.append(k)
                if value == 13:
                    k = [[value]*2]*4
                    matrix.append(k)
                return (matrix)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
