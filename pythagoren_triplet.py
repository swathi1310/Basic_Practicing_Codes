for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split(",")]
    flag = 0
    for i in range(n - 2):
        for j in range(i+1, n - 1):
            for k in range(j+1, n):
                a = arr[i]*arr[i]
                b = arr[j]*arr[j]
                c = arr[k]*arr[k]
                if a + b == c or c + a == b or b + c == a:
                    flag = 1
                    break
    if flag == 1:
        print("Yes")
    else:
        print("No")
