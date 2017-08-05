import string
letters=list(string.letters)
dict1={}
for i in range(10):
    dict1[str(i)]=letters[i]

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

for i in dict1.iterkeys():
    print i

print 'a' in dict1
