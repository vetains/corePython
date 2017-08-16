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
# import shelve
# import wx
# import time
# import sys
#
# # class Welcome(wx.Frame):
# #     def __init__(self):
# #         wx.Frame.__init__(self,None,-1,'Welcome',size=(200,200))
# #         self.panel=wx.Panel(self,-1)
#
#
# class Creation(wx.Frame):   #这是一个询问界面
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'一个询问',pos=(60,60),size=(200,300))
#         panel=wx.Panel(self,-1)
#         self.text1=wx.StaticText(panel,label='你是否要注册一个账户？',
#                                  pos=(50,50),size=(150,40))
#         self.button1=wx.Button(panel,label='是',pos=(60,100),size=(40,20))
#         self.button1.Bind(wx.EVT_BUTTON,self.LogOnClick)
#         self.button2=wx.Button(panel,label='否',pos=(100,100),size=(40,20))
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
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'创建账户',size=(500,500))
#         panel=wx.Panel(self,-1)
#         self.text1=wx.StaticText(panel,label='用户名:',pos=(50,50),size=(40,20))
#         self.text2=wx.StaticText(panel,label='密码:',pos=(50,70),size=(40,20))
#         self.textCtrl1=wx.TextCtrl(panel,pos=(90,50),size=(75,10))
#         self.textCtrl2=wx.TextCtrl(panel,pos=(90,70),size=(75,10))
#         self.name=str(self.textCtrl1.GetValue())
#         self.password=str(self.textCtrl2.GetValue())
#         self.button1=wx.Button(panel,label='创建账户',pos=(160,100),size=(40,20))
#         self.button1.Bind(wx.EVT_BUTTON,
#                 lambda event,n=self.name,p=self.password:self.CreateClick(event,n,p))
#         self.button2=wx.Button(panel,label='取消',pos=(200,100),size=(40,20))
#         self.button2.Bind(wx.EVT_BUTTON,self.QuitClick)
#
#     def QuitClick(self,event):
#         self.Destroy()
#     def CreateClick(self,event,name,password):
#         db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
#         db[name]=[]
#         db[name].append(password)
#         db[name].append(time.strftime("%Y-%m-%d %X"))
#         db.close()
#         self.Destroy()
#
# class adminMenue(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,'管理菜单',size=(600,600))
#         panel=wx.Panel(self,-1)
#         db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
#         nameList=[]
#         pwList=[]
#         for eachKey in db:
#             nameList.append(str(eachKey))
#             pwList.append(str(db[eachKey][0]))
#         db.close()
#         nameStr='名单列表:\n'+'\n'.join(nameList)
#         pwStr='密码列表:\n'+'\n'.join(pwList)
#         self.text1=wx.StaticText(panel,label=nameStr,pos=(50,50),size=(200,200))
#         self.text2=wx.StaticText(panel,label=pwStr,pos=(150,50),size=(200,200))
#
# def welcome(name,password):
#     welcomeApp=wx.App()
#     welcomeWin=wx.Frame(None,title='Welcome',size=(200,2000))
#     panel=wx.Panel(welcomeWin,-1)
#     text1=wx.StaticText(panel,label='Welcome,%s'%name,pos=(50,50),size=(50,10))
#     db=shelve.open(r'/home/vetains/pywork/pycore/charpter7.dat')
#     lastTime=db[name][1]
#     db[name][1]=time.strftime("%Y-%m-%d %X")
#     db.close()
#     text2=wx.StaticText(panel,label=lastTime,pos=(50,60),size=(50,10))
#     welcomeWin.show()
#     welcomeApp.MainLoop()
#
#
# def logInClick(event,name,password):
#     db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
#     keyList=db.keys()
#     db.close()
#     if name in keyList:
#         welcome(name,password)
#     else:
#         creation=Creation()
#         creation.Show()
#
# def adminMenuClick(event):
#     admin=adminMenue()
#     admin.Show()
#
# def quitClick(event):
#     sys.exit()
#
#
# def main():
#     db=shelve.open(r'/home/vetains/pywork/pycore/chapter7.dat')
#     app=wx.App()
#     win=wx.Frame(None,title='Log in System',pos=(50,50),size=(360,240))
#     panel=wx.Panel(win,-1)
#
#     text1=wx.StaticText(panel,label='User\'s Name:',pos=(10,10),size=(100,50))
#     textCtrl1=wx.TextCtrl(panel,pos=(100,10),size=(100,10))
#     name=str(textCtrl1.GetValue())
#     text2=wx.StaticText(panel,label='Password:',pos=(10,60),size=(100,50))
#     textCtrl2=wx.TextCtrl(panel,pos=(100,60),size=(100,0))
#     password=str(textCtrl2.GetValue())
#
#     logInButton=wx.Button(panel,-1,label='Log IN',pos=(30,180),size=(100,50))
#     logInButton.Bind(wx.EVT_BUTTON,lambda event,n=name,p=password:logInClick(event,n,p))
#     adminMenuButton=wx.Button(panel,-1,label='Admin Menu',pos=(130,180),size=(100,50))
#     adminMenuButton.Bind(wx.EVT_BUTTON,adminMenuClick)
#     quitButton=wx.Button(panel,-1,label='Quit',pos=(230,180),size=(100,50))
#     quitButton.Bind(wx.EVT_BUTTON,quitClick)
#     win.Show()
#     app.MainLoop()
#
# if __name__=='__main__':
#     main()

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

# 7-10  rot13加密
#(a)
import string
low_letters=list(string.letters[:26])
up_letters=list(string.letters[26:])

def JiaMi(aimString):
    n=len(aimString)
    newString=''
    for i in range(n):
        if aimString[i] in low_letters:
            k=13+low_letters.index(aimString[i])
            if k>25:
                k=k-26
            new_chr=low_letters[k]
        elif aimString[i] in up_letters:
            k=13+up_letters.index(aimString[i])
            if k>25:
                k=k-26
            new_chr=up_letters[k]
        else:
            new_chr=aimString[i]
        newString+=new_chr
    return newString

aimString=str(raw_input('待加密字符：'))
print JiaMi(aimString)


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
