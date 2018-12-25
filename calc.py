from math import floor
x = 178794
y=225277
i=1
max = 1

p=floor(x/2)+1
q=floor(y/2)+1
while i<p and i<q:
    l = x%i
    l2 = y%i
    if l==0 and l2==0:
        max=i
    i=i+1

print(max)