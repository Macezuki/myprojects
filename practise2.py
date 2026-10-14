
#1 задача
# money = 1000

# while True:
#     print("\n1 — Купить хлеб")
#     print("2 — Купить молоко")
#     print("3 — Купить шоколад")
#     print("4 — Показать остаток денег")
#     print("0 — Выйти")

#     choice = input("Выберите действие: ")

#     if choice == "1":
#         if money >= 50:
#             money -= 50
#             print("Вы купили хлеб")
#         else:
#             print("Недостаточно денег")
#     elif choice == "2":
#         if money >= 80:
#             money -= 80
#             print("Вы купили молоко")
#         else:
#             print("Недостаточно денег")
#     elif choice == "3":
#         if money >= 150:
#             money -= 150
#             print("Вы купили шоколад")
#         else:
#             print("Недостаточно денег")
#     elif choice == "4":
#         print(f"Остаток денег: {money} сом")
#     elif choice == "0":
#         spent = 1000 - money
#         print(f"Вы потратили: {spent} сом")
#         print(f"Осталось: {money} сом")
#         break
#     else:
#         print("Неверный выбор")

#2 задача
# login = "admin"
# password = "12345"
# attempts = 3

# while attempts > 0:
#     user_login = input("Логин: ")
#     user_password = input("Пароль: ")

#     if user_login == login and user_password == password:
#         print("Добро пожаловать")
#         break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print("Неверный логин или пароль")
#             print(f"Осталось попыток: {attempts}")
#         else:
#             print("В доступе отказано")   

#3 задача
# import random

# secret = random.randint(1, 100)  
# attempts = 7

# print("Компьютер загадал число от 1 до 100,угадайта загаданное число")

# while attempts > 0:
#     guess = int(input("Ваше число: "))

#     if guess < secret:
#         print("Загаданное число больше")
#     elif guess > secret:
#         print("Загаданное число меньше")
#     else:
#         print("Вы победили!")
#         break

#     attempts -= 1
#     if attempts > 0:
#         print(f"Осталось попыток: {attempts}")
# else:
#     print("Вы проиграли.")
#     print(f"Загаданное число: {secret}")

