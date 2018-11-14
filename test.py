import re



data1=(u'00088d4b41a34b1db8f390b3238e04e5', u'tmpadbpept02', u'146.240.75.23', None,
       None, None, None, None, u'2', u'1',
       None,  u'system', None, 0L, None)
data2=(u'00088d4b41a34b1db8f390b3238e04e5', u'hsmapept02', u'146.240.75.23', None,
       None, None, None, None, u'2', u'1',
       None,  u'system', None, 0L, None)
data3=(u'00088d4b41a34b1db8f390b3238e04e5', u'tmpaproxyt02', u'146.240.75.23', None,
       None, None, None, None, u'2', u'1',
       None,  u'system', None, 0L, None)
data = (data1,data2,data3)
print len(data)
num=0
for each in data:
    if re.search('db',each[1]) is not None or re.search('hsm',each[1]) or re.search('proxy',each[1]):
        num=num+1
print num