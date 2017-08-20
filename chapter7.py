#-*- coding:utf-8 -*-
# import string
# letters=list(string.letters)
# dict1={}
# for i in range(10):
#     dict1[str(i)]=letters[i]

# for key in dict1:
#     print '%s:%s'%(key,dict1[key])
#
# print 1 not in dict1
# print 'letter %(1)s and letter %(2)s'%dict1
#
# for eachKey in sorted(dict1):
#     print '%s:%s'%(eachKey,dict1[eachKey])
#
# print sorted(dict1)

# for i in dict1.iterkeys():
#     print i
#
# print 'a' in dict1

# 7-3
# import string
# letters=list(string.letters)
# myDict={}
# for i in range(10):
#     myDict[str(i)]=letters[i]
# for eachKey in sorted(myDict):  #将键排序并将键值对显示出来
#     print '%s: %s'%(eachKey,myDict[eachKey])

# # 7-4
# list1=[1,2,3,4]
# list2=['abc','def','hij','klm']
#
# myDict=dict(zip(list2,list1))
# print myDict

# 7-5   #未完成
import shelve
import wx
from time import ctime,time
import sys


class Creation(wx.Frame):
    '''一个询问界面'''
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'一个询问',pos=(60,60),size=(250,300))
        panel=wx.Panel(self,-1)
        self.text1=wx.StaticText(panel,label='你是否要注册一个账户？',
                                 pos=(50,50),size=(180,40))
        self.button1=wx.Button(panel,label='是',pos=(60,100),size=(40,25))
        self.button1.Bind(wx.EVT_BUTTON,self.LogOnClick)
        self.button2=wx.Button(panel,label='否',pos=(100,100),size=(40,25))
        self.button2.Bind(wx.EVT_BUTTON,self.QuitClick)

    def QuitClick(self,event):
        self.Destroy()
    def LogOnClick(self,enent):
        logon=LogOn()
        logon.Show()
        self.Destroy()

class LogOn(wx.Frame):
    '''一个注册界面'''
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'创建账户',size=(400,250))
        panel=wx.Panel(self,-1)
        #用户名与密码文本框
        db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
        now=ctime(time())   #now是由ctime()返回的
        self.text1=wx.StaticText(panel,label='用户名:',pos=(50,50),size=(50,25))
        self.text2=wx.StaticText(panel,label='密码:',pos=(50,70),size=(50,25))
        self.textCtrl1=wx.TextCtrl(panel,pos=(105,50),size=(75,25))
        self.textCtrl2=wx.TextCtrl(panel,pos=(105,70),size=(75,25))
        self.name=str(self.textCtrl1.GetValue())
        self.password=str(self.textCtrl2.GetValue())
        #注册按钮
        self.button1=wx.Button(panel,label='注册',pos=(65,100),size=(40,30))
        # self.button1.Bind(wx.EVT_BUTTON,lambda event,\
        #     n=self.name,p=self.password:self.CreateClick(event,n,p))
        self.button1.Bind(wx.EVT_BUTTON,self.CreateClick)
        #取消按钮
        self.button2=wx.Button(panel,label='取消',pos=(105,100),size=(40,30))
        self.button2.Bind(wx.EVT_BUTTON,self.QuitClick)

    def QuitClick(self,event):
        '''取消事件'''
        self.Destroy()

    def CreateClick(self,event):
        '''注册事件'''
        name=str(self.textCtrl1.GetValue())
        password=str(self.textCtrl2.GetValue())

        db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
        now=ctime(time())   #now是由ctime()返回的字符串
        newUser={'password':password,'time':now}
        db[name]=newUser
        db.close()
        self.Destroy()

class adminMenue(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'管理菜单',size=(600,600))
        panel=wx.Panel(self,-1)
        db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
        nameList=[]
        pwList=[]
        timeList=[]
        for eachKey in db.keys():
            nameList.append(eachKey)
            pwList.append(db[eachKey]['password'])
            timeList.append(db[eachKey]['time'])
        db.close()
        nameStr='名单列表:\n'+'\n'.join(nameList)
        pwStr='密码列表:\n'+'\n'.join(pwList)
        timeStr='登录时间:\n'+'\n'.join(timeList)
        self.text1=wx.StaticText(panel,label=nameStr,pos=(50,50),size=(200,200))
        self.text2=wx.StaticText(panel,label=pwStr,pos=(150,50),size=(200,200))
        self.text3=wx.StaticText(panel,label=timeStr,pos=(250,50),size=(200,200))

