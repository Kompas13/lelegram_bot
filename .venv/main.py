import telebot
import wikipedia

bot = telebot.TeleBot('7062654398:AAGASwlQyDZLPuxRR8s9wA97AhKZXvFQVvk')
wikipedia.set_lang("ru")

# Функция получения статьи в Вики
def get_info_in_wiki(text):
    try:
        wiki_text = wikipedia.page(text).content[:1200]
        # Разделяем по точкам
        wiki_spl_text = wiki_text.split(".")

        # Отбрасываем все после последней точки
        wiki_spl_text = wiki_spl_text[:-1]

        #Переменная для текста
        wiki_text_2 = ''

        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for i in wiki_spl_text:
            if not ("==" in i):

                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if (len((i.strip())) > 3):
                    wiki_text_2 = wiki_text_2 + i + "."
            else:
                break

        return wiki_text_2

    # Обработка исключения
    except Exception as e:
        return str(user_name) + ", информация в Wiki по данному запросу не найдена, попробуйте поискать ещё что-нибудь интересное;)"

# Обработка команды /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_photo(m.chat.id, "https://sun9-82.userapi.com/impg/gQRTLjOI4WaQZzRYhQHRPE8kUefIkN1B_6hy_g/8f9Gos2COVg.jpg?size=820x638&quality=96&sign=f6a638f3c3381460f7cd852a0b887ebe&c_uniq_tag=LQ7QtSsLyMNfaB8Q_lGkwVi5rYZPX6au_nPYHDHywZA&type=album")
    bot.send_message(m.chat.id, "Привет! Отправь мне любое слово, и я найду его значение в Wikipedia")

# Получение сообщений от пользователя
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global user_name
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, get_info_in_wiki(message.text))

# Старт бота
bot.polling(none_stop=True, interval=0)
