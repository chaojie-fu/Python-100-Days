"""
测试数组的切片功能
切片后的数组是指向旧的数据，还是创建一个新的数据
"""
origin = [1, 2, 3, 4, 5]
print('origin = ', origin)
Slice = origin[1:3]
print('slice = ', Slice)
origin[1] = 9
print('origin = ', origin)
print('slice = ', Slice)

"""
结果表明python的数据切片操作时创建一个新的数组
"""
