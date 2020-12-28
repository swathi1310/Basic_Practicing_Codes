""" Kadane’s Algorithm
here we have to find max sum of corresponding numbers for example
in a list [1, 2, 3, -2, 5] the max number is 9 i.e, sum(1, 2, 3, -2, 5)
list [-1, -2, -3, -4] the max sum is -1
"""
"""t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sub_arr = []
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            sub_arr.append(arr[i:j])  # this is to make sublist
    _sum = list(map(sum, sub_arr))  # instead of this we can also use [sum(i) for i in zip(*sub_arr)]
    print(max(_sum))"""
t = int(input())  # other code
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    _sum = [arr[0]]
    for i in range(1, n):
        _sum.append(max(arr[i], _sum[i - 1] + arr[i]))
    print(max(_sum))
