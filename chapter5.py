#-*- coding:utf-8 -*-
# #5-2
# def add(x,y):
#     try:
#         return float(x)*float(y)
#     except BaseException,e:
#         return e
#
# x=raw_input('x:')
# y=raw_input('y:')
# print add(x,y)

# #5-3
# score=int(raw_input('Enter the score:'))
# if score>=90 and score<=100:
#     print 'A'
# elif score>=80 and score<=89:
# score=int(raw_input('Enter the score:'))
# if score>=90 and score<=100:
#     print 'A'
# elif score>=80 and score<=89:
#     print 'B'
# elif score>=70 and score<=79:
#     print 'C'
# elif score>=60 and score<=69:
#     print 'D'
# elif score>=0 and score<=59:
#     print 'F'
# else:
#     print 'Illegal inp
#     print 'B'
# elif score>=70 and score<=79:
#     print 'C'
# elif score>=60 and score<=69:
#     print 'D'
# elif score>=0 and score<=59:
#     print 'F'
# else:
#     print 'Illegal input'
#
# #5-4
# year=int(raw_input('Enter:'))
# def leapYear(year):
#     if year%4==0:
#
#         if year%100!=0:
#             return 'This is exactly a leap-year'
#         else:
#             if year%400==0:
#                 return 'This is exactly a leap-year'
#             else :
#                 return 'This year is not a leap-year'
#     else:
#         return 'This year is not a leap-year'
#
# print leapYear(year)

# #5-5
# sum=float(raw_input('Enter (such as 0.77):'))
#
# if sum%0.25!=0:
#     n1=int(sum//0.25)
#     sum=sum%0.25
#     if sum%0.10!=0:
#         n2=int(sum//0.10)
#         sum=sum%0.10
#         if sum%0.05!=0:
#             n3=int(sum//0.05)
#             sum=sum%0.05
#             n4=int(sum/0.01)
#         else:
#             n3=int(sum/0.05)
#             n4=0
#     else:
#         n2=int(sum/0.10)
#         n3=n4=0
# else:
#     n1=int(sum/0.25)
#     n2=n3=n4=0
#
# print 'give back %s枚$0.25,%s枚$0.10,%s枚$0.05,%s枚$0.01'%(n1,n2,n3,n4)

# #5-5有没有更好的方法：divoid(x,y)函数，返回x/y的商和余(商，余)
# sum=float(raw_input('Enter:'))
# (n1,sum)=divmod(sum,0.25)
# if sum!=0:
#     (n2,sum)=divmod(sum,0.10)
#     if sum!=0:
#         (n3,sum)=divmod(sum,0.05)
#         n4=sum/0.01
#     else:
#         n3=n4=0
# else:
#     n2=n3=n4=0
# print 'give back %s枚$0.25,%s枚$0.10,%s枚$0.05,%s枚$0.01'%(n1,n2,n3,n4)

# #5-6方法1.split()，输入时要有空格
# from string import split
# while True:
#     try:
#         equation=raw_input('Enter(example: a + b):')
#         aList=split(equation)
#         elem1=float(aList[0])
#         oper=aList[1]
#         elem2=float(aList[2])
#     except BaseException:
#         print 'Example: a(blank)+(blank)b'
#     else:
#         break
# if oper=='+':
#     print elem1+elem2
# elif oper=='-':
#     print elem1-elem2
# elif oper=='*':
#     print elem1*elem2
# elif oper=='/':
#     print elem1/elem2
# elif oper=='%':
#     print elem1%elem2
# elif oper=='**':
#     print elem1**elem2
# else:
#     print 'Illegal input'

# #5-6方法2 字符串方法 find
# from string import find
# while True:
#     equation=raw_input('Enter(example: a+b):')
#     operList=['+','-','*','/','%','**']
#     for oper in operList:
#         if equation.find(oper)!=-1: #如果没能找到字符，find会返回-1
#             n=equation.find(oper)
#             break
#         else:
#             n=-1
#             print "can't find %s"%oper
#     if n!=-1:
#         break
#     elif n==-1:
#         print 'input again'
#
# m=len(equation)
# if equation[n+1]=='*':
#     oper='**'
#     elem1=float(equation[0:n])
#     elem2=float(equation[n+2:])
# else:
#     elem1=float(equation[0:n])
#     elem2=float(equation[n+1:])
#
# if oper=='+':
#     print elem1+elem2
# elif oper=='-':
#     print elem1-elem2
# elif oper=='*':
#     print elem1*elem2
# elif oper=='/':
#     print elem1/elem2
# elif oper=='%':
#     print elem1%elem2
# elif oper=='**':
#     print elem1**elem2

# #5-8
# from math import pi
# def Szft(a):
#     return a*a
# def Vlft(a,b,c):
#     return a*b*c
# def Scircle(r):
#     return pi*r*r
# def Vball(R):
#     return (4/3.0)*pi*(R**3)
#
# a=float(raw_input('正方形的边长：'))
# print '正方形的面积:',Szft(a)
# lft=[]
# for i in ['长','宽','高']:
#     lft.append(float(raw_input('立方体的%s:'%i)))
# [x,y,z]=lft
# print '立方体的体积：',Vlft(x,y,z)
# r=float(raw_input('圆的半径：'))
# print '圆的面积为',Scircle(r)
# R=float(raw_input('球的半径：'))
# print '球的体积为',Vball(R)

