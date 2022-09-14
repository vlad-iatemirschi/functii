print('prob 1')
def putere(x,y):
    return x**y

print("S=1+...=",1+putere(0.5,2)+putere(0.5,4)+putere(0.5,6)+putere(0.5,8))

print('operatia factorial')

n=int(input("Introdu n: "))
m=int(input("Introdu m: "))
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return int(fact)
C=factorial(n)/(factorial(m)*factorial(n-m))
print(C)

print('inmultirea fractiilor')

a,b=int(input('prima fractie: ')),int(input(' '))
c,d=int(input('a doua fractie: ')),int(input(' '))
def i(x,y,z,w):
    i=x*z
    j=y*w
    return i,j
print(a,'/',b,'*',c,'/',d,'=',i(a,b,c,d))

print('adunarea fractiilor')

a,b=int(input('prima fractie: ')),int(input(' '))
c,d=int(input('a doua fractie: ')),int(input(' '))
def a(x,y,z,w):
    i=(x*w)+(z*y)
    j=y*w
    return (i,j)
print(a,'/',b,'+',c,'/',d,'=',a(a,b,c,d))

