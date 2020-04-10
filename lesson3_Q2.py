
def solution(a):
    a.sort()
    #print(a)
    tmp,t,next=0,0,0
    list=[]
    list1 = []
    elem=0
    for i in range(len(a)-1):
        next=a[i+1]
        tmp=a[i]+1
        if next==a[i]:
            pass
        if tmp==a[i+1]:
            pass
        else:
            t=tmp
            list.append(tmp)
    print(min(list))

solution([1,2,3,4,5,7,6,9,11])