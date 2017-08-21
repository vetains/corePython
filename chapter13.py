#-*- coding:utf-8 -*-

##在命令行中运行python，粘贴下面三段以导入
# import sys
# sys.path.append('/home/vetains/pywork/pycore')
# import chapter13 as c13

# class C(object):
#     '''a class'''
#     def __init__(self):
#         pass
#     def A(self):
#         print 'a'
#
# c=C()
# print C.__class__

# class P(object):
#     def __init__(self):
#         print 'this is P'

# class C(P):
#     def __init__(self):
#         P.__init__(self)
#         print 'this is C'
#
# class C(P):
#     def __init__(self):
#         super(C,self).__init__()    #super()方法不需要知道父类
#         print 'this is C'
# c=C()
# class RoundFloat(float):
#     def __new__(cls,val):
#         return float.__new__(cls,round(val,2))

# class RoundFloat(float):
#     def __new__(cls,val):
#         return super(RoundFloat,cls).__new__(cls,round(val,2))
#

# #经典类的多重继承MRO
# class P1:
#     def foo(self):
#         print 'P1-foo()'
#
# class P2:
#     def foo(self):
#         print 'P2-foo()'
#     def bar(self):
#         print 'P2-bar()'
#
# class C1(P1,P2):
#     pass
#
# class C2(P1,P2):
#     def bar(self):
#         print 'C2-bar()'
#
# class GC(C1,C2):
#     pass
#
# gc=GC()
# gc.foo()    #P1-foo()
# gc.bar()    #P2-bar(),略过了C2的bar(),深度优先

# #新式类的多重继承MRO
# class P1(object):
#     def foo(self):
#         print 'P1-foo()'
#
# class P2(object):
#     def foo(self):
#         print 'P2-foo()'
#     def bar(self):
#         print 'P2-bar()'
#
# class C1(P1,P2):
#     pass
#
# class C2(P1,P2):
#     def bar(self):
#         print 'C2-bar()'
#
# class GC(C1,C2):
#     pass
#
# gc=GC()
# gc.foo()    #P1-foo()
# gc.bar()    #C2-bar() 广度优先

# #hasattr(),getattr(),setattr(),delattr()
# class myClass(object):
#     def __init__(self):
#         self.foo=42
#
# mc=myClass()
# print hasattr(mc,'foo')
# print getattr(mc,'foo')
# # print getattr(mc,'bar')       #getattr()不存在的属性会报错
# setattr(mc,'bar','64')          #setattr(实例,属性,值)增加一个属性和对应的值
# print dir(mc)                   #检查实例mc里的属性,已经多出例'bar'
# print getattr(mc,'bar')
# mc2=myClass()
# print hasattr(mc2,'bar')        #在另一个实例里并没有属性'bar',说明上一步的set只是实例属性
# delattr(mc,'foo')
# print hasattr(mc,'foo')
# print hasattr(mc2,'foo')        #mc2里仍有'foo',所以delattr也只是删除该实例的属性

# #RoundFloatManual
# class RFM(object):
#     def __init__(self,val):
#         assert isinstance(val,float),'value must be float'
#         self.value=round(val,2)
#
#     def ___str__(self):  #未赋值给__repr__时,只有print时才能显示结果
#         return '%.2f'%self.value
#
#     __repr__=___str__    #赋值给__repr__后,直接调用实例也能返回结果

# #Time60
# class Time60(object):
#     'calculate hours and minutes'
#     def __init__(self,h,m):
#         self.hour=h
#         self.min=m
#
#     def ___str__(self):
#         return '%d : %d'%(self.hour,self.min)
#
#     __repr__=___str__
#
#     def __add__(self,other):
#         '处理了分钟数大于60的情况'
#         if self.min+other.min>=60:
#             return self.__class__(self.hour+other.hour+1,self.min+other.min-60)
#         else:
#             return self.__class__(self.hour+other.hour,self.min+other.min)
#
#     def __iadd__(self,other):
#         if self.min+other.min>=60:
#             self.hour=self.hour+other.hour+1
#             self.min=self.min+other.min-60
#         else:
#             self.hour+=other.hour
#             self.min++other.min
#         return self

