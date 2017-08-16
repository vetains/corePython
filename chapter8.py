#-*- coding:utf-8 -*-
# # 8-2
# f=int(raw_input('from:'))
# t=int(raw_input('to:'))
# try:
#     i=int(raw_input('increment:'))
# except ValueError:
#     i=1
# def printrange(f,t,i):
#     print f,
#     while True:
#         f+=i
#         print f,
#         if f+i>=t:
#             print t,
#             break
# printrange(f,t,i)

# # 8-4 素数
# def isprime(n): #1不是素数
#     l=[]
#     if n!= 2 and n%2==0:
#         return False
#     else:
#         for i in range(1,n+1):
#             if n%i==0:
#                 l.append(i)
#     if l==[1,n]:
#         return True
#     else:
#         return False
# n=int(raw_input("inter:"))
# print isprime(n)

# # 8-5 约数
# def getfactors(n):
#     l=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             l.append(i)
#     for i in l:
#         print i,
# n=int(raw_input("inter:"))
# getfactors(n)

# # 8-6 素因子分解
def isprime(n): #如果是素数就返回True
    l=[]
    if n!=2 and n%2==0:
        return False
    else:
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
    if l==[1,n]:
        return True
    else:
        return False

def func(n):
    l=[]
    ##方法I
    # def in_func(n):
    #     if not isprime(n):
    #         for i in range(2,n+1):
    #             if isprime(i) and n%i==0:
    #                 l.append(i)
    #                 n=n/i
    #                 break
    #         in_func(n)
    #     elif isprime(n):
    #         l.append(n)
    #
    # if n==1:
    #     print 1
    # else:
    #     in_func(n)


    #方法II
    while True:
        if not isprime(n):
            for i in range(2,n+1):
                if isprime(i) and n%i==0:
                    n=n/i
                    l.append(i)
                    break
        elif isprime(n):
            l.append(n)
            break
    for i in l:
        print i,

n=int(raw_input('inter:'))
func(n)
