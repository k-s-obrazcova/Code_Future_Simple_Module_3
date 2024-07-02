import datetime

today = datetime.date.today()
# today = today.strftime('Сегодня день - %d , месяц - %m, год - %Y')
print (f"Текущая дата : {today}")

now = datetime.datetime.now()
print (f"Текущая дата и время : {now}")

other_date = datetime.date(2023, 11, 8)
date_diffrence = today - other_date
print(f"Разница между датами: {date_diffrence}")

formatted_date = now.strftime("""
%a - Название дня кратко
%A - Название дня полное
%b - Название месяца кратко
%B - Название месяца полное
%c - Дата и время
%d - День месяца
%H - Часы в 24 часовом формате
%I - Часы в 12 часовом формате
%j - Номер дня в году
%m - Номер месяца
%M - Число минут
%p - До полудня или после
%S - Число секунд
%U - Номер недели в году
%x - Дата в формате месяц/день/год
%X - Время
%Y - Год с веком
%y - Год без века
""")
print(f"Форматированная дата и время: {formatted_date}")