# #RandSeq.py
# from random import choice
#
# class RandSeq(object):
#     def __init__(self,seq):
#         self.data=seq
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         return choice(self.data)

# #anyIter.py
# class AnyIter(object):
#     def __init__(self,data,safe=False):
#         self.safe=safe
#         self.iter=iter(data)    #iter(data)返回一个迭代器
#
#     def __iter__(self):
#         return self
#
#     def next(self,howmany=1):
#         retval=[]
#         for eachitem in range(howmany):
#             try:
#                 retval.append(self.iter.next())
#             except StopIteration:
#                 if self.safe:
#                     break
#                 else:
#                     raise
#         return retval

# #多类型类定制
# class NumStr(object):
#     def __init__(self,Num=0,Str=''):
#         self.__num=Num
#         self.__str=Str
#
#     def __str__(self):
#         # return '[%d :: %s]'%(self.__num,self.__str) #使用%s会没有单引号 如[1 :: abc]
#         return '[%d :: %r]'%(self.__num,self.__str)   #使用%r会有单引号 [1 :: 'abc']
#
#     __repr__=__str__
#
#     def __add__(self,other):
#         if isinstance(other,NumStr):
#             return self.__class__(self.__num+other.__num,self.___str+other.__str)
#         else:
#             raise TypeError,'should add an object in same class'
#
#     def __mul__(self,num):
#         if isinstance(num,int):
#             return self.__class__(num*self.__num,num*self.__str)
#         else:
#             raise TypeError,'should mul an int number'
#
#     def __nonzero__(self):
#         return self.__num or len(self.__str)  #实例为默认值时返回0?False值
#
#     def _norm_cval(self,cmpres):    # 接受cmp()result 为参数
#         return cmp(cmpres,0)        #cmp()策略为:cmp(数字)+cmp(字符串)=和,再将cmp(和,0)
#
#     def __cmp__(self,other):
#         if isinstance(other,NumStr):
#             return self._norm_cval(cmp(self.__num,other.__num)+cmp(self.__str,other.__str))
#         else:
#             raise TypeError,'should compare the same class object'

# #包装与授权
# class Wrap(object):
#     def __init__(self,obj):
#         self.__data=obj
#     def get(self):
#         return self.__data
#     def __repr__(self):
#         return str(self.__data)
#     def __str__(self):
#         return str(self.__data)
#     def __getattr__(self,attr):
#         return getattr(self.__data,attr)

# #包装标准类型
# from time import time,ctime
#
# class timeWrapme(object):
#     '''ctime:创建时间,mtime:修改时间,atime:访问时间'''
#
#     def __init__(self,obj):
#         '''包装初始化,获得对象并记录时间'''
#         self.__data=obj
#         self.__ctime=self.__mtime=self.__atime=time()
#
#     def get(self):
#         '''获取对象实体,更改访问时间'''
#         self.__atime=time()
#         return self.data
#
#     def gettimeval(self,t_type):
#         '''获取'cma'中的某个时间的值'''
#         if not isinstance(t_type,str) or t_type[0] not in 'cma':
#             raise TypeError,'只能访问 [c]创建时间,[m]修改时间,[a]访问时间'
#         else:
#             print self,'_%s__%stime'%(self.__class__.__name__,t_type[0])
#             return  getattr(self,\
#                     '_%s__%stime'%(self.__class__.__name__,t_type[0]))
#
#     def gettimestr(self,t_type):
#         '''获取时间的字符串'''
#         return ctime(self.gettimeval(t_type))
#
#     def set(self,obj):
#         '''修改,更新修改时间和访问时间'''
#         self.__mtime=self.__atiem=time()
#         self.__data=obj
#
#     def __repr__(self):
#         '''访问,更新访问时间'''
#         self.__atime=time()
#         return str(self.__data)
#
#     def __str__(self):
#         '''访问,更新访问时间'''
#         self.__atime=time()
#         return str(self.__data)
#
#     def __getattr__(self,attr):
#         '''运用属性,更新访问时间'''
#         self.__atime=time()
#         return getattr(self.__data,attr)
#
# l=[1,2,3]
# tw=timeWrapme(l)
# print tw.gettimestr('c')

