N = int(input())
    a,b=[],[]
    for i in range(0,N):
        a.append(input().split())
        if a[i][0]=="insert":
            b.insert(int(a[i][1]),int(a[i][2]))
            if b.index(int(a[i][2]))==a[i][1]:
                b.remove(int(a[i][2]))
        elif a[i][0]=="print":
            print(b)
        elif a[i][0]=="remove":
            b.pop(b.index(int(a[i][1])))
        elif a[i][0]=="append":
            b.append(int(a[i][1]))
        elif a[i][0]=="sort":
            b.sort()
        elif a[i][0]=="pop":
            b.pop()
        elif a[i][0]=="reverse":
            b.reverse()
