# 练习一 字符串
#
# 1. 定义一个字符串Hello Python 并使用print()输出
# 2. 定义第二个字符串Let‘s go并使用print()输出
# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print()输出

str1 = "Hello Python"
print(str1)

str2 = "Let‘s go"
print(str2)

# 或者单双引交替使用
str3 = "\"The Zen of Python\" -- by Tim Peters"
print(str3)


# 练习二 字符串基本操作
#
# 1. 定义两个字符串分别为 xyz 、abc
# 2. 对两个字符串进行连接
# 3. 取出xyz字符串的第二个和第三个元素
# 4. 对abc输出10次
# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出

a = "xyz"
b = "abc"
print(a+b)
print(a[1],b[2])
print(a*10)
for i in range(10):
    print(a)
print('a' in a)
print('a' in b)


# 练习三 列表的基本操作
#
# 1. 定义一个含有5个数字的列表
# 2. 为列表增加一个元素 100
# 3. 使用remove()删除一个元素后观察列表的变化
# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素

list1 = [1,2,3,4,5]
list1.append(100)
print(list1)
list1.remove(5)
print(list1)
print(list1[0:3],list1[-1])


# 练习四 元组的基本操作
#
# 1. 定义一个任意元组，对元组使用append() 查看错误信息
# 2. 访问元组中的倒数第二个元素
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
# 4. 计算元组元素个数

list2 = (1,2,3,4,5)
# list2.append(100)
print(list2[-2])

list3 = ('a','b','c','d','e')
print(list2+list3)

print(len(list2+list3))