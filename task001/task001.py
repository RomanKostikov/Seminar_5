# 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного,чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

# решение без enumerate


def get_data_from_file(nums):
    data = open(nums, 'r')
    dlist = data.read() + ' '
    dlist = list(map(int, dlist.split()))
    data.close()
    return dlist


def find_number(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1


def main():
    fnums = 'C://Users//roman//Desktop//Work for IT//GeekBrains//'\
        'seminars//Python//Seminar_5//task001//task001.txt'
    nums_list = get_data_from_file(fnums)

    print(nums_list)
    print(find_number(nums_list))


if __name__ == '__main__':
    main()
# с использование enumerate(групповое решение)

# f = open('C://Users//roman//Desktop//Work for IT//GeekBrains//'
#          'seminars//Python//Seminar_5//task001//task001.txt', 'r')
# data = f.read().split()
# f.close()

# data = list(map(int, data))

# print(data)

# for i, el in enumerate(data[:-1]):
#     if el != data[i+1] - 1:
#         print(data[i+1] - 1)
