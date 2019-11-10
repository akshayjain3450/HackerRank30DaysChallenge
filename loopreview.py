T = int(input())
if T < 1 and T > 10:
    exit()
else:
    for i in range(T):
        S = input()
        odd = ''
        even = ''
        for j in range(len(S)):
            if j % 2 == 0:
                odd = odd + S[j]
            else:
                even = even + S[j]
        print(odd,even)
