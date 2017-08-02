#-*- coding:utf-8 -*-

# P105
s='abcde'
for i in range(-1,-len(s),-1):
    print i
    print s[:i]

print range(-1,-5)      #不合法
print range(-1,-5,-1)   #从-1开始，每步-1
print range(-5,-1)      #从-5开始，每步+1（默认步长）
print range(-5,-1,-1)   #从-5开始，每步-1,不合法

for i in [None]+range(-1,-len(s),-1):  #为了显示全部的abcde，加上None，s==s[:None]
    print i
    print s[:i]
