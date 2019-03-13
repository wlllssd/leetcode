res = []
def fx(a,begin,end):
    if begin == end:
        res.append(a.copy())
    else:
        for i in range(begin,end):
            a[i],a[begin] = a[begin],a[i]
            fx(a,begin+1,end)
            a[begin],a[i] = a[i],a[begin]
def A(N):
    a = [i for i in range(1,N+1)]
    fx(a,0,N)

A(3)
print(res)
print(len(res))