<textarea readonly="readonl"name="code"class="Python">
#-*- coding:utf-8 -*-

import os
from string import strip
ls = os.linesep     #辅助换行

def writein(fname): #写入函数，以fname为参数，下同
    all=[]
    print "\n Enter lines ('.'by itself to quit)\n"

    i=0
    while True:
        i+=1
        entry=raw_input('第%s行> '%i)    #提示用户正在输入第几行
        if entry =='.':
            break
        else:
            all.append(entry)

    fobj=open(fname,'w')
    fobj.writelines(['%s%s'%(x,ls) for x in all])   #写入x+ls,其中ls是换行符号
    fobj.close()
    print 'Done!'

def changeline(fname):  #编辑函数
    print
    try:
        fobj=open(fname,'r')
    except IOError,e:
        print e         #直接把错误信息打印出来
    else:
        readout(fname)
        print
        lineList=fobj.readlines()   #获取文件里的所有行的文本，默认是列表
        n=len(lineList)             #获取总行数
        changeN=int(raw_input('there are %d lines,which line do you want change:'%n))
        '''默认会在每行的最后换行，所以不用 n+1。比如有4行文字，第五行会有空行，n还是4'''
        print 'Enter your change:\n'
        lineList[changeN-1]=str(raw_input('正在编辑第%d行:'%changeN))+ls
        '''修改当前的行，并在最后加上ls以换行，否则当下一行会附加在当前行后(因为没换行)'''
        fobj=open(fname,'w')
        fobj.writelines(lineList)
        fobj.close()
        print 'After change:',
        readout(fname)


def readout(fname):     #读取函数
    print
    try:
        fobj=open(fname,'r')
    except IOError,e:
        print "*** file open error:",e
    else:
        allLines=fobj.readlines()
        fobj.close()
        for eachLine in allLines:
            print  strip(eachLine)

def main():             #主体函数
    control=raw_input('[W]rite~~[R]ead~~[C]hange:')
    control.lower()
    if control=='w':
        fname=raw_input('enter a filename:')
        writein(fname)
        print           #换行，下同
        main()          #再次回到主体函数，下同
    elif control=='r':
        fname=raw_input('enter a filename:')
        readout(fname)
        print
        main()
    elif control=='c':
        fname=raw_input('enter a filename:')
        changeline(fname)
        print
        main()
    else:
        print 'Enter W to write'
        print 'Enter R to read'
        print 'Enter C to changeline'
        main()

if __name__=='__main__':    #执行主体函数
    main()
</textarea>