# #描述符-使用文件来存储属性
# import os,pickle
#
# class FileDescr(object):
#     saved=[]
#
#     def __init__(self,name=None):
#         self.name=name
#
#     def __get__(self,obj,typ=None):
#         if self.name not in FileDescr.saved:
#             raise AttributeError,'%r used before assignment'%self.name
#
#         try:
#             f=open(self.name,'r')
#             val=pickle.load(f)
#             f.close()
#             return val
#         except (pickle.UnpicklingError,IOError,EOFError,AttributeError,IndexError),e:
#             raise AttributeError,'could not read %r'%self.name
#
#     def __set__(self,obj,val):
#         f=open(self.name,'w')
#         try:
#             pickle.dump(val,f)
#             FileDescr.saved.append(self.name)
#         except (TypeError,pickle.PicklingError),e:
#             raise AttributeError,'could not pickle %r'%self.name
#         finally:
#             f.close()
#
#     def __delete__(self,obj):
#         try:
#             os.unlink(self.name)
#             FileDescr.saved.remove(self.name)
#         except (OSError,ValueError),e:
#             pass
#
# class m(object):
#     foo=FileDescr('foo')
#     bar=FileDescr('bar')      #不懂pickle,例子意义不明

#property()内建函数
# class PX(object):
#     def __init__(self,x):
#         self.__x=~x
#
#     def get_x(self):
#         return ~self.__x
#
#     x=property(get_x)
#
# class HideX(object):
#     def __init__(self,x):
#         self.__x=x
#
#     def get_x(self):
#         return ~self.__x
#
#     def set_x(self,x):
#         self.__x=~x
#
#     x=property(get_x,set_x)
#     '''property(fget,fset,fdel,fdoc),因而默认第一个参数为fget,以此类推.
#        所以调用属性会自动执行get_x,设置属性会自动执行set_x'''
#
# #HideX 类里的方法还可以采用修饰符@property的方式
# class HideX1(object):
#     def __init__(self,x):
#         self.__x=x
#
#     @property
#     def x():
#         def fget(self):
#             return ~self.__x
#
#         def fset(self):
#             self.__x=~x
#
#         return locals() #locals()函数返回一个包含所有函数方法名和对应对象的字典

# #元类示例
# from warnings import warn
#
# class ReqStrSugRepr(type):  #需要__str__ 建议__repr__
#     def __init__(cls,name,bases,attrd):
#         super(ReqStrSugRepr,cls).__init__(name,bases,attrd)
#
#         if '__str__' not in attrd:
#             raise TypeError("Class requires overriding of __str__()")
#
#         if '__repr__' not in attrd:
#             warn("Class suggests overriding of __repr__\n",stacklevel=3)
#
# print '***Defined ReqStrSugRepr (meta)class\n'
#
# class Foo(object):
#     __meatclass__=ReqStrSugRepr
#
#     def __str__(self):
#         return 'Instance of class',self.__class__.__name__
#
#     def __repr__(self):
#         return self.__class__.__name__
#
# print '***Defined Foo class\n'
#
# class Bar(object):
#     __metaclass__=ReqStrSugRepr
#
#     def __str__(self):
#         return 'Instance of class',self.__class__.__name__
#
# print '***Defined Bar class\n'
#
# class FooBar(object):
#     __metaclass__=ReqStrSugRepr
#
# print '***Defined FooBar class\n'

