a = [1,2,3,4,5]

N = len(a)

n = 2

new_a = [None for i in range(N)]
print(a,new_a)

for i in range(N):
    print((i+n)%N)
    new_a[(i+1)%N] = a[i]
    print(new_a)

for n in range(5):
    print(a[-n:] + a[:-n])