from tkinter import N
from tkinter.messagebox import NO
import tracemalloc
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, File
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, Updater, MessageHandler, filters

admin_list = [583427713, 1236034796]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("hello please send a file of image to upload it to the website \n for help please send /help")


async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"this is an image please send a file")


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_type = update.message.text
    await update.message.reply_text(f"your text where {file_type} for help please send /help")


async def document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id in admin_list:
        print(update.message)
        if "text" in update.message.to_dict():
            print("this is text")
            await update.message.reply_text("this is an text please send /help to help you")
        elif "document" in update.message.to_dict():
            file_type = update.message["document"]["mime_type"]
            if file_type == "image/png" or file_type == "image/jpeg":
                await update.message.reply_text("this is an file thank you")
                file_id = update.message.document.file_id
                fileName = update.message.document.file_name
                print("file id is : ", file_id)
                # here is the code to get the file
                currentFile = await update.message.document.get_file()
                await currentFile.download("uploads/" + fileName)
                # await File.download(update.message)

            else:
                await update.message.reply_text("please send an pnj file or jpg file")
        else:
            print("this is photo")
    else:
        await update.message.reply_text(f"your id is {user_id} and you are not an admin")


app = ApplicationBuilder().token(
    '5382529868:AAFtgxfYtQEwFbfChOatXMtc0FqEj13RHcM').build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, text))
app.add_handler(MessageHandler(filters.Document.ALL, document))
app.add_handler(MessageHandler(filters.PHOTO, photo))
app.run_polling()