# # 13-3 类定制
# #dollarize()函数
# def dollarize(money):
#     '''返回美元字符串,两位小数,支持千位逗号,以及$前负号'''
#     if not isinstance(money,float) and not isinstance(money,int):
#         raise TypeError,'输入浮点数或整型'
#
#     roundNum=round(money,2)     #约数
#     intStr=str(roundNum).split('.')[0]  #获取约数的整数部分
#     floatStr=str(roundNum).split('.')[1]    #约数的小数部分
#
#     #千位逗号
#     intStrList_R=[i for i in reversed(list(intStr))] #整数部分字符串的倒序列表
#
#     if roundNum<0:
#         intStrList_R.remove('-')
#         '''除去负号,负号对千位逗号有干扰
#            负号增加了列表长度,使得 -,123,123 的情况出现'''
#
#     i=3     #第一个逗号在倒序列表的第三个索引位,此后为7,11,15...每次+4
#     while i<len(intStrList_R):  #一直到i超出了整数字符串的长度
#         intStrList_R.insert(i,',')
#         i+=4
#     intStrList_R.reverse()
#     intStr=''.join(intStrList_R)
#
#     if len(floatStr) is 1:      #如果小数部分只剩一位,则补加一个0
#         floatStr=floatStr+'0'
#
#     if not roundNum<0:
#         return '$'+intStr+'.'+floatStr
#     else:
#         return '-$'+intStr+'.'+floatStr     #上端列表已经省略intStr的负号
#
# # print dollarize(-11.95555555557)
#
# class MoneyFmt(object):
#     def __init__(self,money,special=False):
#         if not isinstance(money,int) and not isinstance(money,float):
#             raise TypeError,'参数为整型或浮点型'
#         else:
#             self.money=money
#             self.special=special
#
#     def update(self,anotherMoney):
#         if not isinstance(anotherMoney,int) and not isinstance(anotherMoney,float):
#             raise TypeError,'参数为整型或浮点型'
#         else:
#             self.money=anotherMoney
#
#     def __nonzero__(self):
#         #return self.money   #所以是返回数值还是返回布尔值?
#         '''答:这个直接返回数值,但__nonzer__只接受布尔值或整型返回,
#             所以让它返回布尔值就好'''
#         return bool(self.money)
#
#     def __repr__(self):
#         if not self.money<0:
#             return '$'+str(self.money)
#         else:
#             return '-$'+str(self.money)[1:]
#
#     def __str__(self):
#         '''print时显示处理过的形式,解释在上方dollarize()函数中'''
#         roundNum=round(self.money,2)
#         intStr=str(roundNum).split('.')[0]
#         floatStr=str(roundNum).split('.')[1]
#
#         intStrList_R=[i for i in reversed(list(intStr))]
#
#         if roundNum<0:
#             intStrList_R.remove('-')
#
#         i=3
#         while i<len(intStrList_R):
#             intStrList_R.insert(i,',')
#             i+=4
#         intStrList_R.reverse()
#         intStr=''.join(intStrList_R)
#
#         if len(floatStr) is 1:
#             floatStr=floatStr+'0'
#
#         if not roundNum<0:
#             return '$'+intStr+'.'+floatStr
#         else:
#             if not self.special:    #self.special==False时
#                 return '-$'+intStr+'.'+floatStr
#             else:                   #self.special==True时
#                 return '<-$'+intStr+'.'+floatStr+'>'

# #千位逗号的,数学方法的,另一种实现
# def douHao(num):
#     douNums=len(str(int(num)))/3     #判断逗号的个数
#     if len(str(int(num)))%3==0:      #如果数字长度为3的倍数,逗号个数会少一个
#         douNums-=1
#
#     floatStr=''
#     if isinstance(num,float):        #如果是浮点数,要把小数部分摘出来
#         floatStr='.'+str(num).split('.')[1]
#         num=int(num)                 #只处理整数部分
#
#     result=''
#     for i in range(douNums+1)[::-1]:   #假如douNum是3,列表应为[3,2,1,0]
#
#         newStr=str(num/(1000**i))      #1500/1000=1 得到'1,'
#         if i!=0:
#             newStr=newStr+','
#
#         result+=newStr
#         num=num%(1000**i)              #继续处理1500%1000=500
#
#     return result+floatStr
#
# print douHao(123456.89)