class Main(wx.Frame):
    '''主界面'''
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'主界面',size=(360,240))
        panel=wx.Panel(self,-1)
        #用户名
        self.text1=wx.StaticText(panel,label='用户名:',pos=(10,10),size=(100,50))
        self.textCtrl1=wx.TextCtrl(panel,pos=(100,10),size=(100,10))
        # name=str(textCtrl1.GetValue())    #像这样直接获取文本框的文本是不可行的.
        #密码
        self.text2=wx.StaticText(panel,label='密码:',pos=(10,60),size=(100,50))
        self.textCtrl2=wx.TextCtrl(panel,pos=(100,60),size=(100,0))
        # password=str(textCtrl2.GetValue())

        #登录按钮
        self.logInButton=wx.Button(panel,-1,label='登录',pos=(30,180),size=(100,50))
        self.logInButton.Bind(wx.EVT_BUTTON,self.logInClick)
        #菜单按钮
        self.adminMenuButton=wx.Button(panel,-1,label='菜单管理',pos=(130,180),size=(100,50))
        self.adminMenuButton.Bind(wx.EVT_BUTTON,self.adminMenuClick)
        #退出按钮
        self.quitButton=wx.Button(panel,-1,label='退出',pos=(230,180),size=(100,50))
        self.quitButton.Bind(wx.EVT_BUTTON,self.quitClick)

    def adminMenuClick(self,event):
        '''菜单按钮事件'''
        admin=adminMenue()
        admin.Show()

    def quitClick(self,event):
        '''退出按钮事件'''
        sys.exit()

    def logInClick(self,event):
        '''登录按钮事件'''

        name=str(self.textCtrl1.GetValue())
        password=str(self.textCtrl2.GetValue())

        db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
        keyList=db.keys()
        db.close()

        if name in keyList:

            db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
            dbPassword=db[name]['password']
            db.close()

            if password==dbPassword:
                '''用户名已存在且密码正确则唤起欢迎界面'''
                self.welcome(name,password)
            else:
                '''密码错误唤起密码错误界面'''
                self.refuse(name)
        else:
            '''用户名不存在则询问是否注册'''
            creation=Creation()
            creation.Show()

    def welcome(self,name,password):
        '''欢迎界面'''
        welcomeApp=wx.App()
        welcomeWin=wx.Frame(None,title='欢迎!',size=(400,400))
        panel=wx.Panel(welcomeWin,-1)

        welStr='欢迎,%s,你的上次登录时间为'
        text1=wx.StaticText(panel,label=welStr%name,pos=(50,50),size=(500,20))
        db=shelve.open('/home/vetains/pywork/pycore/chapter7.dat')
        lastTime=db[name]['time']    #上次登录时间
        now=ctime(time())            #更新登录时间
        db[name]={'password':password,'time':now}
        db.close()

        text2=wx.StaticText(panel,label=lastTime,pos=(50,80),size=(250,20))

        welcomeWin.Show()
        welcomeApp.MainLoop()

    def refuse(self,name):
        '''密码错误界面'''
        refuseApp=wx.App()
        refuseWin=wx.Frame(None,title='密码错误!',size=(200,200))
        panel=wx.Panel(refuseWin,-1)
        text1=wx.StaticText(panel,label='%s,密码错误'%name,pos=(50,50),size=(50,10))
        refuseWin.Show()
        refuseApp.MainLoop()




# def main():
#     app=wx.App()
#     win=wx.Frame(None,title='Log in System',pos=(50,50),size=(360,240))
#     panel=wx.Panel(win,-1)
#
#     #用户名
#     text1=wx.StaticText(panel,label='用户名:',pos=(10,10),size=(100,50))
#     textCtrl1=wx.TextCtrl(panel,pos=(100,10),size=(100,10))
#     name=str(textCtrl1.GetValue())
#     #密码
#     text2=wx.StaticText(panel,label='密码:',pos=(10,60),size=(100,50))
#     textCtrl2=wx.TextCtrl(panel,pos=(100,60),size=(100,0))
#     password=str(textCtrl2.GetValue())
#
#     #登录按钮
#     logInButton=wx.Button(panel,-1,label='登录',pos=(30,180),size=(100,50))
#     logInButton.Bind(wx.EVT_BUTTON,\
#             lambda event,n=name,p=password:logInClick(event,n,p))
#     #菜单按钮
#     adminMenuButton=wx.Button(panel,-1,label='菜单管理',pos=(130,180),size=(100,50))
#     adminMenuButton.Bind(wx.EVT_BUTTON,adminMenuClick)
#     #退出按钮
#     quitButton=wx.Button(panel,-1,label='退出',pos=(230,180),size=(100,50))
#     quitButton.Bind(wx.EVT_BUTTON,quitClick)
#     win.Show()
#     app.MainLoop()

