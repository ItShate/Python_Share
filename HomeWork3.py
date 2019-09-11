#1.五角数
""" n=0
def getPentagonalNumber(n):
    number= n * (3 * n - 1) // 2
    print(number,end="\t")
    n+=1
    if n % 10 == 0:
        print('')
for i in range(1,101):
    getPentagonalNumber(i) """
#2.求一个整数各个数字之和
""" sum = 0
def sumDigits(n):
    global sum
    while(n > 0):
        ys = n % 10
        n = n // 10
        sum = sum+ys
    print('整数和为：%d'%sum)
number = int(input('请输入整数：'))
sumDigits(number) """
#3升序显示
""" def displaySortedNumbers (num1, num2, num3):
    if num1 > num2:
        if num2 > num3:
            print('这三个数升序为：',num3,num2,num1)
        elif num2 < num3 < num1:
            print('这三个数升序为：',num2,num3,num1)
        else :
            print('这三个数升序为：',num2,num1,num3)
    else :#n1<n2
        if num3 < num1:
            print('这三个数升序为：',num3,num1,num2)
        if num1 < num3 < num2:
            print('这三个数升序为：',num1,num3,num2)
        else :
            print('这三个数升序为：',num1,num2,num3)
num_1, num_2, num_3=eval(input('请输入三个数：'))
displaySortedNumbers (num_1, num_2, num_3) """
""" #2.计算未来学费
import math
sum = 0
#计算前十年的总学费
cost_10 = 10000*math.pow((1+0.05),10)
for i in range(11,15):
    #计算后四年总学费
    cost = 10000*math.pow((1+0.05),i)
    sum += cost
print('十年以后的学费为%.2f,十年后的大学四年的总学费为%.2f'%(cost_10,sum)) """
#4.计算未来投资值
""" import math
def futureInvestmentValue(
    investmentAmount, monthlyInterestRate, years):
    money = investmentAmount * math.pow((1+monthlyInterestRate),years)
    print('%.2f'%money)
futureInvestmentValue(10000,0.05/12,50) """
""" import math
def futureInvestmentValue(
    investmentAmount, monthlyInterestRate):
    print('Years \t\t Future Value')
    for i in range(1,31):
        money = investmentAmount * math.pow((1+monthlyInterestRate*0.01),i)
        print('%d\t\t%.2f'%(i,money))

money_b = float(input('The amount i nvested:'))
annual_interest_rate = float(input('The amount i nvested:'))
futureInvestmentValue(money_b,annual_interest_rate) """
#5.显示字符
""" def printChars(ch1, ch2, numberPerLine):
    n = 0
    for i in range(ord(ch1),ord(ch2)+1):
        print(chr(i),' ',end='')
        n+=1
        if n %numberPerLine == 0:
            print('')
ch1 = input('请输入起始的字符ch1：')
ch2 = input('结束的字符ch2：')
numberPerLine=int(input('每行显示个数：'))
printChars(ch1,ch2,numberPerLine) """


#6.计算一年的天数
""" def numberofDaysInAYear(year):

    if year % 4==0 and year % 100 !=0 or year % 400 ==0:
        print('{}年有:366天。'.format(year))
    else:
        print('{}年有:365天。'.format(year))
for y in range(2010,2021):
    numberofDaysInAYear(y) """
#7.显示角
""" import math
radius = 6371.01
def distance(x1,y1,x2,y2):
    x11=math.radians(x1)
    y11=math.radians(y1)
    x22=math.radians(x2)
    y22=math.radians(y2)
    d =radius*math.acos(math.sin(x11)*math.sin(x22)+math.cos(x11)*math.cos(x22)*math.cos(y11-y22))
    print('大圆两点之间的距离为：%.2f'%d)
x1,y1,x2,y2=eval((input('请输入两点的经纬度：')))
distance(x1,y1,x2,y2) """
#8.梅森素数
""" def ms(p):
    for i in  range(2,p):
        for j in range(2,i):
            if i % j != 0 :
                print(i,'是素数')
ms(31) """
""" import math
def prime_number(p):
    print('p\t\t2^p-1')
    for i in range(2,p+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            for k in range(i+1):
                if math.pow(2,k)-1==i:
                    print('%d\t\t%d'%(k,i))                           
prime_number(31) """
""" 
错误
import math
def prime_number(p):
    print('p\t\t2^p-1')
    p_number=int(math.pow(2,p)-1)
    for i in range(2,p+1):
        
        for j in range(i+1):
            j+=1
            if i%j!=0:
                print('%d\t\t%d\t%d'%(i,p_number,j))  
                break                                  
prime_number(31) """
""" #9.当前时间和日期
import time
#将时间戳显示为时间的长格式
time_1=time.localtime(time.time())
#print('时间戳的长格式:',time_1)
#time_2=time.strftime("%Y--%m--%d %H:%M:%S",time_1)
time_2=time.strftime("Current date and time is %m,%d,%Y %H:%M:%S",time_1)
print(time_2) """
#10.掷骰子
""" #编写执行函数
def zx(ztz_1 , ztz_2):
    ztz_z=ztz_1 + ztz_2
    if ztz_z == 2 or ztz_z == 3 or ztz_z == 12:
        print('You ro11ed {} + {} = {}'.format(ztz_1,ztz_2,ztz_z))
        print('You lose')
    elif ztz_z == 7 or ztz_z == 11 :
        print('You ro11ed {} + {} = {}'.format(ztz_1,ztz_2,ztz_z))
        print('You win')
    else :
        print('You ro11ed {} + {} = {}'.format(ztz_1,ztz_2,ztz_z))
        print('point is ',ztz_z)
        ztz()
#编写函数
def ztz():
    ztz_1,ztz_2 = eval(input('请分别输入两个骰子的点数：'))
    zx(int(ztz_1),int(ztz_2))
#调用主函数，设计程序入口
if __name__ == "__main__":
    ztz() """




