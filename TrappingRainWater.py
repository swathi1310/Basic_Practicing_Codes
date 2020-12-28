t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    fmax = arr[0]
    lmax = max(arr[1:])
    unit = 0
    for i in range(n):
        if arr[i] > fmax:
            fmax = arr[i]
        if arr[i] == lmax and i < n-1:
            lmax = max(arr[i + 1:])
        capacity = min(fmax, lmax)
        trap = max(capacity - arr[i], 0)
        unit += trap
    print(unit)
"""for _ in range(int(input())): #  other code
    n=int(input())
    a=list(map(int,input().split()))
    lmax=a[0]
    rmax=max(a[1:])
    count=0
    for i in range(n):
        if(a[i]>lmax):
            lmax=a[i]
        if(a[i]==rmax and i<n-1):
            rmax=max(a[i+1:])
        h=min(lmax,rmax)
        count+=max(h-a[i],0)
    print(count)"""
