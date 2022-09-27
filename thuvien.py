#xoay mảng
import collections
a_list = collections.deque([1, 2, 3, 4, 5])
a_list.rotate(2)
shifted_list = list(a_list)
print(shifted_list)

#in ra bảng chữ cái
import string
chucaithuong = string.ascii_lowercase
chuhoa = string.ascii_uppercase
kitudacbiet = string.punctuation

#chèn 1 số vào mảng mà vẫn giữ nguyên theo thứ tự tăng dần
import bisect
a = [1,4,6,8,12,15,20]
position = bisect.bisect(a,13)
print(position)
a.insert(position,13)
print(a)

#tìm ước chung lớn nhất
import math
print(math.gcd(*mangcanthay))

#tim bội chung lớn nhất
import math
print(math.lcm(*mangcanthay))
// hoac
from functools import reduce
def test(nums):
    return reduce(lambda x,y:lcm(x,y),nums)
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b // gcd(a, b)
print(test(mangcanthay))

#hoán vị
import itertools
print(list(itertools.permutations([1, 2, 3])))

#prefix sum
from itertools import accumulate
mang = [2,5,6,8]
print ([0]+list(accumulate(mang)))

#loai bo nhung chu giong nhau va canh nhau
mang = [mang[i] for i in range(len(mang)) if (i==0) or mang[i] != mang[i-1]]

#de quy quay lui
n = 3
x = n*[0]
def fine_print(x):
   tmp = '' 
   for i in x:
       for j in range():
          tmp += str(i)
   return tmp
def bin_gen(i):
   for j in range(0,2):
      x[i] = j
      if i == n-1:
         print(fine_print(x))
      else:
         bin_gen(i+1)
bin_gen(0)