# #5-10
# def transform(F):
#     C=(F-32)*(5/9.)
#     return C
# print transform(100)    #example

# #5-11
# print range(0,21,2)
# print range(1,20,2)
#
# def oddOrEven(num):
#     if num%2 is 0:
#         return 'even'
#     else:
#         return 'odd'
# num=int(raw_input('enter:'))
# print oddOrEven(num)
#
# def judge(devidend,devider):
#     if devidend%devider is 0:
#         return True
#     else:
#         return False

# #5-13
# def transform(time):
#     n=time.find(':')
#     l=len(time)
#     hour=int(time[0:n])
#     minute=int(time[n+1:])
#     return hour*60+minute
#
# time=raw_input('time:')
# print transform(time)

# #5-14
# def interest(principal,rate,destiny):
#     i=0
#     while i<destiny:
#         principal*=(1+rate)
#         i+=1
#     return principal
#
# print interest(10000,0.0001,365)

#5-15
# from time import clock
# def GCDivisor(m,n):     #Greatest common divisor
#     if cmp(m,n) is 1:   #如果m>n，cmp(m,n)会返回1,相等返回0,m<n返回1
#         m,n=n,m         #把m，n从小到达排列，则不再需要额外的min
#     aList=range(1,m)[::-1]  #从后往前找的方法
#     for i in aList:
#         if m%i==0 and n%i==0:
#             break
#     return i
#
#     # aList=range(1,m)      #从前往后找的方法
#     # for i in aList:
#     #     if m%i==0 and n%i==0:
#     #         max=i
#     # return max
#
# def LCMultiple(m,n):    #Least common multiple
#     i=int(GCDivisor(m,n))
#     return m*n/i        #LCM=(m/i)*(n/i)*i=m*n/i
#
# start1=clock()
# m=66666;n=66665
# print '最大公约数：',GCDivisor(m,n)
# start11=clock()
# print '耗时'+str((start11-start1)*1000)+'ms'
#
# #辗转相除法:两数中的最小数，和两数相除所得的余数的最大公约数，为两数的最大公约数
# def ZZDivisor(m,n):
#     if cmp(m,n) is 1:
#         m,n=n,m     #m小n大
#     q=1
#     while q!=0:
#         q=n%m       #q为两数余数
#         n=m         #m比余数大，让m成为被除数
#         m=q         #余数小，做除数
#                     #一直循环到余数为零，此时被除数是最大公约数
#     return n
#
# start2=clock()
# m=9876543210;n=988543214
# print '最大公约数：',ZZDivisor(m,n)
# start22=clock()
# print '耗时'+str((start22-start2)*1000)+'ms'
#
# #更相减损法：先判断两数是否同时为偶数，是则都除2,直到不是偶数；
# #两数相减得差，用小数与差相减得差，再次用小数与差相减...直到所得差为0
# #最大公约数等于差为0的数乘上约掉的若干个2
# def JSDivisor(m,n):
#     i=0
#     while m%2==0 and n%2==0:
#         m/=2
#         n/=2
#         i+=1
#     q=1
#     if cmp(m,n) is 1:
#         m,n=n,m     #m小n大
#     while q!=0:
#         q=n-m
#         if cmp(m,q) is 1:   #最后一步，q=0，m比q大
#             m,n=q,m     #最后一步，m=q=0,值在n上
#         else:
#             m,n=m,q
#
#     return  n*(2**i)
#
# start3=clock()
# m=9876543210;n=988543214
# print '最大公约数：',JSDivisor(m,n)
# start33=clock()
# print '耗时'+str((start33-start3)*1000)+'ms'      #更相减损法总不如辗转相除法快

#5-16
# remaining={}
# def getPaid(i,payment,balance):
#     remaining[str(i)+'p']=payment
#     remaining[str(i)+'b']=balance
#
# i=0
# ob=float(raw_input('Enter opening balance:'))
# mp=float(raw_input('Enter monthly payment:'))
# getPaid(i,mp,ob)
#
# print "\n Enter '.' to quit\n"
#
# while True:
#     payment=raw_input('Enter monthly payment:')
#     if payment=='.':
#         break
#     i+=1
#     payment=float(payment)
#     balance=remaining[str(i-1)+'b']-payment
#     getPaid(i,payment,balance)
#
# print
# print ' '*5+'Amount Remaining'
# print 'Pymt#'+'  '+'Paid'+' '*5+'Balance'
# print '-'*5+  '  '+'-'*6 +' '*3 +'-'*9
# for x in range(i+1):
    # print x,' '*5+'$',remaining[str(x)+'p'],' '*3+'$',remaining[str(x)+'b']

# # 5-17
# from random import *
# N=randint(2,100)    #N=randrange(2,101)
# NList=[]
# for i in range(N):
#     NList.append(randint(0,(2**31)-1))   #NList.append(randrange(2**31))
# N2=randint(2,N)
# N2List=[]
# for i in range(N2):
#     N2List.append(choice(NList))
# print N2List
