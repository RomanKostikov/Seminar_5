# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# (отдельный файл txt).
"""Doc."""
import os
os.system('cls')

input = 'C://Users//roman//Desktop//Work for IT//GeekBrains//'\
    'seminars//Python//Seminar_5//homework001//input.txt'
out = 'C://Users//roman//Desktop//Work for IT//GeekBrains//'\
    'seminars//Python//Seminar_5//homework001//output.txt'


def del_some_words(input):
    input = list(filter(lambda x: 'абв' not in x, input))
    print(input)
    return " ".join(input)


def main():
    with open(input, 'r', encoding='UTF-8') as input_file:
        out_list = [word.split() for word in input_file.readlines()]
        out_list = out_list[0]+out_list[1]
    with open(out, 'w', encoding='UTF-8') as out_file:
        out_file.write(del_some_words(out_list))


if __name__ == '__main__':
    main()
