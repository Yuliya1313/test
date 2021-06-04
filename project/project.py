import gspread
# Чтение гугл таблицы
gc = gspread.service_account()

sh = gc.open("Обратная связь по заказу дисков (Ответы)")

print(sh.sheet1.get('A1'))