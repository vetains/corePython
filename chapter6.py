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

def thousand(num):
    i=num/1000
    if i:
        if i==1:
            return 'one thousand'
        elif i==2:
            return 'two thounsand'
        elif i==3:
            return 'three thounsand'
        elif i==4:
            return 'four thounsand'
        elif i==5:
            return 'five thounsand'
        elif i==6:
            return 'six thounsand'
        elif i==7:
            return 'seven thounsand'
        elif i==8:
            return 'eight thounsand'
        elif i==9:
            return 'night thounsand'
        elif i==10:
            return 'ten thounsand'
    else:
        return ''

def Handred(num):
    numH=int(str(num)[-3:None])
    i=numH/100
    if i==1:
        if int(str(num)[-2:None])==0:
            return 'one handred'
        else:
            return 'one handred and'
    elif i==2:
        if int(str(num)[-2:None])==0:
            return 'two handred'
        else:
            return 'two handred and'
    elif i==3:
        if int(str(num)[-2:None])==0:
            return 'three handred'
        else:
            return 'three handred and'
    elif i==4:
        if int(str(num)[-2:None])==0:
            return 'four handred'
        else:
            return 'four handred and'
    elif i==5:
        if int(str(num)[-2:None])==0:
            return 'five handred'
        else:
            return 'five handred and'
    elif i==6:
        if int(str(num)[-2:None])==0:
            return 'six handred'
        else:
            return 'six handred and'
    elif i==7:
        if int(str(num)[-2:None])==0:
            return 'seven handred'
        else:
            return 'seven handred and'
    elif i==8:
        if int(str(num)[-2:None])==0:
            return 'eight handred'
        else:
            return 'eight handred and'
    elif i==9:
        if int(str(num)[-2:None])==0:
            return 'nine handred'
        else:
            return 'nine handred and'
    elif i==0:
        if num>999:
            if int(str(num)[-2:None])==0:
                return ' '
            else:
                return 'and'
        else:
            return ''

def Ten(num):
    ten=''
    numTS=int(str(num)[-2:None])
    T=numTS/10
    S=numTS-10*T
    if T!=1 and T!=0:
        if T==2:
            ten=' twenty-'
        elif T==3:
            ten=' thirty-'
        elif T==4:
            ten=' forty'
        elif T==5:
            ten=' fifty-'
        elif T==6:
            ten=' sixty-'
        elif T==7:
            ten=' seventy-'
        elif T==8:
            ten=' eighty-'
        elif T==9:
            ten=' ninety-'
        if S=='0':
            ten=ten[:-1]
    elif T==1:
        ten=' '
    elif T==0:
        ten=' '
    return ten

def Single(num):
    single=''
    numTS=int(str(num)[-2:None])
    T=numTS/10
    S=numTS-10*T
    if T!=0 and T!=1:
        if S==1:
            single='first'
        if S==2:
            single='second'
        elif S==3:
            single='third'
        elif S==4:
            single='four'
        elif S==5:
            single='five'
        elif S==6:
            single='six'
        elif S==7:
            single='seven'
        elif S==8:
            single='eight'
        elif S==9:
            single='nine'
    elif T==1:
        if numTS==11:
            single='eleven'
        elif numTS==12:
            single='twelve'
        elif numTS==13:
            single='thirdteen'
        elif numTS==14:
            single='fourteen'
        elif numTS==15:
            single='fifteen'
        elif numTS==16:
            single='sixteen'
        elif numTS==17:
            single='seventeen'
        elif numTS==18:
            single='eighteen'
        elif numTS==19:
            single='nineteen'
        elif numTS==10:
            single='ten'
    elif T==0:
        if S==0 and num==0:
            single='zero'
        elif S==1:
            single='one'
        elif S==2:
            single='two'
        elif S==3:
            single='three'
        elif S==4:
            single='four'
        elif S==5:
            single='five'
        elif S==6:
            single='six'
        elif S==7:
            single='seven'
        elif S==8:
            single='eight'
        elif S==9:
            single='nine'
    return single

num=int(raw_input('enter a number:\n'))
print str(thousand(num)),str(Handred(num))+str(Ten(num))+Single(num)