# #13-4 用户注册
# import shelve
# import wx
# from time import ctime,time
# import sys
#
# class My_DB(object):
#     '''数据库类,在实例化操作时加载已经保存的用户信息,提供访问函数来添加或更新数据库信息.
#        数据修改后,数据库会在垃圾回收时将新信息保存到磁盘'''
#     def __init__(self,name):
#         self.db=shelve.\
#             open('/home/vetains/pywork/pycore/chapter13.dat')   #打开数据库
#         self.name=name
#         if self.name in self.db.keys():
#             self.info=self.db[self.name]
#         else:
#             self.db[self.name]=''
#             self.info=''
#
#     def LookOrUpdate(self,newInfo=None):
#         '''newInfo有值时更新数据库,否则直接返回数据库内的info'''
#         if newInfo:     #调用方法时若给了newInfo,则更新info
#             self.info=newInfo
#         return self.info
#
#     def __del__(self):
#         '''数据库类被垃圾回收时保存信息到磁盘'''
#         self.db[self.name]=self.info
#         self.db.close()
#
#
# #更新7-5的代码,运用上信息数据库类,修改主要在welcome函数里
#
# class Creation(wx.Frame):
#     '''一个询问界面'''
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'一个询问',pos=(60,60),size=(250,300))
#         panel=wx.Panel(self,-1)
#         self.text1=wx.StaticText(panel,label='你是否要注册一个账户？',
#                                  pos=(50,50),size=(180,40))
#         self.button1=wx.Button(panel,label='是',pos=(60,100),size=(40,25))
#         self.button1.Bind(wx.EVT_BUTTON,self.LogOnClick)
#         self.button2=wx.Button(panel,label='否',pos=(100,100),size=(40,25))
#         self.button2.Bind(wx.EVT_BUTTON,self.QuitClick)
#
#     def QuitClick(self,event):
#         self.Destroy()
#     def LogOnClick(self,enent):
#         logon=LogOn()
#         logon.Show()
#         self.Destroy()
#
# class LogOn(wx.Frame):
#     '''一个注册界面'''
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'创建账户',size=(400,250))
#         panel=wx.Panel(self,-1)
#         #用户名与密码文本框
#         db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
#         now=ctime(time())   #now是由ctime()返回的
#         self.text1=wx.StaticText(panel,label='用户名:',pos=(50,50),size=(50,25))
#         self.text2=wx.StaticText(panel,label='密码:',pos=(50,70),size=(50,25))
#         self.textCtrl1=wx.TextCtrl(panel,pos=(105,50),size=(75,25))
#         self.textCtrl2=wx.TextCtrl(panel,pos=(105,70),size=(75,25))
#         self.name=str(self.textCtrl1.GetValue())
#         self.password=str(self.textCtrl2.GetValue())
#         #注册按钮
#         self.button1=wx.Button(panel,label='注册',pos=(65,100),size=(40,30))
#         # self.button1.Bind(wx.EVT_BUTTON,lambda event,\
#         #     n=self.name,p=self.password:self.CreateClick(event,n,p))
#         self.button1.Bind(wx.EVT_BUTTON,self.CreateClick)
#         #取消按钮
#         self.button2=wx.Button(panel,label='取消',pos=(105,100),size=(40,30))
#         self.button2.Bind(wx.EVT_BUTTON,self.QuitClick)
#
#     def QuitClick(self,event):
#         '''取消事件'''
#         self.Destroy()
#
#     def CreateClick(self,event):
#         '''注册事件'''
#         name=str(self.textCtrl1.GetValue())
#         password=str(self.textCtrl2.GetValue())
#
#         db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
#         now=ctime(time())   #now是由ctime()返回的字符串
#         newUser={'password':password,'time':now}
#         db[name]=newUser
#         db.close()
#         self.Destroy()
#
# class adminMenue(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'管理菜单',size=(600,600))
#         panel=wx.Panel(self,-1)
#         db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
#         nameList=[]
#         pwList=[]
#         timeList=[]
#         for eachKey in db.keys():
#             nameList.append(eachKey)
#             pwList.append(db[eachKey]['password'])
#             timeList.append(db[eachKey]['time'])
#         db.close()
#         nameStr='名单列表:\n'+'\n'.join(nameList)
#         pwStr='密码列表:\n'+'\n'.join(pwList)
#         timeStr='登录时间:\n'+'\n'.join(timeList)
#         self.text1=wx.StaticText(panel,label=nameStr,pos=(50,50),size=(200,200))
#         self.text2=wx.StaticText(panel,label=pwStr,pos=(150,50),size=(200,200))
#         self.text3=wx.StaticText(panel,label=timeStr,pos=(250,50),size=(200,200))
#
# class Main(wx.Frame):
#     '''主界面'''
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'主界面',size=(360,240))
#         panel=wx.Panel(self,-1)
#         #用户名
#         self.text1=wx.StaticText(panel,label='用户名:',pos=(10,10),size=(100,50))
#         self.textCtrl1=wx.TextCtrl(panel,pos=(100,10),size=(100,10))
#         # name=str(textCtrl1.GetValue())    #像这样直接获取文本框的文本是不可行的.
#         #密码
#         self.text2=wx.StaticText(panel,label='密码:',pos=(10,60),size=(100,50))
#         self.textCtrl2=wx.TextCtrl(panel,pos=(100,60),size=(100,0))
#         # password=str(textCtrl2.GetValue())
#
#         #登录按钮
#         self.logInButton=wx.Button(panel,-1,label='登录',pos=(30,180),size=(100,50))
#         self.logInButton.Bind(wx.EVT_BUTTON,self.logInClick)
#         #菜单按钮
#         self.adminMenuButton=wx.Button(panel,-1,label='菜单管理',pos=(130,180),size=(100,50))
#         self.adminMenuButton.Bind(wx.EVT_BUTTON,self.adminMenuClick)
#         #退出按钮
#         self.quitButton=wx.Button(panel,-1,label='退出',pos=(230,180),size=(100,50))
#         self.quitButton.Bind(wx.EVT_BUTTON,self.quitClick)
#
#     def adminMenuClick(self,event):
#         '''菜单按钮事件'''
#         admin=adminMenue()
#         admin.Show()
#
#     def quitClick(self,event):
#         '''退出按钮事件'''
#         sys.exit()
#
#     def logInClick(self,event):
#         '''登录按钮事件'''
#
#         name=str(self.textCtrl1.GetValue())
#         password=str(self.textCtrl2.GetValue())
#
#         db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
#         keyList=db.keys()
#         db.close()
#
#         if name in keyList:
#
#             db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
#             dbPassword=db[name]['password']
#             db.close()
#
#             if password==dbPassword:
#                 '''用户名已存在且密码正确则唤起欢迎界面'''
#                 self.welcome(name,password)
#             else:
#                 '''密码错误唤起密码错误界面'''
#                 self.refuse(name)
#         else:
#             '''用户名不存在则询问是否注册'''
#             creation=Creation()
#             creation.Show()
#
#     def welcome(self,name,password):
#         '''欢迎界面||因13-4而增加了内容'''
#
#         def fix(event):
#             '''修改按钮事件'''
#             newInfo=str(textCtrl1.GetValue())
#             infoDB.LookOrUpdate(newInfo)
#
#         def quit(event):
#             '''退出按钮事件'''
#             welcomeWin.Destroy()
#
#         welcomeApp=wx.App()
#         welcomeWin=wx.Frame(None,title='欢迎!',size=(400,400))
#         panel=wx.Panel(welcomeWin,-1)
#
#         welStr='欢迎,%s,你的上次登录时间为'
#         text1=wx.StaticText(panel,label=welStr%name,pos=(50,50),size=(500,20))
#         db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
#         lastTime=db[name]['time']    #上次登录时间
#         now=ctime(time())            #更新登录时间
#         db[name]={'password':password,'time':now}
#         db.close()
#         text2=wx.StaticText(panel,label=lastTime,pos=(50,80),size=(250,20))
#         #调用数据库类
#         infoDB=My_DB(name)
#         text3=wx.StaticText(panel,label='储存的信息为:',pos=(50,105),size=(250,20))
#         #显示储存信息的文本框,可修改,默认值为信息 value=infoDB.info
#         textCtrl1=wx.TextCtrl(panel,value=infoDB.info,pos=(50,130),size=(250,20))
#         #设置修改储存信息的按钮
#         FixButton=wx.Button(panel,label='修改',pos=(50,155),size=(50,45))
#         FixButton.Bind(wx.EVT_BUTTON,fix)
#         #设置退出按钮
#         QuitButton=wx.Button(panel,label='退出',pos=(105,155),size=(50,45))
#         QuitButton.Bind(wx.EVT_BUTTON,quit)
#
#
#         welcomeWin.Show()
#         welcomeApp.MainLoop()
#
#     def refuse(self,name):
#         '''密码错误界面'''
#         refuseApp=wx.App()
#         refuseWin=wx.Frame(None,title='密码错误!',size=(200,200))
#         panel=wx.Panel(refuseWin,-1)
#         text1=wx.StaticText(panel,label='%s,密码错误'%name,pos=(50,50),size=(50,10))
#         refuseWin.Show()
#         refuseApp.MainLoop()
#
#
# def test():
#     '''执行函数'''
#     app=wx.App()
#     main=Main()
#     main.Show()
#     app.MainLoop()
#
# if __name__=='__main__':
#     test()

