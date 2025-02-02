"""
File: my_list.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
"""

from typing import List

""" 列表类简易实现 """
class MyList:
    def __init__(self):
        """ 构造方法 """
        self.__capacity = 10  # 列表容量
        self.__nums: List[int] = [0] * self.__capacity  # 数组（存储列表元素）
        self.__size = 0  # 列表长度（即当前元素数量）
        self.__extend_ratio = 2  # 每次列表扩容的倍数

    def __check_index(self, index: int):
        """检查索引是否合法"""
        assert 0 <= index < self.__size, "索引越界: size-> {}, index->{}".format(self.__size, index)

    def __check_size_or_extend_capacity(self):
        if self.__size == self.__capacity:
            self.__extend_capacity()

    def size(self) -> int:
        """ 获取列表长度（即当前元素数量） """
        return self.__size

    def capacity(self) -> int:
        """ 获取列表容量 """
        return self.__capacity

    def get(self, index: int) -> int:
        """ 访问元素 """
        # 索引如果越界则抛出异常，下同
        self.__check_index(index)
        return self.__nums[index]

    def set(self, value: int, index: int) -> None:
        """ 更新元素 """
        self.__check_index(index)
        self.__nums[index] = value

    def add(self, value: int) -> None:
        """尾部插入元素"""
        self.__check_size_or_extend_capacity()
        self.__nums[self.__size] = value
        # 更新元素数量
        self.__size += 1

    def insert(self, value: int, index: int) -> None:
        """在索引`index`处插入值`value`"""
        self.__check_index(index)
        self.__check_size_or_extend_capacity()

        for j in range(self.__size - 1, index - 1, -1):
            self.__nums[j + 1] = self.__nums[j]

        self.__nums[index] = value
        self.__size += 1

    def remove(self, index: int) -> int:
        """ 删除元素 """
        target = self.get(index)
        # 索引 i 之后的元素都向前移动一位
        for j in range(index, self.__size - 1):
            self.__nums[j] = self.__nums[j + 1]
        # 更新元素数量
        self.__size -= 1
        # 返回被删除元素
        return target

    def __extend_capacity(self) -> None:
        """ 列表扩容 """
        # 新建一个长度为 self.__size 的数组，并将原数组拷贝到新数组
        self.__nums = self.__nums + [0] * self.capacity() * (self.__extend_ratio - 1)
        # 更新列表容量
        self.__capacity = len(self.__nums)

    def to_array(self) -> List[int]:
        """ 返回有效长度的列表 """
        return self.__nums[:self.__size]


""" Driver Code """
if __name__ == "__main__":
    """ 初始化列表 """
    list = MyList()
    """ 尾部添加元素 """
    list.add(1)
    list.add(3)
    list.add(2)
    list.add(5)
    list.add(4)
    print("列表 list = {} ，容量 = {} ，长度 = {}"
          .format(list.to_array(), list.capacity(), list.size()))

    """ 中间插入元素 """
    list.add(num=6, index=3)
    print("在索引 3 处插入数字 6 ，得到 list =", list.to_array())

    """ 删除元素 """
    list.remove(3)
    print("删除索引 3 处的元素，得到 list =", list.to_array())

    """ 访问元素 """
    num = list.get(1)
    print("访问索引 1 处的元素，得到 num =", num)

    """ 更新元素 """
    list.set(0, 1)
    print("将索引 1 处的元素更新为 0 ，得到 list =", list.to_array())

    """ 测试扩容机制 """
    for i in range(10):
        # 在 i = 5 时，列表长度将超出列表容量，此时触发扩容机制
        list.add(i)
    print("扩容后的列表 list = {} ，容量 = {} ，长度 = {}"
          .format(list.to_array(), list.capacity(), list.size()))
