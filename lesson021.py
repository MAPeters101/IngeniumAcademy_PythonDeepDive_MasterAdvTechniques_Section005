def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


if __name__ == '__main__':
    infinite = infinite_sequence()
    print(next(infinite)) # 0
    print(next(infinite)) # 1

    for num in infinite:
        print(num)