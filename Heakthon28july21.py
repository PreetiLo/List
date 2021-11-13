import random
i = 1
name = ""
helper = []
number_of_com = 0
win_0 = []
win_1 = []
win_2 = []
win_3 = []
win_4 = []
win_5 = []
win_6 = []
win_7 = []
win_8 = []
win_9 = []
win_10 = []
print ("Welcome to the Swiss Round Calculator. This project was made by Enes Kristo")
number_of_com = int(input("Please enter the number of the competitors:\n"))
if number_of_com <= 16:
    loop = 3
elif number_of_com <= 32:
    loop = 4
elif number_of_com <= 64:
    loop = 5
elif number_of_com <= 128:
    loop = 6
elif number_of_com <= 256:
    loop = 7
elif number_of_com <= 512:
    loop = 8
elif number_of_com <= 1024:
    loop = 9
else:
    loop = 10
while i <= number_of_com:
    name = str(input("Name of competitor nr."+str(i)+":\n"))
    helper.append([name, 0, 0])
    i += 1
def odd():
    b = 0
    while b <= (number_of_com - 2):
        helper_1 = helper[b]
        b += 1
        helper_2 = helper[b]
        print ("Player " + str(helper_1[0]) + " is vs player " + str(helper_2[0]) + ".")
        b += 1
    helper_3 = helper[(number_of_com-1)]
    print (str(helper_3[0])+" gets a free win.")
    helper_3[1] += 1
    helper[(number_of_com-1)] = helper_3
    b = 0
    while b <= (number_of_com - 2):
        helper_1 = helper[b]
        b += 1
        helper_2 = helper[b]
        print("In the match between player " + str(helper_1[0]) + " and player " +str(helper_2[0]) + " who won?")
        a = int(input("Enter 1 if player " + str(helper_1[0]) + " won or 2 if player " + str(helper_2[0]) + " won.\n"))
        if a == 1 or a == 2:
            if a == 1:
                helper_1[1] += 1
                helper_2[2] += 1
                b -= 1
                helper[b] = helper_1
                b += 1
                helper[b] = helper_2
            else:
                helper_1[2] += 1
                helper_2[1] += 1
                b -= 1
                helper[b] = helper_1
                b += 1
                helper[b] = helper_2
        else:
            print("Enter a correct number.")
            b -= 1
            continue
        b += 1
    random.shuffle(helper)
    v = 0
    while v < number_of_com:
        helper_1 = helper[v]
        if helper_1[1] == 0:
            win_0.append(helper_1)
        elif helper_1[1] == 1:
            win_1.append(helper_1)
        elif helper_1[1] == 2:
            win_2.append(helper_1)
        elif helper_1[1] == 3:
            win_3.append(helper_1)
        elif helper_1[1] == 4:
            win_4.append(helper_1)
        elif helper_1[1] == 5:
            win_5.append(helper_1)
        elif helper_1[1] == 6:
            win_6.append(helper_1)
        elif helper_1[1] == 7:
            win_7.append(helper_1)
        elif helper_1[1] == 8:
            win_8.append(helper_1)
        elif helper_1[1] == 9:
            win_9.append(helper_1)
        elif helper_1[1] == 10:
            win_10.append(helper_1)
        v += 1
    random.shuffle(win_0)
    random.shuffle(win_1)
    random.shuffle(win_2)
    random.shuffle(win_3)
    random.shuffle(win_4)
    random.shuffle(win_5)
    random.shuffle(win_6)
    random.shuffle(win_7)
    random.shuffle(win_8)
    random.shuffle(win_9)
    random.shuffle(win_10)
    while len(helper) > 0:
        helper.pop()
    helper.append(win_10)
    helper.append(win_9)
    helper.append(win_8)
    helper.append(win_7)
    helper.append(win_6)
    helper.append(win_5)
    helper.append(win_4)
    helper.append(win_3)
    helper.append(win_2)
    helper.append(win_1)
    helper.append(win_0)
def even():
    b = 0
    while b <= (number_of_com - 2):
        helper_1 = helper[b]
        b += 1
        helper_2 = helper[b]
        print ("Player " + str(helper_1[0]) + " is vs player " +str(helper_2[0]) + ".")
        b += 1
    b = 0
    while b <= (number_of_com - 2):
        helper_1 = helper[b]
        b += 1
        helper_2 = helper[b]
        print("In the match between player " + str(helper_1[0]) + " and player " +str(helper_2[0]) + " who won?")
        a = int(input("Enter 1 if player " + str(helper_1[0]) + " won or 2 if player " + str(helper_2[0]) + " won."))
        if a == 1 or a == 2:
            if a == 1:
                helper_1[1] += 1
                helper_2[2] += 1
                b -= 1
                helper[b] = helper_1
                b += 1
                helper[b] = helper_2
            else:
                helper_1[2] += 1
                helper_2[1] += 1
                b -= 1
                helper[b] = helper_1
                b += 1
                helper[b] = helper_2
        else:
            print("Enter a correct number.")
            b -= 1
            continue
        b += 1
        random.shuffle(helper)
        v = 0
    while v < number_of_com:
        helper_1 = helper[v]
        if helper_1[1] == 0:
            win_0.append(helper_1)
        elif helper_1[1] == 1:
            win_1.append(helper_1)
        elif helper_1[1] == 2:
            win_2.append(helper_1)
        elif helper_1[1] == 3:
            win_3.append(helper_1)
        elif helper_1[1] == 4:
            win_4.append(helper_1)
        elif helper_1[1] == 5:
            win_5.append(helper_1)
        elif helper_1[1] == 6:
            win_6.append(helper_1)
        elif helper_1[1] == 7:
            win_7.append(helper_1)
        elif helper_1[1] == 8:
            win_8.append(helper_1)
        elif helper_1[1] == 9:
            win_9.append(helper_1)
        elif helper_1[1] == 10:
            win_10.append(helper_1)
        v += 1
    random.shuffle(win_0)
    random.shuffle(win_1)
    random.shuffle(win_2)
    random.shuffle(win_3)
    random.shuffle(win_4)
    random.shuffle(win_5)
    random.shuffle(win_6)
    random.shuffle(win_7)
    random.shuffle(win_8)
    random.shuffle(win_9)
    random.shuffle(win_10)
    while len(helper) > 0:
        helper.pop()
    helper.append(win_10)
    helper.append(win_9)
    helper.append(win_8)
    helper.append(win_7)
    helper.append(win_6)
    helper.append(win_5)
    helper.append(win_4)
    helper.append(win_3)
    helper.append(win_2)
    helper.append(win_1)
    helper.append(win_0)
if number_of_com % 2 == 0:
    c = 1
    while c <= loop:
        even()
        c += 1
else:
    c = 1
    while c <= loop:
        odd()
        c += 1 