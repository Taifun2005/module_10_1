# import threading
# import time
#
# def func1():
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
# def func2(x):
#     for i in range(10):
#         time.sleep(3)
#         print(i, threading.current_thread())
#         print(threading.current_thread().is_alive())
#
# thread =threading.Thread(target=func2, args=(1, ))
# thread.start()
# func1()
# print(threading.enumerate())
# print(threading.currentThread())

"""
import threading
import time


def func1():
    for i in range(10):
        time.sleep(1)
        print((i, threading.current_thread()))
def func2(x):
    for i in range(10):
        time.sleep(1)
        print((i, threading.current_thread()))
        print(threading.currentThread().is_alive())


thread = threading.Thread(target=func2,args=(1, ))
thread.start()
func1()
print(threading.enumerate())
print(threading.currentThread())"""


#       Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков


import threading
import time


def write_words(word_count, file_name):  # word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
    # started_at = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:  #
        for i in range(1, word_count + 1):
            # file.write("Какое-то слово № ", i)
            # file.write('\n')
            # file.write(f"Какое-то слово № {i}"  + '\n')
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    # ended_at = time.time()
    # elapsed = ended_at - started_at
    # print(f'Функция работала {elapsed} СЕК')
    print(f"Завершилась запись в файл {file_name}")
    started_at = time.time()


started_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = time.time()
elapsed = ended_at - started_at
print(f'Функция работала {elapsed} СЕК')


thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

started_at = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
ended_at = time.time()
elapsed = ended_at - started_at
print(f'Функция работала {elapsed} СЕК')
