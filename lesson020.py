def count_uo_to(n):
    count = 1
    while count <= n:
        yield count # [1, 2, 3, 4, 5, 6]
        count += 1


