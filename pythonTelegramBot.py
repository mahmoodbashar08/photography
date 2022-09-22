from turtle import up
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, MessageHandler, Updater, MessageHandler, filters
admin_list = [583427713]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    print("hello : ")

    if "text" in update.message.to_dict():
        print("Yessss")
    else:
        print("Nooooooo")
    first_name = update.effective_user.first_name
    last_name = update.effective_user.last_name
    username = update.effective_user.username
    if first_name == None or last_name == None or username == None:
        pass
    else:
        print("first name :" + first_name)
        print("last name :" + last_name)
        print("username :" + username)
    user_id = update.effective_user.id
#     print(update.message.text)
#     if user_id in admin_list:

#         await update.message.reply_text(f'Hello {update.effective_user.first_name} {update.effective_user.last_name} your id is : {user_id}')
#     else:
    await update.message.reply_text(f"your first name is : {first_name} and your last name is : {last_name} with username of : {username} and your id is {user_id} ")


# async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text('give a file')
#     chat_id = update.message.chat_id
#     fileID = update.message['document']['file_id']
#     context.bot.sendDocument(chat_id=chat_id,
#                              caption='This is the file that you have sent to bot',
#                              document=fileID)

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("hello")
    print(update.message)
    if "text" in update.message.to_dict():
        print("this is text")
    elif "document" in update.message.to_dict():
        print("this is file")
    else:
        print("this is photo")
#     file_type = update.message["document"]["mime_type"]
    await update.message.reply_text(update.message)


async def image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("hello")
    print(update.message)
    file_type = update.message["document"]["mime_type"]
    await update.message.reply_text(f"your file type where {file_type}")


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("hello")
    print(update.message)
    file_type = update.message
    await update.message.reply_text(f"your file type where {file_type}")


app = ApplicationBuilder().token(
    '5382529868:AAFtgxfYtQEwFbfChOatXMtc0FqEj13RHcM').build()
app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("start1", start1))
app.add_handler(MessageHandler(filters.ALL, download))
# app.add_handler(MessageHandler(filters.Document.Category('image/'), image))
# app.add_handler(MessageHandler(filters.TEXT, text))

app.run_polling()
