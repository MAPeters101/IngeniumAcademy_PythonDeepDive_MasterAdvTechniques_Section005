def count_up_to(n):
    count = 1
    while count <= n:
        yield count # [1, 2, 3, 4, 5, 6]
        count += 1


if __name__ == '__main__':
    counter = count_up_to(5)
    # print(counter[3])
    print(next(counter)) # 1
    print(next(counter)) # 2

    for num in counter: # 3, 4, 5
        print(num)

    for num in counter: # Nothing generator
        print(num)


