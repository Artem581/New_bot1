import os
from dontev import load_dontev
from telegram import Update
from telegram ext.import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)


load_dontev()
TOKEN = os.getenv('TELEGRAM-BOT-TOKEN')

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Привет! Я твой телеграм бот. Как могу помочь?")

async def help_command(update, context):
    await update.message.reply_text(
        "Команды:\n/start - начать\n/help - помощь\n/about - обо мне"
    )


async def handle_text(update, context):
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

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ComandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(MmessageHandler(filters.TEXT | ~filters.COMMAND, handle_text))
    app.run_polling()
