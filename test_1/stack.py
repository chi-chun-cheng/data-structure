def equalStacks(*args):
    H = [sum(args[0]), sum(args[1]), sum(args[2])]
    while H[0]!=H[1] or H[1]!=H[2]:
        m = min(H)
        for i in range(3):
            if H[i] > m:
                H[i]-=(args[i].pop(0))
    return H

def equalStacks(h1, h2, h3):
    # Write your code here
    s1,s2,s3 = map(sum, [h1,h2,h3])
    while not( s1==s2==s3 ):
        mx = max(s1, s2, s3)
        if s1 == mx:
            s1 -= h1[0]
            h1.pop(0)
        if s2 == mx:
            s2 -= h2[0]
            h2.pop(0)
        if s3 == mx:
            s3 -= h3[0]
            h3.pop(0)
    return s1    

def getMax(operations):
    L = []
    M = []
    for i in operations:
        op = i.split(" ")
        if op[0]=="1":
            L.append(int(op[1]))
        elif op[0]=="2":
            L.pop()
        else:
            M.append(max(L))
    return M


def getMax(operations):
    # Write your code here
    stack = []
    ans = []

    for op in operations:
        if op[0] == '1':
            num = int(op[1:])
            if len(stack) == 0:
                stack.append(num)
            else:
                stack.append(max(num, stack[-1]))
        elif op[0] == '2':
            stack.pop()
        else:
            ans.append(stack[-1])

    return ans