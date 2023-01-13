# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""Doc."""
import os
os.system('cls')


def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


def main():
    my_text = 'Напишите напиабв програбвмму программу, удаляющую из \
    этого абв текста все абв вабвс слова, содерабващие содержащие "абв"'
    my_text = del_some_words(my_text)
    print(my_text)


if __name__ == '__main__':
    main()
