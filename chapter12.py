#-*- coding:utf-8 -*-

# #在脚本中导入模块？
# import sys
# sys.path.append('/home/vetains/pywork/pycore')
# import chapter11
#
# chapter11.main()    #成功导入并运行，文件夹内新增例chapter11.pyc文件

##一个脚本：检查该目录下文档的总行数
# from os import listdir
#
# folder='/home/vetains/pywork/pycore'
# l=listdir(folder)
# codeList=[]
# for eachfile in l:
#     if eachfile[0] is not '.':
#         f=open(folder+'/'+eachfile,'r')
#         codeList.extend(f.readlines())  #应该用extend而不是append，扩张列表
#         f.close()
#
# print len(codeList) #如果用了append，这里是(13),长度为(13)个列表

# # 12-6 importAs()函数
# def importAs(module):
#     short=__import__(module)    #import module as short
#     return short
#
# a=importAs('operator')
# print a.add(1,1)

#12-7 导入钩子
##zip应用
'''
在当前目录的命令行中，输入
zip -r chapter12.zip chapter12
即可将文件夹chapter12压缩成为chapter12.zip
但文件夹中仍有一目录chapter12,py文件在该目录下
'''
# import sys
# sys.path.append('/home/vetains/pywork/pycore/chapter12.zip/chapter12')
# import chapter11 as easyMath
# easyMath.main()

'''
压缩文件夹内没有目录的方法
首先
zip -r testmodule.zip chapter11.py
将chapter11.py放入zip中，然后-g指令增加
zip -g testmodule.zip chapter.pyc
把pyc文件也放入zip文件中
'''
'''
更直接的方法
zip testmodule.zip chapter11.py chapter11.pyc
就可以了
'''

import sys
sys.path.append('/home/vetains/pywork/pycore/testmodule.zip')
import chapter11 as easyMath
easyMath.main()
