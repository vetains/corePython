#-*- coding:utf-8 -*_
#例9-1

# import os
# for tmpdir in ('/home/vetains/pywork/tmp'):
#     if os.path.isdir(tmpdir):
#         break
# else:   #for循环没有遭遇break时执行else
#     print 'no temp directory avallable'
#     tmpdir=''   #如果=''，在下面的if里不工作
#
# if tmpdir:
#     os.chdir(tmpdir)    #change 改变当前工作目录
#     cwd=os.getcwd()     #cwd 返回当前工作目录
#     print '*** curent temporary directory'
#     print cwd           #是 /
#
#     print '*** creating example directory'
#     os.mkdir('/home/vetains/pywork/tmp/example') #创建目录example
#     os.chdir('/home/vetains/pywork/tmp/example') #改变当前工作目录为example
#     cwd=os.getcwd()
#     print '***new working directory'
#     print cwd
#     print '*** original directory listing'
#     print os.listdir(cwd)
#
#     print '***creating test file...'
#     fobj=open('test','w')
#     fobj.write('foo\n')
#     fobj.write('bar\n')
#     fobj.close()
#     print os.listdir(cwd)
#
#     print "*** renaming 'test' to 'filetest.txt'"
#     os.rename('test','filetest.txt')
#     print '*** updated directory listing'
#     print os.listdir(cwd)
#
#     path=os.path.join(cwd,os.listdir(cwd)[0])   #组合为一个路径名
#     print '*** full file pathname'
#     print path
#     print '***(pathname,basename)=='
#     print os.path.split(path)
#     print '***(filename,extension)=='
#     print os.path.splitext(os.path.basename(path))
#
#     print '*** displaying test file contents'
#     fobj=open(path)
#     for eachline in fobj:
#         print eachline
#     fobj.close()
#
#     print '*** deleting test file'
#     os.remove(path)
#     print '*** updated directory listing:'
#     print os.listdir(cwd)
#     os.chdir(os.pardir)
#     print '*** deleting test directory'
#     os.rmdir('/home/vetains/pywork/tmp/example')
#     print '***Done!'


# # 9-1 文件过滤
# testfile=open('/home/vetains/pywork/pycore/8-10.txt','r')
# testList=testfile.readlines()
# testfile.close()
# for eachLine in testList:
#     if eachLine[0] != '#':  #忽略掉以#开头的文段
#         print eachLine

# # 9-2   文件访问
# F='/home/vetains/pywork/pycore/8-10.txt'
# N=int(raw_input('How many lines:'))
# testfile=open(F,'r')
# txtList=testfile.readlines()
# testfile.close()
# for i in range(N):
#     print txtList[i]
#
# # 9-3 文件信息：总行数
# testfile=open('/home/vetains/pywork/pycore/8-10.txt','r')
# txtList=testfile.readlines()
# testfile.close()
# print len(txtList)

# 9-4 逐页（25行）显示文本
##前期工作：增加8-10.txt的行数
# f=open('/home/vetains/pywork/pycore/8-10.txt','r')
# fList=f.readlines()
# f.close()
# for i in range(50):
#     fList.append(str(i)+'\n')
# print fList
# f=open('/home/vetains/pywork/pycore/8-10.txt','w')
# for eachline in fList:
#     f.write(eachline)
# f.close()

# f=open('/home/vetains/pywork/pycore/8-10.txt','r')
# fList=f.readlines()
# f.close()
# n=len(fList)
# for i in range(n):
#     print '第%s行:'%(i+1),fList[i]
#     if (i+1)%25==0:     #i=24,49时分别为第25,50行
#         raw_input('按任意键继续')

# # 9-6 文件比较
# f1=open('/home/vetains/pywork/pycore/8-10.txt','r')
# f1List=f1.readlines()
# f1.close()
# n1=len(f1List)
# f2=open('/home/vetains/pywork/pycore/8-10_copy.txt','r')
# f2List=f2.readlines()
# f2.close()
# n2=len(f2List)
# n=max(n1,n2)
# for i in range(n):
#     if f1List[i] != f2List[i]:
#         print '第%i行不同'%i
#         print '文件1为%s'%(f1List[i])
#         print '文件2为%s'%(f2List[i])

##试验：定义一个可迭代的函数
def func(n):
    l=[]
    for i in range(n):
        l.append(i*2)

    # for i in range(len(l)):
    #     yield l[i]

    # return iter(l)

    return l

n=10
for i in func(n):
    print i
# 9-7 解析文件
