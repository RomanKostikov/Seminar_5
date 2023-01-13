# 36. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#     *Пример:*
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
"""Doc."""

nums = [1, 5, 2, 3, 4, 6, 1, 7]

# Первый вариант решения


def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups


def main():
    print(get_up2(nums))


if __name__ == '__main__':
    main()
# Второй вариант решения


def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups


print(get_up(nums))

# третий вариант решения с enumerate (групповой)

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = list()
new_list.append(my_list[0])
# print(len(new_list))

for index, elem in enumerate(my_list):
    if elem > new_list[-1]:
        new_list.append(elem)

print(new_list)
