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
# def isprime(n): #如果是素数就返回True
    # l=[]
    # if n!=2 and n%2==0:
    #     return False
    # else:
    #     for i in range(1,n+1):
    #         if n%i==0:
    #             l.append(i)
    # if l==[1,n]:
    #     return True
    # else:
    #     return False
#
# def func(n):
#     l=[]
#     ##方法I
#     # def in_func(n):
#     #     if not isprime(n):
#     #         for i in range(2,n+1):
#     #             if isprime(i) and n%i==0:
#     #                 l.append(i)
#     #                 n=n/i
#     #                 break
#     #         in_func(n)
#     #     elif isprime(n):
#     #         l.append(n)
#     #
#     # if n==1:
#     #     print 1
#     # else:
#     #     in_func(n)
#
#
#     #方法II
    # while True:
    #     if not isprime(n):
    #         for i in range(2,n+1):
    #             if isprime(i) and n%i==0:
    #                 n=n/i
    #                 l.append(i)
    #                 break
    #     elif isprime(n):
    #         l.append(n)
    #         break
    # for i in l:
    #     print i,
#
# n=int(raw_input('inter:'))
# func(n)

# 8-7  完全数  6=3+2+1=3*2*1
# def isprime(n):
#     l=[]
#     if n!=2 and n%2==0:
#         return False
#     else:
#         for i in range(1,n+1):
#             if n%i==0:
#                 l.append(i)
#     if l==[1,n]:
#         return True
#     else:
#         return False
#
# def func(n):
#     l=[]
#     while True:
#         if not isprime(n):
#             for i in range(2,n+1):
#                 if isprime(i) and n%i==0:
#                     n=n/i
#                     l.append(i)
#                     break
#         elif isprime(n):
#             l.append(n)
#             break
#     l.append(1)     #题目的定义里约数包括1
#     return l
#
# def isperfect(n):
#     l=func(n)
#     sum=0
#     for i in l:
#         sum+=i
#     if sum==n:
#         return True
#     else:
#         return False
#
# n=int(raw_input('Inter:'))
# print isperfect(n)

# # 8-8 阶乘
# def factorial(N):
#     sum=1
#     for i in range(1,N+1):
#         sum*=i
#     return sum
# N=int(raw_input('Inter:'))
# print factorial(N)

# # 8-9 斐波那契数列
# def Febo(n):
#     l=[1,1]
#     i=1
#     while len(l)<n:             #当斐波那契数列长度不足时
#         l.append(l[i]+l[i-1])   #增加至所需长度
#         i+=1
#     return l[n-1]
#
# print Febo(8)
#
# #递归方法产生斐波那契数列
# def febo(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return febo(n-1)+febo(n-2)  #递归的核心算法，当前数字等于上一个加上上上个数字
#
# for n in range(10):
#     print febo(n)

# # 8-10 文本处理
# import string
# txtfile=open('/home/vetains/pywork/pycore/8-10.txt','r')
# txtlist=txtfile.readlines()
# txtfile.close()
# fuList=list(string.letters)
# yuanList=['a','e','i','o','u','A','E','I','O','U']
# for eachelem in yuanList:
#     fuList.remove(eachelem)
# sum=0
# yuan=0
# fu=0
# for eachN in txtlist:
#     lettersList=eachN.split(' ')
#     sum+=len(lettersList)
#     for eachletter in lettersList:
#         for i in range(len(eachletter)):
#             if eachletter[i] in fuList:
#                 fu+=1
#             elif eachletter[i] in yuanList:
#                 yuan+=1
# print('''单词总数：%i
# 元音总数：%i
# 辅音总数：%i'''%(sum,yuan,fu))

# 8-12 各种进制
setASCII=set([x for x in range(33,127)])    #ASCII(33~126)
print '-'*10
begin=int(raw_input('输入起始值：'))
end=int(raw_input('输入结束值：'))
setBE=set([x for x in range(begin,end+1)])
#
# def inASCII(setBE,setASCII):
#     for i in setASCII&setBE:
#         DEC=i
#         BIN=bin(i)
#         OCT=oct(i)
#         HEX=hex(i)
#         ASC=chr(i)
#         print '%i         %s       %s        %s      %s' %(DEC,BIN,OCT,HEX,ASC)


def EZ(begin,end):
    for i in range(begin,end):
        DEC=i
        BIN=bin(i)
        OCT=oct(i)
        HEX=hex(i)
        if i<33 or i>126:   #直接在这里处理i是否在ASCII内就好
            print '%i         %s       %s        %s ' %(DEC,BIN,OCT,HEX)
        else:
            ASC=chr(i)
            print '%i         %s       %s        %s      %s' %(DEC,BIN,OCT,HEX,ASC)


if setBE&setASCII==set([]):  #如果BE和ASC交集为空
    print '十进制    二进制    八进制    十六进制  '
    print '-'*48
    EZ(begin,end+1)
    print '-'*48
else:                       #BE和ASC交集不为空
    print '十进制    二进制    八进制    十六进制   ASCII'
    print '-'*48
    EZ(begin,end+1)
    # if begin<33 and end>133:      #不用在这里展开繁杂的讨论
    #     outASCII(begin,33)
    #     inASCII(setBE,setASCII)
    #     outASCII(133,end+1)
    # elif begin>=33 and end=<133:
    #     inASCII(setBE,setASCII)
    # elif begin<33 and end<133:
    #     outASCII(begin,33)
    #     inASCII(setBE,setASCII)
    # elif begin>33 and end>133:
    #     inASCII(setBE,setASCII)
    #     outASCII(133,end)
    # else:
    #     print '?'
    print '-'*48
