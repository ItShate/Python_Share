#求五边形面积
import math
r=float(input('请输入五边形的半径：'))
s=2*r*math.sin(math.pi/5)
Area=5*s*s/(4*math.tan(math.pi/5))
print('半径为%.2f的五边形的面积为：%.2f'%(r,Area))
#计算两点之间的大圆距离
radius = 6371.01
x1,y1=eval(input('请输入第一点的经纬度：'))
x2,y2=eval(input('请输入第二点的经纬度：'))
x11=math.radians(x1)
y11=math.radians(y1)
x22=math.radians(x2)
y22=math.radians(y2)
d =radius*math.acos(math.sin(x11)*math.sin(x22)+math.cos(x11)*math.cos(x22)*math.cos(y11-y22))
print('两点之间大圆的距离为：%fkm'%d)
# 计算五角星面积
s=float(input('请输入五角星的边长：'))
Area=5*s*s/(4*math.tan(math.pi/5))
print('边长为%.2f的五角星的面积为%f'%(s,Area))
#计算正多边形的面积
n=int(input('请输入正多边形的边数：'))
s=float(input('请输入正多边形的边长：'))
Area=n*s*s/(4*math.tan(math.pi/n))
print('边长为%.2f的正%d边形的面积为:%f'%(s,n,Area))
# 找出ASCII码字符
A=int(input('请输入一个ASCII值:'))
print('ASCII值为%s的字符为:%s'%(A,chr(A)))
#工资表
name=input('请输入雇员名字：')
week_time=float(input('请输入一周工作时间：'))
pay=float(input('请输入每小时报酬：'))
f_tax=float(input('请输入联邦预扣税：'))
s_tax=float(input('请输入州预扣税：'))
# 获取雇员名字
print('Employee Name:'+name)
print('Hours Worked:%.1f'%(week_time))
print('Pay Rate: $%.2f'%(pay))
# 计算个人总收入
print('Gross Pay:$%.1f'%(week_time*pay))
print('Deductions:')
#计算雇员的联邦预扣税
print(' Federal Wihholding (%.1f%%)：$%.1f'%(f_tax*100,(week_time*pay)*f_tax))
#计算雇员的州预扣税
print(' State Wi thholding (%.1f%%)：$%.2f'%(s_tax*100, (week_time*pay)*s_tax))
#计算雇员总扣除的税
t_deduction=week_time*pay*f_tax+week_time*pay*s_tax
print(' Total Deduction：$%.2f'%t_deduction)
#计算员工的实际工资
print(' Net Pay: $%.2f'%(week_time*pay-t_deduction))
#反向数字
number=int(input('输入一个四位数字：'))
n1=number%10
n2=(number//10)%10
n3=(number//100)%10
n4=number//1000
num=n1*1000+n2*100+n3*10+n4
print(num)
#加密
email='320288355@qq.com'
for e in email:
    a=ord(e)-5
    print(chr(a),end="")