n = int(input())
bu = []
values = []
for i in range(n):
    value = list(map(str, input().split()))
    buy = {'id': 0, 'type': 'xx', 'name': 'aa', 'price': 0, 'quantity': 0}
    if value[1] == 'Buy':
        buy['id'] = int(value[0])
        buy['type'] = str(value[1])
        buy['name'] = str(value[2])
        buy['price'] = int(value[3])
        buy['quantity'] = int(value[4])
        bu.append(buy)
    values.append(value)
res = [[key for key in bu[0].keys()], *[list(idx.values()) for idx in bu]]
cnt = 0
cn = 0
for j in range(n):
    for k in range(1, len(res)):
        if values[j][2] == res[k][2] and values[j][1] != 'Buy':
            if int(values[j][3]) <= res[k][3] and int(values[j][4]) <= res[k][4]:
                print("{}:{}".format(values[j][2], values[j][3]))
                cn = 1
                break
            else:
                cnt = 1
                break
        else:
            cnt = 1
            break
if cnt == 1 and cn != 1:
    print("Stocks not traded")