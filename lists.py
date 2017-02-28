list = []
cmd = int(input())

for i in range(0,cmd):
    inp = input().strip().split()
    if (inp[0] == "insert"):
        leng = int(inp[1])
        val = int(inp[2])
        list.insert(leng, val)
    elif (inp[0] == "print"):
        print (list)

    elif (inp[0] == "remove"):
        list.remove(int(inp[1]))

    elif (inp[0] == "append"):
        list.append(int(inp[1]))

    elif (inp[0] == "sort"):
        list.sort()

    elif (inp[0] == "pop"):
        list.pop(int(inp[1]))

    elif (inp[0] == "reverse"):
        list.reverse()


