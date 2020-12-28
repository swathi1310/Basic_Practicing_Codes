for i in range(0, 7):
    for j in range(0, 7):
        if j == 0 or j == 6 or (i == j and j > 0):
            print("*", end="")
        else:
            print(end=" ")
    print(end="    ")
    for j in range(8, 14):
        if (j == 8 and (0 < i < 6)) or (j == 13 and (0 < i < 6)) or ((8 < j < 13) and (i == 0 or i == 6)):
            print("*", end="")
        else:
            print(end=" ")
    print(end="    ")
    for j in range(15, 22):
        if (j > 15 and i == 0) or (j == 15 and (i == 1 or i == 2)) or (j > 15 and i == 3) or (j == 21 and (i == 4 or i == 5)) or (j < 21 and i == 6):
            print("*", end="")
        else:
            print(end=" ")
    print(end="    ")
    for j in range(23, 30):
        if j == 23 or j == 29 or (j >= 23 and i == 3):
            print("*", end="")
        else:
            print(end=" ")
    print(end="    ")
    for j in range(31, 38):
        if j == 34 or (j >= 31 and (i == 0 or i == 6)):
            print("*", end="")
        else:
            print(end=" ")
    print()