# # 13-5 几何，Point类，记录X,Y坐标点
# class Point(object):
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#
#     def __str__(self):
#         return '(%s,%s)'%(str(self.x),str(self.y))
#
#     __repr__=__str__

# # 13-6 直线或斜线类
# from math import sqrt
#
# class Line(object):
#     '''线段类'''
#     def __init__(self,x1=0,y1=0,x2=0,y2=0):
#         self.x1=x1
#         self.y1=y1
#         self.x2=x2
#         self.y2=y2
#
#     def __str__(self):
#         return '起点(%s,%s),终点(%s,%s)'%(self.x1,self.y1,self.x2,self.y2)
#
#     __repr__=__str__
#
#     # def __set__(self,obj,newx1,newy1,newx2,newy2):
#     #     self.x1=newx1         #所以__set__这种描述符到底有什么用
#     #     self.y1=newy1
#     #     self.x2=newx2
#     #     self.y2=newy2
#
#
#     def length(self):
#         '''线段长度'''
#         length=sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2)
#         return '线段长度为:%s'%str(length)
#
#     def slope(self):
#         '''线段斜率'''
#         try:
#             slope=float(self.y2-self.y1)/float(self.x2-self.x1)
#             return '线段斜率为：%s'%str(slope)
#         except ZeroDivisionError:
#             return '竖直线无斜率'

