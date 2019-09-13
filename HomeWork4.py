#1.定级
def grading(sco):
    scores = list(map(int, sco.split(' ')))
    scores_ = list(map(int, sco.split(' ')))
    sco_number = max(scores)
    #sco_number = scores[-1]
    for i in range(len(scores)):
        if scores_ [i] >= (sco_number-10):
            print('Student {} score is {} and grade is A'.format(i,scores[i],))
        elif scores_ [i] >= (sco_number-20):
            print('Student {} score is {} and grade is B'.format(i,scores[i],))
        elif scores_ [i] >= (sco_number-40):
            print('Student {} score is {} and grade is B'.format(i,scores[i],))
        else:
             print('Student {} score is {} and grade is F'.format(i,scores[i],))
scores = input('Enter scores: ')
grading (scores)
#2.逆序读取数字
""" def number(num):
    #将字符串转为列表
    num_=list(num)
    #去除空格，num_.remove(' ')默认自去除一个
    for i in num_:
        if ' ' in num_:
            num_1=num_.remove(' ')
    #逆序输出列表中的元素
    num_2=sorted(num_,reverse=True)
    print(num_2)
num = input('请输入一个整数列表：')
number(num)  """
#统计数字个数
""" def Statistical_char(c):
    #将字符串转化为列表
    char_=c.split(' ')
    print(char_)
    #去除列表中的重复元素,并将元祖转为列表
    char_1 = list(set(char_))
    #统计字符个数
    for i in char_1:
        print('%s occurs %s times'%(i,char_.count(i)))
char = input('Enter integers between 1 and 100:')
Statistical_char(char) """
#4.分析成绩
""" def achievement(ach):
    #将字符串转化为列表
    achievement = ach.split(' ')
    sum_ = 0
    count = 0
    #求平均值
    for i in achievement:
        i = int(i)
        sum_=sum_ + i
        count += 1
    average = sum_ / count
    print(average)
    count_1 = 0
    count_2 = 0
    for i in achievement:
        i = int (i)
        if i >= average :
            count_1+=1
        else :
            count_2+=1
    
    print('低于平均分数的有%d个'%count_2)
    print('大于、等于平均分数的有%d个'%count_1)

ach=input('请输入分数，以空格隔离:')
achievement (ach) """
#5.统计单个数字
import random 
"""    

def counts():
    counts = []
    for i in range(1,11,1):
        num = random.random()
        num=int(num*10000//1000)
        counts.append(num)
    return counts
counts_list = {}
def counts_():
    counts_lis = []
    for j in range(1,11):
        s = counts()
        counts_list.append(s)
    yuan_list = set(counts_list)
    print(yuan_list)
for i in yuan_list:
print('%d出现次数：%d'%(i,counts_list.count(i))) 

#    print(counts_list)
if __name__ == "__main__":
    counts_()
 """
""" ls = list()
ls = [random.randint(0,10) for i in range(1000)]
yuan_list = set(ls)
for i in yuan_list:
    print('%d出现的次数为：%d'%(i,ls.count(i))) """
 #6.找出最小元素的下标
""" def indexOfSmallestElement(lst):
    #将字符串转化为列表，并将字符列表转化为数字列表
    lst_list = list(map(int,lst.split(' ')))
    #将列表转化为字典，去除重复元素
    yuan_list = set(lst_list)
    #将字典转化为列表。
    lst_list_1 = list(yuan_list)
    #查找最小元素
    number = min(lst_list_1)
    #升序
    #lst_list_1.sort()
    #print(lst_list_1)

    #查找最小元素所在第一个索引
    print(lst_list.index(number))
    #print(lst_list.index(lst_list_1[:1]))

lsr = input('请输入数字列表：')
indexOfSmallestElement(lsr) """
#7.随机数选择器
""" import random
def shuffle(lst):
    print(lst)
    list(random.shuffle(lst))
    print(lst)





ls = list(input('请输入一个列表：'))
shuffle(ls) """
#8.消除重复
""" def eliminateDuplicates(lst):
    #将字符转化为列表
    list_ = lst.split(' ')
    #将列表转化字典，并且将字典转化为列表
    list_1 = list(set(list_))
    print('The distinct numbers are:',list_1)

lst = input('Enter ten numbers:')
eliminateDuplicates(lst) """
#9.有序吗？
""" def t_f():
    is_sorted=isSorted()
    #判断函数返回值
    if is_sorted == 1:
        print('The list is not sorted')
    else:
        print('The 1ist is already sorted')

def isSorted():
    list_1 = []
    lst = input ('Enter 1ist:')
    #将字符串转化为列表
    list_ = lst.split(' ')
    list_1 = lst.split(' ')
    #升序
    list_.sort()
    list_2 =list_
    #判断是否为升序
    for i in range(0,len(list_)):
        print(list_1[i])
        print(list_2[i])
        if list_1[i] != list_2[i]:
            return 1
        else:
            continue
if __name__ == "__main__":
    t_f()  """













