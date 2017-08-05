#-*- coding:utf-8 -*-

# # P105
# s='abcde'
# for i in range(-1,-len(s),-1):
#     print i
#     print s[:i]
#
# print range(-1,-5)      #不合法
# print range(-1,-5,-1)   #从-1开始，每步-1
# print range(-5,-1)      #从-5开始，每步+1（默认步长）
# print range(-5,-1,-1)   #从-5开始，每步-1,不合法
#
# for i in [None]+range(-1,-len(s),-1):  #为了显示全部的abcde，加上None，s==s[:None]
#     print i
#     print s[:i]
#
# # 6-2
# import string
# from keyword import kwlist,iskeyword
#
# myInput=raw_input('Identifier to test?\n')
#
# alphas=string.letters+'_'   #包含所有字母的大小写和‘_’
# nums=string.digits          #包含所有数字
#
# if myInput[0] in alphas:
#     if len(myInput)==1:
#         print "okay as an identifier"
#     elif len(myInput)>1:
#         if myInput in kwlist:       #也可以直接用iskeyword(myInput)来判断myInput是不是关键字
#             print "it's a keyword"
#         else:
#             for i in myInput[1:]:
#                 if i not in alphas+nums:
#                     print 'invallid:remaining symbol must be alphanumeric'
#                     break
#             else:       #for语句的else选项，只有在for语句完成循环不被break时才执行
#                 print 'okay as an identifier'   #否则就要每循环一次就打印一次了
# else:
#     print 'invalid:first symbol must be alphabetic'

# # 6-3
# n=int(raw_input('how many numbers?\n'))
# list1=[]
# for i in range(n):
#     list1.append(float(raw_input('第%d个：'%(i+1))))
# list1.sort()
# list1.reverse()
# print list1

# # 6-4
# n=int(raw_input('how many students?\n'))
# list1=[]
# sum=0
# for i in range(n):
#     list1.append(float(raw_input('score:')))
#     sum+=list1[i]
# average=sum/n
# print 'average='+str(average)

# # 6-5   回文
# str1=raw_input('enter a string:')
# n=len(str1)
# list1=[]
# for i in range(n):
#     list1.append(str1[n-i-1])
# str2=''.join(list1)     #join()方法将列表里的字符串拼接起来
# print str1+str2

# 6-6 strip()函数的替代方法
# str1=raw_input('enter a string:\n')
# list1=[]
# n=len(str1)
# for i in range(n):      #找到第一个不是空格的字符的下标
#     if str1[i]!=' ':
#         n1=i
#         break
# for i in range(n):      #找到最后一个不是空格的元素的下标
#     if str1[n-1-i]!=' ':
#         n2=n-1-i
#         break
# for i in range(n1,n2+1):
#     list1.append(str1[i])
# str2=''.join(list1)
# print "'"+str2+"'"

# 6-7   修改例6.5的错误代码
# num=int(raw_input('enter a number:\n'))
# list1=range(1,num+1)
# i=0
# while i<len(list1):
#     if num%list1[i]==0:
#         list1[i]=''
#     i+=1
# list2=[]
# for i in list1:
#     if i!='':
#         list2.append(i)
# print list2
#
# num=int(raw_input('enter a number:\n'))
# list1=range(1,num+1)
# i=0
# while i<len(list1):
#     if num%list1[i]==0:
#         del list1[i]
#         i-=1    #索引在删除发生后应该回退一位
#     i+=1
# print list1

# 6-8

