"""t = int(input())
for _ in range(t):
    n = int(input())
    ele = list(map(int, input().split()[:n]))
    _max = 0
    flag = 0
    for i in ele:
        cnt = ele.count(i)
        ele = list(filter(lambda x: x != i, ele))
        if cnt > _max and cnt > n/2:
            _max = cnt
            flag = 1
    if flag == 1:
        print(i)
    else:
        print("-1")"""
test = int(input())
for z in range(test):
    size = int(input())
    arr = list(map(int, input().split()))
    s = set(arr)
    d = {}
    for i in s:
        d[i] = 0
    for i in arr:
        d[i] += 1
    a = -1
    for i in d.keys():
        if d.get(i) > size // 2:
            a = i
    print(a)
