from os import system
try: 
    from colorama import Style, Fore, init
    init()
except:
    system("pip install colorama")
    from colorama import Style, Fore, init
    init()
try: 
    from gpassw.functions import password
except:
    system("pip install gpassw")
    from gpassw.functions import password
    import gpassw.config as config

name = input("Напиши своё имя: ")
print(f"Привет, {name}! Сейчас подберём для тебя оптимальный пароль...")
passw = password.medium(10) #Генерация среднего пароля
checking = password.check(passw) #Проверяем пароль на надёжность
print(checking)
if checking == None: #Если пароль надёжен на 100%
    print(Fore.GREEN + "Ваш пароль надёжен." + Style.RESET_ALL)
elif len(checking) < 2 or len(checking) == 2: #Если пароль ненадёжен на два пункта или меньше (Из 5)
    print(Fore.GREEN + "Ваш пароль надёжен." + Style.RESET_ALL)
else:
    print(Fore.RED + "Ваш пароль ненадёжен." + Style.RESET_ALL) #Если пароль нёнадёжен на >2 пункта
print(f"Мы подобрали тебе пароль - {passw} Окей?")
answer = input("Да/Нет: ")
if answer == "Да" or answer == "да":
    print("Теперь напиши пароль, который мы тебе подобрали для входа в аккаунт.")
else:
    raise SystemExit(1)
hello_password = input("Пароль: ")
while hello_password != passw:
    print(Fore.RED + "Пароль неверный." + Style.RESET_ALL)
    hello_password = input("Пароль: ")
print("Вы успешно вошли!")