t = int(input())
for _ in range(t):
    string = input()
    string_rev = string[::-1]
    flag = 0
    cnt = 0
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            if string[i:] == string_rev[i:j]:
                print(string[i:])
                flag = 1
                break
            else:
                cnt = 1
    if cnt == 1 and flag == 0:
        print(string[0])  # vnrtysfrzrmzlygfv