# def thousand(num):
#     i=num/1000
#     if i:
#         if i==1:
#             return 'one thousand'
#         elif i==2:
#             return 'two thounsand'
#         elif i==3:
#             return 'three thounsand'
#         elif i==4:
#             return 'four thounsand'
#         elif i==5:
#             return 'five thounsand'
#         elif i==6:
#             return 'six thounsand'
#         elif i==7:
#             return 'seven thounsand'
#         elif i==8:
#             return 'eight thounsand'
#         elif i==9:
#             return 'night thounsand'
#         elif i==10:
#             return 'ten thounsand'
#     else:
#         return ''
#
# def Handred(num):
#     numH=int(str(num)[-3:None])
#     i=numH/100
#     if i==1:
#         if int(str(num)[-2:None])==0:
#             return 'one handred'
#         else:
#             return 'one handred and'
#     elif i==2:
#         if int(str(num)[-2:None])==0:
#             return 'two handred'
#         else:
#             return 'two handred and'
#     elif i==3:
#         if int(str(num)[-2:None])==0:
#             return 'three handred'
#         else:
#             return 'three handred and'
#     elif i==4:
#         if int(str(num)[-2:None])==0:
#             return 'four handred'
#         else:
#             return 'four handred and'
#     elif i==5:
#         if int(str(num)[-2:None])==0:
#             return 'five handred'
#         else:
#             return 'five handred and'
#     elif i==6:
#         if int(str(num)[-2:None])==0:
#             return 'six handred'
#         else:
#             return 'six handred and'
#     elif i==7:
#         if int(str(num)[-2:None])==0:
#             return 'seven handred'
#         else:
#             return 'seven handred and'
#     elif i==8:
#         if int(str(num)[-2:None])==0:
#             return 'eight handred'
#         else:
#             return 'eight handred and'
#     elif i==9:
#         if int(str(num)[-2:None])==0:
#             return 'nine handred'
#         else:
#             return 'nine handred and'
#     elif i==0:
#         if num>999:
#             if int(str(num)[-2:None])==0:
#                 return ' '
#             else:
#                 return 'and'
#         else:
#             return ''
#
# def Ten(num):
#     ten=''
#     numTS=int(str(num)[-2:None])
#     T=numTS/10
#     S=numTS-10*T
#     if T!=1 and T!=0:
#         if T==2:
#             ten=' twenty-'
#         elif T==3:
#             ten=' thirty-'
#         elif T==4:
#             ten=' forty'
#         elif T==5:
#             ten=' fifty-'
#         elif T==6:
#             ten=' sixty-'
#         elif T==7:
#             ten=' seventy-'
#         elif T==8:
#             ten=' eighty-'
#         elif T==9:
#             ten=' ninety-'
#         if S=='0':
#             ten=ten[:-1]
#     elif T==1:
#         ten=' '
#     elif T==0:
#         ten=' '
#     return ten
#
# def Single(num):
#     single=''
#     numTS=int(str(num)[-2:None])
#     T=numTS/10
#     S=numTS-10*T
#     if T!=0 and T!=1:
#         if S==1:
#             single='first'
#         if S==2:
#             single='second'
#         elif S==3:
#             single='third'
#         elif S==4:
#             single='four'
#         elif S==5:
#             single='five'
#         elif S==6:
#             single='six'
#         elif S==7:
#             single='seven'
#         elif S==8:
#             single='eight'
#         elif S==9:
#             single='nine'
#     elif T==1:
#         if numTS==11:
#             single='eleven'
#         elif numTS==12:
#             single='twelve'
#         elif numTS==13:
#             single='thirdteen'
#         elif numTS==14:
#             single='fourteen'
#         elif numTS==15:
#             single='fifteen'
#         elif numTS==16:
#             single='sixteen'
#         elif numTS==17:
#             single='seventeen'
#         elif numTS==18:
#             single='eighteen'
#         elif numTS==19:
#             single='nineteen'
#         elif numTS==10:
#             single='ten'
#     elif T==0:
#         if S==0 and num==0:
#             single='zero'
#         elif S==1:
#             single='one'
#         elif S==2:
#             single='two'
#         elif S==3:
#             single='three'
#         elif S==4:
#             single='four'
#         elif S==5:
#             single='five'
#         elif S==6:
#             single='six'
#         elif S==7:
#             single='seven'
#         elif S==8:
#             single='eight'
#         elif S==9:
#             single='nine'
#     return single
#
# num=int(raw_input('enter a number:\n'))
# print str(thousand(num)),str(Handred(num))+str(Ten(num))+Single(num)

# # 6-9
# mins=int(raw_input('enter minutes:'))
# h=mins/60
# m=mins-60*h
# if len(str(m))==1:
#     print '%d:0%d'%(h,m)
# else:
#     print '%d:%d'%(h,m)

# 6-10
# import string
# lowLetters=string.letters[:26]  #a~z
# upperLetters=string.letters[26:]    #A~Z
# def updown(str):
#     n=len(str)
#     strList=[]
#     for i in range(n):
#         if str[i] in lowLetters:
#             strList.append(str[i].upper())
#         elif str[i] in upperLetters:
#             strList.append(str[i].lower())
#         else:
#             strList.append(str[i])
#     str1=''.join(strList)
#     return str1
#
# str=raw_input('enter:\n')
# print updown(str)

# # 6-12
# def findchar(string,char):
#     n=len(string)
#     for i in range(n):
#         if string[i]==char:
#             break
#     else:
#         i=-1
#     return  i
#
# def rfindchar(string,char):
#     n=len(string)
#     for i in range(n):
#         if string[n-i-1]==char:
#             i=n-i-1
#             break
#     else:
#         i=-1
#     return i
#
# def subchar(string,char,newchar):
#     n=len(string)
#     newStrList=[]
#     for i in range(n):
#         if string[i]==char:
#             newStrList.append(newchar)
#         else:
#             newStrList.append(string[i])
#     newString=''.join(newStrList)
#     return newString
#
# string='abccba'
# char='b'
# newchar='B'
# print findchar(string,char)
# print rfindchar(string,char)
# print subchar(string,char,newchar)

