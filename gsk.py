# remove consecutive letters from a string
t = int(input())
for _ in range(t):
    string = input()
    _str = ""
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i] != string[i - 1]:
                _str += string[i]
    if string[-1] != _str[-1] and string[-1] != string[-2]:
        _str += string[-1]
    print(_str)
# others
t = int(input())
while t > 0:
    t = t - 1
    s = input()
    while True:
        p = 0
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j != i + 1:
                s = s[:i] + s[j:]
                p = 1
            else:
                i += 1
        if p == 0:
            break
    print(s)
