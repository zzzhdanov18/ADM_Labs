#основные комбинаторные формулы 

##############################
import os
clear  = lambda: os.system('cls')
from colorama import init, Fore
init(autoreset=True)
from sup_functions import *
###############################

check = 1
while check != 0:
    print_yellow_text('-----------------Выберете опцию--------------------')

    print('1) Сочетание без повторений')
    print('2) Сочетание с повторениями')
    print('3) Размещения без повторений')
    print('4) Размещения с повторениями')
    print('5) Перестановка без повторений')
    print('6) Перестанвка с повторениями')
    print('7) Правило сложения')
    print('8) Правило умножения\n')
    #остальные функции
    print_im_text('>>Для остановки введите 0 <<')
    print_yellow_text('---------------------------------------------------')
    check = int(input())
    match check:
        case 1:
            clear()
            print('                       [ Пример задачи на сочетание без повторений]')
            print('В ящике находятся M деталей. Сколько существует способов выбрать из ящика N различных деталей?\n')
            print_blue_text('>>>Введите данные')
            m = int(input("M = "))
            n = int(input("N = "))
            while (n > m or n <= 0 or m <= 0):
                print_red_text(">>>>> Данные некорректны. Повторите ввод")
                m = int(input("M = "))
                n = int(input("N = "))
            clear()
            print('                       [ Пример задачи на сочетание без повторений ]')
            print('В ящике находятся '+str(m)+' деталей. Сколько существует способов выбрать из ящика '+str(n)+' различных деталей?\n')
            mem = fact_(m)/(fact_(n)*fact_(m-n))
            print_blue_text('[Формула -> С = M! / (N!*(M-N)!) ]') 
            print_green_text('>>> Ответ '+str(int(mem)))
        case 2:
            clear()
            print('                       [ Пример задачи на сочетание c повторениями]')
            print('В магазине продаются карандаши N цветов. Сколько существует способов купить M карандашей?')
            print_blue_text('>>>Введите данные')
            n = int(input("N = "))
            m = int(input("M = "))
            while (n <= 0 or m <= 0):
                print_red_text(">>>>> Данные некорректны. Повторите ввод")
                n = int(input("N = "))
                m = int(input("M = "))
            clear()
            print('                       [ Пример задачи на сочетание с повторениями ]')
            print('В магазине продаются карандаши '+str(n)+' цветов. Сколько существует способов купить ' + str(m)+' карандашей?\n')
            mem = fact_(m + n - 1)/(fact_(m)*fact_(n-1))
            print_blue_text('[Формула -> С = (N+M-1)! / (M!*(N-1)!) ]') 
            print_green_text('>>> Ответ '+str(int(mem)))
        case 3:
            clear()
            print('                       [ Пример задачи на размещение без повторений]')
            print('В доме имеются N гаражей. Сколькими способами возможно разместить M различных машин?')
            print_blue_text('>>>Введите данные')
            n = int(input("N = "))
            m = int(input("M = "))
            while (m > n or n <= 0 or m <= 0):
                print_red_text(">>>>> Данные некорректны. Повторите ввод")
                n = int(input("N = "))
                m = int(input("M = "))
            clear()
            print('                       [ Пример задачи на размещение без повторений ]')
            print('В доме имеются '+str(n)+' гаражей. Сколькими способами возможно разместить ' + str(m)+' различных машин?\n')
            mem = fact_(n)/(fact_(n-m))
            print_blue_text('[Формула -> A = N! / (N-M)! ]') 
            print_green_text('>>> Ответ '+str(int(mem)))
        case 4:
            clear()
            print('                       [ Пример задачи на размещение c повторениями ]')
            print('Алфавит имеет N букв. Сколько существует способов составить слово длины M?')
            print_blue_text('>>>Введите данные')
            n = int(input("N = "))
            m = int(input("M = "))
            while (n <= 0 or m <= 0):
                print_red_text(">>>>> Данные некорректны. Повторите ввод")
                n = int(input("N = "))
                m = int(input("M = "))
            clear()
            print('                       [ Пример задачи на размещение с повторениями ]')
            print('Алфавит имеет '+str(n)+' букв. Сколько существует способов совтавить слово длины ' + str(m)+' ?\n')
            mem = n**m
            print_blue_text('[Формула -> A = N^M ]') 
            print_green_text('>>> Ответ '+str(int(mem)))
        case 5:
            clear()
            print('                       [ Пример задачи на перестановку без повторений ]')
            print('Алфавит имеет N букв. Сколько существует способов составить слово длины N, если каждую букву можно использовать только один раз?')
            print_blue_text('>>>Введите данные')
            n = int(input("N = "))
            while (n <= 0):
                print_red_text(">>>>> Данные некорректны. Повторите ввод")
                n = int(input("N = "))
            clear()
            print('                       [ Пример задачи на перестановку без повторений ]')
            print('Алфавит имеет '+str(n)+' букв. Сколько существует способов совтавить слово длины ' + str(n)+' , если каждую букву можно использовать только один раз?\n')
            mem = fact_(n)
            print_blue_text('[Формула -> P = N! ]') 
            print_green_text('>>> Ответ '+str(int(mem)))
        case 6:
            clear()
            print('                       [ Пример задачи на перестановку c повторениями ]')
            print('Сколько различных 6-тибуквенных слов можно написать из 3 букв {a,b,c}, если буква a должна повторяться 3 раза, буква b – 2 раза, буква c – 1 раз.\n')
            print_blue_text('[Формула -> P = N!/(N1!*N2! ... * Nk!) ]') 
            print_green_text('>>> Ответ 60')
        