t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()[:n]))
    sub_arr = []
    for i in range((n+k-1)//k):
        sub_arr1 = list(reversed(arr[i * k:(i + 1) * k]))
        sub_arr.extend(sub_arr1)
    print(sub_arr)
