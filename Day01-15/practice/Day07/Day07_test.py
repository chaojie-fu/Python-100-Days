# 单引号与双引号是否存在区别
str1 = 'hello world'
str2 = "hello world"
print(str1 == str2)
# 似乎没有区别

# ---------------------------------------------------------[列表]---------------------------------------------------------
list1 = [1, 3, 5, 7, 100]
list1.remove(3)
print(list1)
# str = 'hello'
# str.remove('h')
# str.remove(0)
# 以上注释掉的语句都会报错，remove不适用于字符串

# ---------------------------------------------------------(元组)---------------------------------------------------------

# ---------------------------------------------------------{集合}---------------------------------------------------------
# 集合自动除去重复的元素
set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = set(range(1, 10))
print(set2)
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
print(set1)
print(set2)
# remove的元素如果不存在会引发KeyError
print('-------------------------------------------')
# 将元组转换成集合
set3 = set((1, 2, 3, 3, 2, 1))
print(set3.pop())
print(set3)
print('-------------------------------------------')
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
print('-------------------------------------------')
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
# ---------------------------------------------------------{字典}---------------------------------------------------------
# ---------------------------------------------------------{键:值}---------------------------------------------------------
