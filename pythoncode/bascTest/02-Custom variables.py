score = 100     #定义了一个变量,这个变量的名字叫做score,它里面存储了一个数值 100
high = 180      #单位是cm

# 赋值
#count1=count2=count3=1
count1,count2,count3=1,2,3

# 换行
count = count1 + count2 + count3; print(count)

applePrice = 3.5    #苹果的价格 元/斤
weight = 7.5        #购买的苹果的重量 斤

money = applePrice * weight     #如果money=xxxx是第一次的话,那么就表示定义了一个变量

money = money - 10      #如果 money=xxxx不是第一次出现,那么就不是定义变量,而是给这个已经存在的变量赋上一个新的值

print(money)

print(type(money))


a, b, c, d = 10, 8.8, True, 2+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))