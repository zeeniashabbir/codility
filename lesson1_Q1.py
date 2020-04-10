def solution(N):
    c,i,m=0,0,0
    list=[]
    binary_value=bin(N)
    binary_value=binary_value[2:]
    print(binary_value)
    l=len(binary_value)-1
    for i in range(l):
        if binary_value[i] =='1' and binary_value[i+1] =='0':
            c = 0
            while binary_value[i+1] =='0':
                c+=1
                i+=1
            list.append(c)
        else:
            pass
    #print(list)
    print(max(list))

s=solution(647)
