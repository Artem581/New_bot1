import os
from dotenv import load_dotenv
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button_hi = KeyboardButton("Привет")
    button_how = KeyboardButton("Как дела?")
    button_help = KeyboardButton("Помощь")
    
    keyboard = [[button_hi, button_how], [button_help]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Привет! Я твой телеграм бот. Выберите опцию:",
        reply_markup=reply_markup
    )



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Команды:\n/start - начать\n/help - помощь\n/menu - меню с кнопками"
    )



async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button_time = InlineKeyboardButton("Дата и время", callback_data="time")
    button_fact = InlineKeyboardButton("Случайный факт", callback_data="fact")
    button_site = InlineKeyboardButton("Открыть сайт", url="https://example.com")
    
    keyboard = [
        [button_time, button_fact],
        [button_site]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)



async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text.lower()
        if "привет" in text:
            await update.message.reply_text("Привет, как твои дела?")
        elif "как дела" in text:
            await update.message.reply_text("У меня всё отлично, спасибо!")
        elif "пока" in text:
            await update.message.reply_text("До встречи! Хорошего дня!")
        elif "как пройти до сквера" in text:
            await update.message.reply_text("Прямо, налево, прямо и направо.")
        elif "погода в мухосранске" in text:
            await update.message.reply_text("Тепло как никогда раньше")
        elif "кто съел королевский торт" in text:
            await update.message.reply_text("Не я")
        else:
            await update.message.reply_text("Извини, я пока это не понимаю.")


def main():
    if not TOKEN:
        raise ValueError("Токен не найден! Проверьте файл .env")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