#13-7 数据类

# #13-8 堆栈    等学完了《数据结构与算法》，回来试试不用列表的解决办法
# class Stack(object):
#     '''堆栈类,借助列表实现，last-in-first-out,LIFO'''
#     def __init__(self,seq=[]):
#         self.StackList=list(seq)
#
#     def __str__(self):
#         return str(self.StackList)
#
#     __repr__=__str__
#
#     def push(self,elem):
#         '''向堆栈中压入一个数据项'''
#         self.StackList.append(elem)
#
#     def pop(self):
#         '''从堆栈中移出一个数据项'''
#         return self.StackList.pop()
#
#     def isempty(self):
#         '''判断堆栈是否为空，返回0或1'''
#         if bool(len(self.StackList)):
#             return 1
#         else:
#             return 0
#
#     def peek(self):
#         '''取出堆栈顶部的数据项，但不移除'''
#         return self.StackList[-1]

# #13-9 队列类/
# class Queue(object):
#     '''队列类，先进先出，first-in-first-out,FIFO'''
#     def __init__(self,seq=[]):
#         self.QueueList=list(seq)
#
#     def __str__(self):
#         return str(self.QueueList)
#
#     __repr__=__str__
#
#     def enqueue(self,elem):
#         '''在列表的尾部加入一个新的元素'''
#         self.QueueList.append(elem)
#
#     def dequeue(self):
#         '''在列表的头部取出一个元素，返回它并将它移除'''
#         # elem=self.QueueList[0]
#         # del self.QueueList[0]
#         # return elem
#         return self.QueueList.pop(0)

# #13-10 堆栈和队列
# class SAQ(object):
#     def __init__(self,seq=[]):
#         self.SAQList=list(seq)
#
#     def __str__(self):
#         return str(self.SAQList)
#
#     __repr__=__str__
#
#     def shift(self):
#         '''返回并删除列表中的第一个元素'''
#         return self.SAQList.pop(0)
#
#     def upshift(self,elem):
#         '''在列表的头部压入一个新的元素'''
#         self.SAQList.insert(0,elem)
#
#     def push(self,elem):
#         '''在列表尾部加上一个新元素'''
#         self.SAQList.append(elem)
#
#     def pop(self):
#         '''返回并删除列表中的最后一个元素'''
#         return self.SAQList.pop()

