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

#filter()