#sàng nguyên tố
a,b = map(int,input().split())
Primes = [0] * (10**6)
def SieveOfEratosthenes(n) :
     
    Primes[0] = 1
    i = 3
    while(i*i <= n) :
        if (Primes[i // 2] == 0) :
            for j in range(3 * i, n+1, 2 * i) :
                Primes[j // 2] = 1
        i += 2
n = 10**6
SieveOfEratosthenes(n)
socankiemtra = 999976
if (socankiemtra == 2) :
    print(True)
elif(socankiemtra % 2 == 1 and Primes[socankiemtra // 2] == 0) :
    print(True)
else :
    print(False)

#chuyen toan bo mang ve int or str
print(list(map(int,["1","2"])))

#in ra tap con
from itertools import combinations
comb = combinations([1, 2, 3], 2)
for i in list(comb):
    print (i)
    
#loc cac phan tu 
vao = [s for s in vao if s != "null"]

#dien tich cua tam giac tao boi 3 diem
dientich = 1/2 * (x1 * (y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2 ))
dientichdagiacndinh= | 1/2 [(x1*y2 + x2*y3 +… + x(n-1)*y(n) + x(n) y1 ) -(x2*y1 + x3*y2 +… + x(n)*y(n-1) + x1*y(n))] |
k = [s for s in range(1,4)]

#chia cac chuoi giong nhau dung canh nhau
from itertools import groupby
test_str = 'ggggffggisssbbbeessssstt'
res = ["".join(group) for ele, group in groupby(test_str)]
print("Consecutive split string is : " + str(res))

#chia chuỗi thành subword cạnh nhau
def combos(s):
  if not s:
    return
  yield (s,)
  for i in range(1, len(s)):
    for c in combos(s[i:]):
      yield (s[:i],) + c
for c in combos('Bang'):
  print(c)

# tim tap giao
X = set([1, 3, 5, 7]) 
Y = set([2, 3, 5, 8]) 
print(X.intersection(Y))

#phần bù

set1 = {"A", "B", "C", "D"}
set2 = {"C", "D", "E", "F"}

print(set1 ^ set2)
#>> {'F', 'B', 'E', 'A'}
print(set1.symmetric_difference(set2))
#>> {'F', 'B', 'E', 'A'}

#mo xoa file
import os
script = os.path.dirname(__file__)
inp = os.path.join(script,"C:/Users/admin/Desktop/in.inp.txt")
with open(inp, "r") as in_file:
     print(in_file.read())


mo = open("C:/Users/admin/Desktop/in.inp.txt","r")
dong = open("C:/Users/admin/Desktop/out.inp.txt","w")
dulieu = mo.readline().split()
dong.write(1)

#tinh thoi gian chuong trinh dang chay
import time
start = time.time()
end = time.time()
print(end-start)

#setup graph và bfs
import os
from collections import defaultdict 
script_dir = os.path.dirname(__file__)
in_file = os.path.join(script_dir,'BAI1.INP.txt')
out_file = os.path.join(script_dir, 'BAI1.OUT.txt')
mang = []
with open(in_file,'r') as in_f:
     n,m = map(int,in_f.readline().split())
     x,y,z,t = map(int,in_f.readline().split())
     graph = defaultdict(list)
     for i in range(n) :
        k = list(map(int,in_f.readline().split()))
        for j in range(len(k)):
            graph[k[j]].append([i,j])
        mang.append(k)
for i in graph :
    print(i,graph[i])
time = 0 
path = [[x-1,y-1,time]]
come = [[0,0]]
while path != [] :
    x,y,time = map(int,path[0])
    print(path)
    if x+1 <= len(mang) -1 and mang[x+1][y] != 0 and [x+1,y] not in come:
        path.append([x+1,y,time+1])
        come.append([x+1,y])
        for i in graph[mang[x][y]] :
            if i not in come :
                path.append([x+1,y,time+1])
        if x+1 == z-1 and y == t-1 :
            break
    if y+1 <= len(mang[0]) -1 and mang[x][y+1] != 0 and [x,y+1] not in come:
        path.append([x,y+1,time+1])
        come.append([x,y+1])
        if x == z-1 and y+1 == t-1 :
            break
    if x-1 != -1 and mang[x-1][y] != 0 and [x-1,y] not in come:
        path.append([x-1,y,time+1])
        come.append([x-1,y])
        if x-1 == z-1 and y == t-1 :
            break
    if y-1 != -1 and mang[x][y-1] != 0 and [x,y-1] not in come:
        path.append([x,y-1,time+1])
        come.append([x,y-1])
        if x == z-1 and y-1 == t-1 :
            break
    del path[0]
print(come)
with open(out_file,'w') as out_f:
    out_f.write(str(tong))

#vidu ve prefix sum
from itertools import accumulate
for g in range(int(input())):
    n, k = map(int, input().split())
    s = str(input())
    a= []
    for i in s :
        if i == 'W':
            a.append(1)
        else :
            a.append(0)
    a=[0]+list(accumulate(a))
    mang = []
    print(a)
    for i in range(n - k + 1):
        mang.append(a[i + k] - a[i])
    print(mang)
    print(min(mang))

#Vị trí tương đối giữa hai đường thẳng 
d1: a1x + b1y = c1
d2: a2x + b2y = c2
Ta tính các định thức:
D = a1*b2 - a2*b1; 
Dx = c1*b2 - c2*b1; 
Dy = a1*c2 - a2*c1.
Nếu (D = 0) và (Dx = 0) và (Dy = 0) thì d1 và d2 trùng nhau;
Nếu a1*a2 + b1*b2 =0 thì d1 vuông d2
Nếu (D =0) và ((Dx <> 0) hoặc (Dy <> 0)) thì d1 song song với d2;
Nếu D <> 0 thì hai đường thẳng cắt nhau tại x=Dx/D; y=Dy/D

#Phương trình đường thẳng đi qua hai điểm A(x1,y1), B(x2,y2)
(y1 - y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0

#Cho 3 điểm phân biệt A(x1,y1), B(x2,y2), M(x3,y3) cùng nằm trên một đường thẳng, xét M có nằm giữa A, B hay không?
Điều kiện là: (x1 - x3)(x3 - x2) >0 hoặc (y1 - y3)(y3 - y2) > 0

# Khoảng cách từ một điểm M(x0,y0) đến đường thẳng d có phương trình tổng quát ax + by + c = 0
h = abs(ax0+by0+c)/(a**2 + b**2)**(1/2)

#Khoảng cách giữa 2 điểm A(x1,y1), B(x2,y2) trong mặt phẳng
d = ((x1-x2)**(2) + (x1-x2)**(2))**(1/2)

#sàng tìm thừa số của 1 số
import math as mt

MAXN = 100001
spf = [0 for i in range(MAXN)]
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i
 
def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
 
    return ret
sieve()
#socantim thua so 
x = 12246
print("prime factorization for", x, ": ",
                                end = "")
 
p = getFactorization(x)
 
for i in range(len(p)):
    print(p[i], end = " ")