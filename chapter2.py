#-×- coding:utf-8 -*-
# # 2-1
# aName='Hello world!'
# announce='I\'m vetains'
# print aName
# print announce
# print '%s %s'%(aName,announce)
#

# #2-2
# #!/usr/bin/env python
# a=1+2*4
# print a

# #2-4
# s=raw_input('enter your name:')
# m=raw_input('enter your age:')
# print 'your name is %s'%s
# print 'your age is %d'%(int(m))

# #2-5
# i=0
# while i<11:
#     print i
#     i+=1
# print
# for i in range(11):
#     print i

# #2-6
# e=int(input('enter a number:'))
# if e>0:
#     print 'your number>0'
# elif e==0:
#     print 'your number=0'
# else:
#     print 'your number<0'

# #2-7
# s=str(raw_input('enter your string:'))
# i=0
# while i<len(s):
#     print s[i],
#     i+=1
# print
# for i in range(len(s)):
#     print s[i],

# #2-8
# list1=[1,3,5,1,5]
# i=0
# sum=0
# while i<len(list1):
#     sum+=list1[i]
#     i+=1
# print sum
# print
# sum=0
# for i in range(len(list1)):
#     sum+=list1[i]
# print sum
#
# userList=[]
# n=int(raw_input('enter your length of list:'))
# for i in range(n):
#     userList.append(int(raw_input('enter your number(%d/%d):'%(i+1,n))))
#
# sum=0
# for i in range(n):
#     sum+=userList[i]
# print sum
#
# i=0
# userList=[]
# while i<n:
#     userList.append(int(raw_input('enter your number(%d/%d)'%(i+1,n))))
#     i+=1
# sum=0
# i=0
# while i<n:
#     sum+=userList[i]
#     i+=1
# print sum

# #2-9
# n=int(raw_input('how many nmbers?'))
# print
# userList=[]
# sum=0.0
# for i in range(n):
#     elem=float(raw_input('enter for list(%d/%d):'%((i+1),n)))
#     userList.append(elem)
#     sum=sum+elem
# average=sum/n
# print average

# #2-10
# test=True
# while test:
#     try:
#         elem=int(raw_input('enter a number betwenn 1~100:'))
#         if elem>0 and elem<101:
#             print 'good job!'
#             test=False
#         else:
#             print 'try again'
#     except:
#         print 'try again'
#         continue

# #2-11
# from sys import exit
#
# def adding(list=[]):
#     sum=0
#     for i in range(len(list)):
#         sum=sum+list[i]
#     return sum
# def average(list=[]):
#     n=float(len(list))
#     sum=adding(list)
#     return sum/n
# def creatList(n=5):
#     list=[]
#     for i in range(n):
#         list.append(float(raw_input('enter your number(%d/%d)'%((i+1),n))))
#     return list
#
# def main():
#     print '*'*20
#     print 'MENU:'
#     print 'A:取五个数的平均值'
#     print 'B:取五个数的和'
#     print 'X:退出'
#     print '*'*20
#     Control=str((raw_input('enter your choice:')))
#     Control.lower()
#     if Control=='x':
#         exit()
#     elif Control=='a':
#         aList=creatList(5)
#         Average=average(aList)
#         print '平均值为：',Average
#         print
#         main()
#     elif Control=='b':
#         aList=creatList(5)
#         sum=adding(aList)
#         print '所求和为：',sum
#         print
#         main()
#     else:
#         print 'try again'
#         print
#         main()
#
# if __name__=='__main__':
#     main()

# #2-15
# alist=[]
# for i in range(3):
#     alist.append(float(raw_input('enter your number(%d/3):'%(i+1))))
# a=alist[0]
# b=alist[1]
# c=alist[2]
# '''从小到大排序'''
# if a>b:
#     a,b=b,a
# if b>c:
#     b,c=c,b
# if a>b:
#     a,b=b,a
# blist=[a,b,c]
# print blist

# #2-16
# FFF=open('/home/vetains/pywork/pycore/chapter2.py','r')
# for eachLine in FFF:
#     print eachLine
# FFF.close()

def main():
    main.__doc__='''take a try at main.__doc__'''
    pass

main()
