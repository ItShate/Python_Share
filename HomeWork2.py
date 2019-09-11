#7.18
#1.代数
import math
a,b,c = eval(input('Enter a, b, c: '))
p = b*b-4*a*c
if p > 0:
    r1 = (-b+math.sqrt(p))/2*a
    r2 = (-b-math.sqrt(p))/2*a
    print('The roots are %.6f and %.5f'%(r1,r2))
elif p == 0:
    r0 = -(b/2*a)
    print('The root is %f'%r0)
else:
    print('The equation has no real roots')
#2.学习加法
import numpy as np
res1 = np.random.choice(range(1,100))
res2 = np.random.choice(range(1,100))
print('系统产生的随机数为：{}、{}'.format(res1,res2))
num = int(input('请输入这两个随机数的和:'))
if num == res1+res2:
    print('程序报告正确!')
else :
    print('程序报告错误!')
#3.找未来数据
day=int(input('Enter today\'s day:'))
num_day=int(input('Enter the number of days elapsed since today:'))
today=(day+num_day%7)%7
if today == 1:
    today_str = 'Monday'
elif today == 2:
    today_str = 'Tuesday'
elif today == 3:
    today_str = 'Wednesday'
elif today == 4:
    today_str = 'Thursday'
elif today == 5:
    today_str = 'Friday'
elif today == 6:
    today_str = 'Saturday' 
elif today == 0:
    today_str = 'Sunday'  
print('Today is Sunday and the future day is ',today_str)
#4.对三个数排序
num_1,num_2,num_3 = eval(input('请输入三个数：'))
if num_1 > num_2:
    if num_2 > num_3:
        print(num_3,num_2,num_1)
    elif num_2 < num_3 < num_1:
        print(num_2,num_3,num_1)
    else :
        print(num_2,num_1,num_3)
else :#n1<n2
    if num_3 < num_1:
        print(num_3,num_1,num_2)
    if num_1 < num_3 < num_2:
        print(num_1,num_3,num_2)
    else :
        print(num_1,num_2,num_3)

#5.金融——比较价钱
package1_1,package1_2 = eval(input('Enter weight and price for package 1: '))
package2_1,package2_2 = eval(input('Enter weight and price for package 2: '))
price_1 = package1_1/package1_2
price_2 = package2_1/package2_2
if price_1 > price_2:
    print('Package 1 has the better price.')
else :
    print('Package 2 has the better price.')
