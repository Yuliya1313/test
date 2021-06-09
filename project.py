import time
import gspread
import telebot
# Чтение гугл таблицы
from secret import TOKEN, ID




def skad():
    from secret import TOKEN, ID
    print(TOKEN)
    bot = telebot.TeleBot(TOKEN)
    
    f = open('number.txt')
    h = f.read()
    f.close()
    h = int(h)


    gc = gspread.service_account()

    sh = gc.open("Обратная связь по заказу дисков (Ответы)")

    print(sh.sheet1.get('A1'))

    count = 0
    i = 1
    val = ''
    while val != list():    
        count += 1
        i += 1
        val = sh.sheet1.get('A' + str(i))
    new_count = count
    new = 0
    
    if count > h:
        new = count - h   # вычисляем сколько строк(отзывов) добавилось
        for j in range(new):
            count = new_count - j
            print(count)
            print(j)
            if sh.sheet1.get('H' + str(count)) != list():
                name = sh.sheet1.get('H' + str(count))
                phone = sh.sheet1.get('J' + str(count))
                question = sh.sheet1.get('K' + str(count))
                sms = str('Имя клиента: ' + str(name) + '\nТелефон: ' + str(phone) + '\nВопрос: ' + str(question))
                bot.send_message(ID, str(sms))
                time.sleep(60)
            
    if new_count > h:
        f = open('number.txt', 'w')
        f.writelines(str(new_count))
        f.close()
        
        
 
while True:
    skad()
    time.sleep(3600)