def test():
    app=wx.App()
    main=Main()
    main.Show()
    app.MainLoop()

if __name__=='__main__':
    test()

# # 7-7
# def new_dict(oldDict):
#     newDict={}
#     length=len(oldDict)
#     for eachKey in oldDict.keys():
#         newDict[oldDict[eachKey]]=eachKey   #旧字典的值作键，键作值
#     return newDict
#
# a={'a':1,'b':2}
# print new_dict(a)

# # 7-8 雇员和编号
# import shelve
#
# def newGuy():
#     name=str(raw_input('姓名:'))
#     No=str(raw_input('编号:'))
#     db=shelve.open('/home/vetains/pywork/pycore/7-8.dat')
#     db[No]=name
#     db.close()
#     print 'Done!'
#
# def Look():
#     db=shelve.open('/home/vetains/pywork/pycore/7-8.dat')
#     if db.keys():
#         keys=db.keys()
#         keys.sort()     #使雇员按编号排列，方便查阅
#         for eachKey in keys:
#             print '编号:'+eachKey+' 姓名:'+db[eachKey]
#         db.close()
#     else:
#         print '档案为空，请往档案中添加资料'
#         db.close()
#
# def main():
#     inp=str(raw_input('查阅(L)，增加(A)'))
#     inp=inp.lower()
#     if inp=='l':
#         Look()
#         main()
#     elif inp=='a':
#         newGuy()
#         main()
#
# if __name__=='__main__':
#     main()

# 7-9
# #（a)
# srcstr='abc'
# dststr='mno'      #len(srcstr)==len(dststr)
# aim_string='abcdef'
# def tr(srcstr,dststr,aim_string):
#     new_string=''
#     n=len(aim_string)
#     for i in range(n):
#         if aim_string[i] in srcstr:         #如果该字符在翻译里
#             k=srcstr.index(aim_string[i])   #获得目标位置的索引
#             new_chr=dststr[k]               #新字符从dststr里得到
#         else:
#             new_chr=aim_string[i]           #否则新字符按原字符
#         new_string=new_string+new_chr
#     return new_string
#
# print tr(srcstr,dststr,aim_string)

# #（c)
#
# srcstr='abcdef'
# dststr='mno'        #len(srcstr)>=len(dst)
# aim_string='abcdefghi'
# def tr(srcstr,dststr,aim_string):
#     new_string=''
#     n=len(aim_string)
#     for i in range(n):
#         if aim_string[i] in srcstr:
#             k=srcstr.index(aim_string[i])
#             try:
#                 new_chr=dststr[k]
#             except IndexError:  #如果字符在dststr里没有，则删除
#                 new_chr=''
#         else:
#             new_chr=aim_string[i]
#         new_string=new_string+new_chr
#     return new_string
#
# print tr(srcstr,dststr,aim_string)

# # 7-10  rot13加密
# #(a)
# import string
# low_letters=list(string.letters[:26])
# up_letters=list(string.letters[26:])
#
# def JiaMi(aimString):
#     n=len(aimString)
#     newString=''
#     for i in range(n):
#         if aimString[i] in low_letters:
#             k=13+low_letters.index(aimString[i])
#             if k>25:
#                 k=k-26
#             new_chr=low_letters[k]
#         elif aimString[i] in up_letters:
#             k=13+up_letters.index(aimString[i])
#             if k>25:
#                 k=k-26
#             new_chr=up_letters[k]
#         else:
#             new_chr=aimString[i]
#         newString+=new_chr
#     return newString
#
# aimString=str(raw_input('待加密字符：'))
# print JiaMi(aimString)


# def JieMi(aimString):
#     n=len(aimString)
#     newString=''
#     for i in range(n):
#         if aimString[i] in low_letters:
#             k=-13+low_letters.index(aimString[i])
#             if k<0:
#                 k=k+26
#             new_chr=low_letters[k]
#         elif aimString[i] in up_letters:
#             k=-13+up_letters.index(aimString[i])
#             if k<0:
#                 k=k+26
#             new_chr=up_letters[k]
#         else:
#             new_chr=aimString[i]
#         newString+=new_chr
#     return newString
# aimString=str(raw_input('待解密字符：'))
# print JieMi(aimString)
