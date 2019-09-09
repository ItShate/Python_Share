#摄氏度转化为华氏度
c=int(input('请输入摄氏度：')) 
f=(9/5)*c+32
print('摄氏度为%d的华氏度为%.1f'%(c,f))
#计算圆柱体积
import math
r,h=eval(input('请输入圆柱体的半径和高'))
area=r*r*math.pi
volume=area*h
print('圆柱体的地面积为%.4f'%area)
print('圆柱体的体积为%.1f'%volume)
#英尺与米数转换
y=float(input('请输入英尺：'))
meter=y*0.305
print('%.1f英尺等于%0.4f米'%(y,meter))
#能量计算
m=float(input('请输入水的质量：'))
i=float(input('请输入水的初始温度：'))
f=float(input('请输入水的最终温度：'))
q=m*(f-i)*4184
print('所需要的能量为：%0.1f'%q)
#利息计算
e,g=eval(input('Enter balance and interest rate (e.g., 3 for 3%): '))
l=e*g/1200
print('The interest is %0.5f'%l) """
#计算加速度
""" v0,v1,t=eval(input('Enter v0, v1, and t:'))
a=(v1-v0)/t
print('The average acceleration is %0.4f'%a)
#复利值
i=1
sum=0
number=float(input('Enter the monthly saving amount: '))
while i<=6:
    sum=(sum+number)*(1+0.00417)
    i+=1
print('After the sixth month, the account value is %.2f'%sum)
#对0-1000的整数的各位数字求和
number=int(input('Enter a number between 0 and 1000: '))
sum=0
while number>0 :
    num=number%10
    sum=sum+num
    number=number//10
print('The sum of the digits is ',sum)


