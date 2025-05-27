import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, это бот для быстрого взаимодейсвтия с PixelVPN")
    notify_admin(message, "Команда /start")

@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id, 'Чтобы использовать PixelVPN нужно: 1) написать - , для оплаты и получения доступа 2) Установить бесплатное приложение Amnezia VPN - 3) Запустить приложение и нажать кнопку "Начать", нажать на ')
    notify_admin(message, "Команда /info")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Если что-то не работает, то перезапусти бота - /start. Тех. поддержа - ')
    notify_admin(message, "Команда /help")
    
@bot.message_handler(commands=['find'])
def find_command(message):

ADMIN_ID =
@bot.message_handler(commands=['path'])
def path_message(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id != ADMIN_ID:
        bot.send_message(chat_id, "Отказано в доступе")
        return

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    if message.from_user.id != ADMIN_ID:
        try:
            bot.send_message(
                ADMIN_ID,
                f"Новое сообщение от @{message.from_user.username or 'без username'} "
                f"(ID: {message.from_user.id}):\n\n{message.text}"
            )
        except Exception as e:
            print(f"Ошибка при отправке сообщения админу: {e}")

bot.infinity_polling()