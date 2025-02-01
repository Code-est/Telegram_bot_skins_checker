# Telegram_bot_skins_checker

![1](https://github.com/user-attachments/assets/b1ba7643-e195-4410-a9c1-f9d130d573f5)

### Описание:
Телеграм бот, написанный на Python, который позволяет в режиме реального времени узнать стоимость предмета (скина) в компьютерной игре CS 2.
#

### Как устроен:
Код, написанный на языке Python, использует дополнительные библиотеки `Telebot` и `Requests`. С помощью библиотеки `Telebot` функционирует сам телеграм бот, и написанные Inline кнопки, позволяющие отдавать внутринние команды (callback). После выбора скина и нажатия соответствующией Inline кнопки происходит запрос на сервер STEAM с помощью модуля Requests. Запросов может производится от двух до шести для каждого предмета, в зависимости от информации в файле `data.py`, из которых минимальные два это всегда запрос хотя бы одной существующией цены и фотографии самого скина. Остальные четыре запроса могут быть направлены только в том случае, если в файле `data.py` имеется ссылка на остальные качества предмета (скина). После получения ответа на запрос код обрабатывает полученные данные и выводит стомость каждого качества предмета (скина) и фотографию.  
> [!IMPORTANT]
> При выборе конкретного предмета (скина) каждый раз производится запрос на сервер STEAM по ссылкам из файла `data.py`.
#

### Дополнение файлов data.py и Telegram_bot.py
#### Инструкция по созданию каждого предмета (скина): #
Файл `data.py` может быть дополнительно расширен в случае появления новых скинов. Каждый скин имеет свою запись в следующем виде:  
"SG 553 | Hypnotic" : ["FN", "MW", "FT", "WW", "BS", "photo"]   , где
1. "SG 553 | Hypnotic" - это название скина. В файле `data.py` желательно указывать название также как и в файле `Telegram_bot.py`;
2. "FN", "MW", "FT", "WW", "BS" - это ссылки* на качество скина;
3. "photo" - это ссылка на фото скина
#### Метод получения ссылок: #
Для работы бота используются специальные ссылки, а не те что указываются в URI.  
Для получения ссылки на качества необходимо:
1. Зайти на страницу предмета (скина) соответствуюшего качества;
2. С помощью правой конпки мыши открыть "Исследовать элемент";
3. Перейти во вкладку "Сеть";
4. Скопировать ссылку справа первом появившися ответе, т.к. в нем содержится информация о цене
![image](https://github.com/user-attachments/assets/954732a9-fb27-4ee1-9609-c9194348cfa6)
![image](https://github.com/user-attachments/assets/4bc28d78-7c11-4a23-bc6a-8164a6b2e373)  

Для получения ссылки на фото необходимо:
1. Просто открыть любую страницу в STEAM со скином и взять URI сверху
#### Метод добавления скинов в основной код файла Telegram_bot.py: #
Образец кода

    elif call.data == "m4a4":
        b1 = telebot.types.InlineKeyboardMarkup(row_width=1)

        m4a4_2 = telebot.types.InlineKeyboardButton("M4A4 | Poseidon", callback_data = "M4A4 | Poseidon")
        m4a4_3 = telebot.types.InlineKeyboardButton("M4A4 | The Coalition", callback_data = "M4A4 | The Coalition")
        m4a4_4 = telebot.types.InlineKeyboardButton("M4A4 | Eye of Horus", callback_data = "M4A4 | Eye of Horus")
        m4a4_5 = telebot.types.InlineKeyboardButton("M4A4 | Radiation Hazard", callback_data = "M4A4 | Radiation Hazard")
        m4a4_6 = telebot.types.InlineKeyboardButton("M4A4 | Daybreak", callback_data = "M4A4 | Daybreak")
        back_button_rifles = telebot.types.InlineKeyboardButton("BACK", callback_data = "rifles")

        b1.add(m4a4_2, m4a4_3, m4a4_4, m4a4_5, m4a4_6, back_button_rifles)
        bot.edit_message_text(chat_id= call.message.chat.id, message_id=call.message.message_id, text = "ALL M4A4's!", reply_markup = b1)
        print(call.data)

Для добалвения нового скина необходимо:
1. Между переменными "m4a4_6" и "back_button_rifles" добавить новую переменную с названием "m4a4_7";
2. В первых ковычках указать название, которое будет указано на кнопке в телеграме;
3. Во вторых ковычках (callback_data = ) указать название скина в файле `data.py`;
4. В скобках у "b1.add" указать новую переменную "m4a4_7" для появления кнопки с указанным новым скином в телеграме  

Таким образом осуществляется связь между двумя файлами. Дополнение кода для всех остальных скинов осуществляется аналогичным образом.
#


### Как запустить:
1. Установить `Telebot` (pip install pyTelegramBotAPI)  
2. Установить `Requests` (pip install requests)  
3. Получить Token от Bot Father в телеграме для подключения бота (https://core.telegram.org/bots/tutorial#obtain-your-bot-token)  
4. Запустить `Telegram_bot.py`  
#