#6.找出一个月中的天数
month,year = eval(input('请输入月和年：'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    if month == 2:
        print('%d年%d月有29天'%(year,month))
else :
    if month in [1,3,5,7,8,10,12]:
        print('%d年%d月有31天'%(year,month))
    elif month in [4,6,9,11]:
        print('%d年%d月有30天'%(year,month))
    else :
        print('%d年%d月有28天'%(year,month)) 
#7.游戏——头和尾
 import numpy 
res = numpy.random.choice(['正','反'])
guess_number = input('请输入猜测的硬币的正、反面：')
print('程序的硬币正反面：%s'%res)
if guess_number == res:
    print('猜测值正确！')
else:
    print('猜测值错误！')
#8.石头、剪刀、布
import numpy
num_py=int(numpy.random.choice([0,1,2]))
guess_num=int(input('scissor (0), rock (1)， paper (2): '))
print("The computer is:",num_py)
gest=['scissor','rock','paper']
if guess_num == num_py:
    print('The computer is {0}. You are {1} too.It is a draw.'.format(gest[num_py],gest[guess_num]))
elif guess_num == 0 and num_py == 2 or guess_num == 1 and num_py == 0 or guess_num == 2 and num_py == 1 :
    print('The computer is {0}. You are {1}. You won'.format(gest[num_py],gest[guess_num]))
else:
    print('The computer is {0}. You are {1}. You fail'.format(gest[num_py],gest[guess_num]))
#9.
import math
year = int(input('Enter year: (e.g.. 2008): '))
month = int(input('Enter month: 1-12: '))
q = int(input('Enter the day of the month: 1- 31:'))
j  =round(year/100)
k = year%100
week = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday',]
if month < 3:
    m = month+12
else:
    m = month
h = (q+math.floor(26*(m+1)/10)+k+math.floor(k/4)+math.floor(j/4)+5*j)%7
print('Day of the week is {}'.format(week[h]))
#10.游戏—选择一张牌(梅花、红桃、方块、黑桃)
import numpy
colour = numpy.random.choice(['plum blossom','Heart','block','Spade'])
number = numpy.random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
print('The card you picked is the {} of {}'.format(colour,number))

#11.判断回文数
#方法一:
number = int(input('Enter a three-digit integer:'))
if number//100 == number%10:
    print('%d is a palindrome'%number)
else:
    print('%d is not a palindrome'%number)
#方法二:
number = int(input('Enter a three-digit integer:'))
number_str = str(number)
if number_str[0] == number_str[-1]:
    print('%d is a palindrome'%number)
else:
    print('%d is not a palindrome'%number)
#12.计算三角形的周长
edges_1,edges_2,edges_3 = eval(input('Enter three edges: '))
if edges_1 + edges_2 > edges_3 and edges_1 + edges_3 > edges_2 and edges_3 + edges_2 > edges_1 :
    print('The perimeter is ',edges_1+edges_2+edges_3)
else:
    print('Input is illegal!')
#7.19
#1.统计正数、负数个数并求平均值
number=1
num_1=-1
num_2=0
sum_1=-1
sum_2=0
while(number!=0):
    if number > 0:
        sum_1=sum_1+number
        num_1+=1
    elif number < 0:
        sum_2=sum_2+number
        num_2+=1
    number = int(input('Enter an integer, the input ends if it is 0: '))
print('正数个数：%d,负数个数：%d,平均值：%.2f'%(num_1,num_2,(sum_1+sum_2)/(num_1+num_2))) 
#2.计算未来学费
import math
sum = 0
#计算前十年的总学费
cost_10 = 10000*math.pow((1+0.05),10)
for i in range(11,15):
    #计算后四年总学费
    cost = 10000*math.pow((1+0.05),i)
    sum += cost
print('十年以后的学费为%.2f,十年后的大学四年的总学费为%.2f'%(cost_10,sum))
#4.可被5和6同时整除的数
n=0
for i in range(100,1001):
    if i%5 ==0 and i%6 == 0:
        n += 1
        print(i,end=" ")
        if n%10 == 0:
            print("")
#5.找出最小的n
n=1
while(n*n <= 12000):
    n+=1
print('满足n*n>12000的最小n为：',n)
#7.消除错误
sum_1=0
sum_2=0
for i in range(1,5001):
    num_1=1/i
    sum_1+=num_1
    #反向
    num_2=1/(5001-i)
    sum_2+=num_2
print('从左向右的和为:%f,从右向左的和为:%.f，左向右与右向左的差为：%f'%(sum_1,sum_2,sum_1-sum_2))
#8.数列求和
sum = 0
for i in range(1,98,2):
    number = i/(i+2)
    sum += number
print(sum)
#9.计算π
for j in range(10000,100001,10000) :
    sum=0
    for i in range(1,j+1):
        if i%2 != 0:
            num = 1/(2*i-1)
        else :
            num = (-1)*(1/(2*i-1))
        sum = sum+num
    pi = 4*sum
    print('{}是的π值为：{}'.format(j,pi))
#10.完全数
n=0
for i in range(1,10000):
    t = i
    # a_list=[]
    for j in range(1,i):
        if i % j == 0:
            # a_list.append(j)
            t -= j
    if t == 0:
        print(i,'是完全数')
        n+=1    
print('10000以内完全数有：',n)
#11.数学问题——组合
import numpy
#随机产生两个数
 num_1 = numpy.random.choice([1,2,3,4,5,6,7])
num_2 = numpy.random.choice([1,2,3,4,5,6,7])
n=0
for i in range(1,num_1+1):
    for j in range(1,num_2+1):
        print(i,j)
        n += 1
print('The total number of al1 combinations is ',n)




