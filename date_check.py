import datetime

today = datetime.date.today()
# today = today.strftime('Сегодня день - %d , месяц - %m, год - %Y')
print (f"Текущая дата : {today}")

now = datetime.datetime.now()
print (f"Текущая дата и время : {now}")

other_date = datetime.date(2023, 11, 8)
date_diffrence = today - other_date
print(f"Разница между датами: {date_diffrence}")

