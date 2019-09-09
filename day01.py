#求100以内所有数的和
""" i=1
sum=0
while i<=100:
    sum=sum+i
    i+=1
print(sum) """
#如何用一行代码转换a b的值
#a,b=1,21
#print(a,b)

#print("100"+"100")
'''
a=input('请输入：')
print(a,type(a))

a=float(input('请输入数字：'))
b=float(input('请输入数字：'))
print('%.2f-%.2f=%.2f'%(a,b,a-b))
'''
# a=float(input('请输入数字：'))
# b=float(input('请输入数字：'))
# print('{}-{}={}'.format(a,b,a-b))
""" a=float(input('请输入数字：'))
b=float(input('请输入数字：'))
c=float(input('请要进行的运算方式：'))
if c==+:
    print('{}+{}={}'.format(a,b,a+b)) """
""" a=97
print(chr(a))
b='a'
print(ord(b)) """
""" # 对email进行加密
email='1440067010@qq.com'
for e in email:
    a=ord(e)
    b=a-5
    print(chr(b)) """
# 对email进行加密
# email='1440067010@qq.com'
# for e in email:
#     a=ord(e)
#     b=a-5
#     print(chr(b),end="") 

""" email='1440067010@qq.com'
# 导入hash包
import hashlib
# 创建MD5对象，可以直接传入要加密的数据
m=hashlib.md5(email.encode(encoding='utf-8'))
# 转化为16进制打印md5值
email_md5=m.hexdigest()
print('md5加密前的email为%s,md5加密后的email为%s'%(email,email_md5))

import hashlib
email='1440067010@qq.com'
email_md5=hashlib.md5(email.encode(encoding='UTF-8')).hexdigest()
print('md5加密前的email为%s,md5加密后的email为%s'%(email,email_md5)) """

""" import hashlib
m=hashlib.md5()
a=input('请输入字符串：')
m.update """
""" s = 'ABCDLSESRF'
s14 = s[-1::-1]
print(s14)
s15 = s[::-1]
print(s15) """
""" a='100'
b=100
print(a==b)

c=200
d=200
print(c is d)   #is比较内存地址
print(id(c))
print(id(d))
#in是判断在容器中（可迭代对象—可以被for循环）有无该东西
a='I am hph'
print('am' in a)
print('hh' is not a)
 """
""" # 输入一个年份，判断是否是闰年
y=int(input('输入一个年份:'))
if (y%4==0 and y%100!=0) or y%400==0:
    print('%d是闰年'%y)
else:
    print('%d不是闰年'%y) """
# 输入一个月，判断有多少天
""" mouth=int(input('输入月份：'))
mouth_1=[1,3,5,7,8,10,11]
if mouth in mouth_1:
    print('%d月有31天'%mouth)
else :
    print('%d月有30天'%mouth) """

""" 将化氏度转化为摄氏度
F=float(input('输入一个华氏度：'))
C=(F-32)/1.8
print('%.2f转化摄氏度为%.2f'%(F,C)) """

#判断三位数是否为水仙花数
a=int(input('请输入一个三位数：'))
b=a%10
c=(a//10)%10
d=(a//100)
#print(b,c,d)
if b **3 + c**3 + d**3==a:
    print('%d数为水仙花数'%a)
else :
    print('%d数为水仙花数'%a)