# 6-13
# import string
# nums=string.digits
# def atoc(string):
#     n=len(string)
#     ij=i_=False
#     if string[-1]=='j':
#         for i in range(n):
#             if string[n-2-i] not in nums:
#                 ij=n-2-i
#                 break
#     else:
#         for i in range(n):
#             if string[n-1-i] not in nums:
#                 i_=n-1-i
#                 break
#     if ij:
#         real=float(eval(string[:ij]))
#         image=float(string[ij:-1])
#         return complex(real,image)
#     elif i_:
#         real=float(eval(string[:i_]))
#         image=float(string[i_:])
#         return complex(real,image)
#     else:
#         return float(string)
#
# string=str(raw_input('enter:\n'))
# print string
# print atoc(string)

# # 6-14 剪刀石头布
# from random import choice
# dictSTC={'s':2,'c':1,'t':0}
# print '[S]cissors,s[T]one,[C]loth'
# listSTC=['s','t','c']
# while True:
#     UserChoice=raw_input('enter your choice:\n')
#     UserChoice=UserChoice.lower()
#     if UserChoice in listSTC:
#         break
#     else:
#         print 'Try again\n'
# listSTC=['s','t','c']
# ComChoice=choice(listSTC)
# print ComChoice
# def judge(UserChoice,ComChoice):
#     if UserChoice=='s' and ComChoice=='t':
#         return 'Computer win'
#     elif UserChoice=='t' and ComChoice=='s':
#         return 'User win'
#     else:
#         if dictSTC[UserChoice]>dictSTC[ComChoice]:
#             return 'User win'
#         elif dictSTC[UserChoice]<dictSTC[ComChoice]:
#             return 'Computer win'
#         elif dictSTC[UserChoice]==dictSTC[ComChoice]:
#             return 'Tie'
# print judge(UserChoice,ComChoice)

# 6-15
# import datetime
#
# def transform(date_input):
#     month=int(date_input.split('/')[0])
#     day=int(date_input.split('/')[1])
#     year=int(date_input.split('/')[2])
#     return (year,month,day)
# #(a)
# # d1_input=raw_input('M/D/Y:')
# # d2_input=raw_input('M/D/Y:')
# # d1=datetime.date(transform(d1_input)[0],transform(d1_input)[1],transform(d1_input)[2])
# # d2=datetime.date(transform(d2_input)[0],transform(d2_input)[1],transform(d2_input)[2])
# # print (d2-d1).days
# # #(b)
# d3_input=raw_input('(birthday)M/D/Y:')
# d3=datetime.date(transform(d3_input)[0],transform(d3_input)[1],transform(d3_input)[2])
# print (datetime.date.today()-d3).days
# #(c)
# import time
# year=int(time.strftime('%Y'))+1
# d4=datetime.date(year,transform(d3_input)[1],transform(d3_input)[2])
# print (d4-datetime.date.today()).days
#
# # 6-17
# def newPop(list):
#     n=len(list)
#     popitem=list[n-1]
#     del list[n-1]
#     return popitem
# list=[1,2,3]
# while True:
#     print newPop(list)
#     raw_input()

# 6-18
def func(list,lines,horizontal=1):
    n=len(list)
    elems=n/lines  #每行（或每列）的元素个数

    if horizontal==1:   #水平排列
        dict_horizon={}
        for i in range(lines):  #用一个字典储存每行里的元素
            dict_horizon[i]=[]

        for y in range(lines):      #没有考虑余数部分
            for x in range(elems):
                dict_horizon[y].append(str(list[y*elems+x]))

        MOD_H_elems=n%lines
        for i in range(MOD_H_elems):  #在最后一行加上余数部分
            dict_horizon[lines-1].append(str(list[lines*elems+i]))

        strh=''
        for x in range(lines):
            strh+=','.join(dict_horizon[x])+'\n'

        return strh

    if horizontal==0:
        dict_vertical={}    #新建字典保存每一行的元素
        for i in range(elems):
            dict_vertical[i]=[]

        for x in range(lines):   #竖直排列，水平中的行数变成了每行元素个数
            for y in range(elems):  #每行元素个数变成了行数
                dict_vertical[y].append(str(list[x*elems+y]))

        MOD_V_elems=n%lines

        for i in range(MOD_V_elems):    #余数元素需要新建若干行
            dict_vertical[i+elems]=[]
        for i in range(MOD_V_elems):    #该行只有最后一位有元素
            for x in range(lines-1):
                dict_vertical[i+elems].append('  ')
            dict_vertical[i+elems].append(str(list[lines*elems+i]))

        strv=''
        for x in range(elems+MOD_V_elems):
            strv+=','.join(dict_vertical[x])+'\n'
        return strv

list=[]
for i in range(100):
    list.append(i)
print func(list,7,horizontal=0)
