# #!/usr/bin/env python
# #-*- coding:utf-8 -*-
#
# #例11.1
# from operator import add,sub
# from random import choice,randint
#
# ops={'+':add,'-':sub}
# MaxTries=2
#
# def doprob():
#     op=choice('+-')
#     nums=[randint(1,10) for i in range(2)]  #获得一个列表，表中有两个随机数
#     nums.sort(reverse=True)
#     answer=ops[op](*nums)
#     pr='%d %s %d='%(nums[0],op,nums[1])
#     oops=0
#     while True:
#         try:
#             if int(raw_input(pr))==answer:
#                 print 'correct'
#                 break
#             if oops==MaxTries:
#                 print 'answer\n%s %d'%(pr,answer)
#             else:
#                 print 'incorrect...try again'
#                 oops+=1
#         except (KeyboardInterrupt,EOFError,ValueError):
#             print 'invalid input...try again'
#
# def main():
#     while True:
#         doprob()
#         try:
#             opt=raw_input('Again?[Y/n]').lower()
#             if opt and opt[0]=='n':
#                 break
#         except (KeyboardInterrupt,EOFError):
#             break
#
# if __name__=='__main__':
#     main()

##函数声明__doc__
# def aTest():
#     'a function return Nothing'
#     return None
# print aTest.__doc__

##修饰器，装饰器例子
# from time import ctime,sleep
#
# def tsfunc(func):
#     def wrappendFunc():
#         print '[%s] %s() called'%(ctime(),func.__name__)
#         return func()
#     return wrappendFunc     #如果写成wrappendFunc(),则函数返回的是None
#
# @tsfunc     #foo=tsfunc(foo)
# def foo():
#     pass
#
# foo()
# sleep(4)
#
# for i in range(2):
#     sleep(1)
#     foo()

##元组参数
# def func(x,y=1,*rest):  #元组参数储存多余的参数
#     print x
#     print y
#     for i in rest:
#         print i
#
# func(1,2,3,4,5,6)

##字典参数
# def func(x,y=1,**Dic):
#     print x
#     print y
#     for eachkey in Dic.keys():
#         print 'key %s: value %s'%(eachkey,Dic[eachkey])
#
# func(1,2,c='qqq')

##测试函数
# def testit(func,*nkwargs,**kwargs):
#     try:
#         retval=func(*nkwargs,**kwargs)
#         result=(True,retval)    #如果正常运行，返回True和结果
#     except Exception,diag:
#         result=(False,diag)     #运行出现异常则返回False和错误信息
#     return result
#
# def test():
#     funcs=(int,long,float)
#     vals=(1234,12.34,'1234','12.34')
#
#     for eachFunc in funcs:
#         print '-'*20
#         for eachval in vals:
#             retval=testit(eachFunc,eachval)
#             if retval[0]:   #retval[0]为True或False，用于if的判断函数执行是否产生异常
#                 print '%s:%s='%(eachFunc.__name__,str(eachval)),retval[1]
#             else:
#                 print '%s:%s= FALED:'%(eachFunc.__name__,str(eachval)),retval[1]
#
# if __name__=='__main__':
#     test()

#filter(),map(),reduce()

# ##闭包
# def counter(start_at=0):
#     count=[start_at]
#     def iner():
#         count[0]+=1
#         return count[0]
#     return iner
#
# count=counter(3)
# for i in range(4):
#     print count()

##func_closure
# output='<int %r id=%#0x val=%d>'
# w=x=y=z=1
#
# def f1():
#     x=y=z=2
#
# def f2():
#     y=z=3
#
#     def f3():
#         z=4
#         print output%('w',id(w),w)
#         print output%('x',id(x),x)
#         print output%('y',id(y),y)
#         print output%('z',id(z),z)
#
#     clo=f3.func_closure
#     if clo:
#         print "f3 closure vars:",[str(c) for c in clo]
#     else:
#         print "no f3 closure vars"
#     f3()
#
# clo=f2.func_closure
# if clo:
#     print "f2 closure vars:",[str(c) for c in clo]
# else:
#     print "no f2 closure vars"
# f2()
#
# clo=f1.func_closure
# if clo:
#     print "f1 closure vars:",[str(c) for c in clo]
# else:
#     print "no f1 closure vars"
# f1()