# #13-11 电子商务
# '''顾客类User，存货清单类Item，购物车类Cart。可以将多个货物放在购物车里，顾客可以有多个购物车'''
#
# class User(object):
#     '''顾客类'''
#     def __init__(self,name):
#         self.name=name
#         self.Hand={}  #手里的购物车,默认有0个购物车
#
#     def getCart(self):
#         '''获得一个购物车'''
#         i=len(self.Hand.keys())+1   #这是手里的第i个购物车
#         self.Hand[i]=Cart()
#
#     def getItem(self,item,i=1):
#         '''往第i个购物车里添加货物'''
#         if isinstance(item,Item):
#             self.Hand[i].append(item)
#         else:
#             raise TypeError,'只能往购物车里添加已有的货物'
#
#     def askItemPrice(self,item):
#         '''询问单件货物价格'''
#         if isinstance(item,Item):
#             return '货物%s的价格是 %s'%(item.name,str(item.price))
#         else:
#             raise TypeError,'没有这个货物'
#
#     def askAllMoney(self,i=1):
#         '''询问第i个购物车里的货物总价'''
#         if i>len(self.Hand):
#             raise IndexError,'你没有这个购物车'
#         else:
#             return '这个购物车里的货物总价为：%s'%str(self.Hand[i].money())
#
#     def askNums(self,i=1):
#         '''询问车里的货物数量'''
#         return '购物车里的货物数量为:%s'%str(self.Hand[i].nums())
#
# class Item(object):
#     '''货物类，两个属性，名字和价格'''
#     def __init__(self,name,price):
#         self.name=name
#         if isinstance(price,int) or isinstance(price,float):
#             self.price=float(price)
#         else:
#             raise TypeError,'价格应为整型或浮点型'
#
# class Cart(list):
#     '''购物车类，可以查询车内的货物数量和总价格'''
#     def __init__(self):
#         super(Cart,self).__init__()
#
#     def nums(self):
#         '''返回购物车内货物数量'''
#         return len(self)
#
#     def money(self):
#         '''购物车里的货物总价格'''
#         MoneySum=0
#         for i in self:
#             MoneySum+=i.price
#         return MoneySum
#
# def main():
#     '''主体函数，模拟一次购物过程'''
#     mike=User('Mike')   #客户Mike
#     item1=Item('apple',1.50)
#     item2=Item('pear',2.50)
#     item3=Item('banana',3.40)
#     itemList=[item1,item2,item3]
#
#     print '货物总览:'
#     print '-'*20
#     for i in range(3):      #购物菜单
#         print itemList[i].name
#     print '-'*20
#
#     mike.getCart()
#     print 'Mike获得一辆购物车'
#     print
#
#     print 'Mike询问了货物1的价格: '+mike.askItemPrice(item1)
#     print 'Mike询问了货物2的价格: '+mike.askItemPrice(item2)
#     print 'Mike询问了货物3的价格: '+mike.askItemPrice(item3)
#     print
#
#     print 'Mike把货物1,2放入了购物车'
#     mike.getItem(item1)
#     mike.getItem(item2)
#     print
#
#     print 'Mike询问了当前购物车里的货物的货物数目和总价格'
#     print mike.askNums()
#     print mike.askAllMoney()
#     print
#
#     print 'Mike获得第二辆购物车'
#     mike.getCart()
#     print
#
#     print 'Mike继续购买3个苹果和3个香蕉'
#     for i in range(3):
#         mike.getItem(item1,i=2)
#         mike.getItem(item3,i=2)
#
#     print 'Mike询问了第二辆购物车里的货物数目和总价格'
#     print mike.askNums(2)
#     print mike.askAllMoney(2)
#     print
#
#     print '此时购物车1的情况是：'
#     print mike.askNums(1)
#     print mike.askAllMoney(1)
#
# if __name__=='__main__':
    # main()

# 13-12 聊天室
