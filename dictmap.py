N = int(input())
d = dict()
count = 0

if N>=0 and N<=100000:
    for _ in range(0, N):
        name, number = input().split()
        d[name] = number

    while 1:
        try:
            key = input()
            if key in d:
                print("{}={}".format(key, d[key]))
            else:
                print("Not found")
        except:
            break
