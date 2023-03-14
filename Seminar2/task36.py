def print_operation_table(operation, num_rows=6, num_columns=6):
    a = []
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            a.append(operation(i, j))
    print(*a)
    print(*a[:6])
    print(*a[6:12])
    print(*a[12:18])
    print(*a[18:24])
    print(*a[24:30])
    print(*a[30:36])

    
     

print_operation_table(lambda x, y: x * y)
