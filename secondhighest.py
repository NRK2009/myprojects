if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if n>11 or n < 2:
        print("Value of n is wrong. (n>11 and n < 2)")
        exit(0)
    to_list = list(set(list(arr)))
    for i in to_list:
        if i > 100 or i < -100:
            print("Input is wrong. (-100 <= A[i] <= 100)")
            exit(0)
    to_list.sort()
    to_list.reverse()
    print(to_list[1])