##高级闭包和装饰器的例子
# from time import time
#
# def logged(when):
#     def log(f,*args,**kargs):
#         print '''Called:
#         function:%s
#         args:%r
#         kargs:%r'''%(f,args,kargs)
#
#     def pre_logged(f):
#         def wrapper(*args,**kargs):
#             log(f,*args,**kargs)
#             return f(*args,**kargs)
#         return wrapper
#
#     def post_logged(f):
#         def wrapper(*args,**kargs):
#             now=time()
#             try:
#                 return f(*args,**kargs)
#             finally:
#                 log(f,*args,**kargs)
#                 print "time delta:%s"%(time()-now)
#         return wrapper
#
#     try:
#         return {"pre":pre_logged,"post":post_logged}[when]
#     except KeyError,e:
#         raise ValueError(e),'must be "pre" or "post"'
#
# @logged("post")
# def hello(name):
#     print "hello",name
#
# hello('world')

# #变量作用域和命名空间
# j,k=1,2
#
# def proc1():
#     j,k=3,4
#     print 'j==%d and k==%d'%(j,k)
#     k=5
#
# def proc2():
#     j=6
#     proc1()
#     print 'j==%d and k==%d'%(j,k)
#
# k=7
# proc1() #3,4
# print 'j==%d and k==%d'%(j,k)   #1,7
#
# j=8
# proc2() #proc1()的 3,4  然后6,7
# print 'j==%d and k==%d'%(j,k)   #8,7

##递归阶乘
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (n*factorial(n-1))
#
# print factorial(5)

##加强的生成器特性 以闭包为例
# def counter(start_at=0):
#     count=start_at
#     while True:
#         val=(yield count)
#         if val is not None:
#             count=val
#         else:
#             count+=1
#
# count=counter(5)
# print count.next()
# print count.next()
# print count.send(99)
# print count.next()
# count.close()

# # 11-1 参数
# def countToFour1():
#     for eachNum in range(5):
#         print eachNum,
# def countToFour2(n):
#     for eachNum in range(n,5):
#         print eachNum,
# def countToFour3(n=1):
#     for eachNum in range(n,5):
#         print eachNum,
#
# l1=[2,4,5,None]
# l2=[countToFour1,countToFour2,countToFour3]
# for eachFunc in l2:
#     for eachNum in l1:
#         try:
#             eachFunc(eachNum)
#             print
#         except Exception,e:
#             print e

# 11-3
# # (a)
# def max2(a,b):
#     if cmp(a,b) is 1:
#         return a
#     else:
#         return b
#
# def min2(a,b):
#     if cmp(a,b) is -1:
#         return a
#     else:
#         return b
#
# print max2('a','z')     #显示z
# print min2('ab','abc')  #显示ab
#(b)
# def my_max(L):
#     max=L[0]
#     for i in range(len(L)):
#         max=max2(max,L[i])
#     return max
#
# def my_min(L):
#     min=L[0]
#     for i in range(len(L)):
#         min=min2(min,L[i])
#     return min
#
# aList=[1,2,3,4,'a','b','c','z']
# print my_max(aList) #返回z
# print my_min(aList) #返回1

# # 11-4 总时间(分)为参数，返回等价的小时分钟显示
# def HourMin(n):
#     hour=str(n/60)
#     minute=str(n%60)
#     return '%s小时%s分'%(hour,minute)
#
# print HourMin(763)

# # 11-7 map()&zip()
# #map()方法
# list1=[1,2,3]
# list2=['abc','def','ghi']
# list3=map(lambda x,y:str(x)+str(y),list1,list2)
# print list3
# #zip()方法
# list4=[str(i[0])+str(i[1]) for i in zip(list1,list2)]
# print list4

# # 11-8 filter()
# def leapYear(year):
#     '''如果是闰年返回True，否则返回False'''
#     if year%4==0:
#         if year%100!=0:
#             return True
#         else:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#     else:
#         return False
#
# listYears=[x for x in range(1899,2200)] #一个年份列表
# print filter(leapYear,listYears)    #filter()函数返回一个列表，表中元素符合函数leapYear(即返回True)


# #11-9 用reduce()实现average()
# def average(alist):
#     '''用reduce()求得序列所有元素的总和后转化为浮点数，除以序列元素总数得平均值'''
#     return float(reduce(lambda x,y:x+y,alist))/len(alist)
#
# list1=[1,3,5,7,9]
# print average(list1)
