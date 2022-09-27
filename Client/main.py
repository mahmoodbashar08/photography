# # from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# # from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, MessageHandler, Updater, MessageHandler, filters
# # admin_list = [5834427713]


# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
# #     user_id = update.effective_user.id
# #     if user_id in admin_list:
# #         await update.message.reply_text(f'Hello {update.effective_user.first_name} {update.effective_user.last_name} your id is : {user_id}')
# #     else:
# #         await update.message.reply_text(f"your id is {user_id} and you are not an admin")


# # # async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
# # #     await update.message.reply_text('give a file')
# # #     chat_id = update.message.chat_id
# # #     fileID = update.message['document']['file_id']
# # #     context.bot.sendDocument(chat_id=chat_id,
# # #                              caption='This is the file that you have sent to bot',
# # #                              document=fileID)
# # def downloader(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
# #     context.bot.get_file(update.message.document).download()

# #     # writing to a custom file
# #     with open("custom/file.doc", 'wb') as f:
# #         context.bot.get_file(update.message.document).download(out=f)


# # app = ApplicationBuilder().token(
# #     '5382529868:AAFtgxfYtQEwFbfChOatXMtc0FqEj13RHcM').build()
# # app.add_handler(CommandHandler("start", start))
# # # app.add_handler(CommandHandler("start1", start1))
# # app.add_handler(MessageHandler(filters.document, downloader))


# # app.run_polling()
from flask import Flask
from flask import request
from flask import Response


TOKEN = "5382529868:AAFtgxfYtQEwFbfChOatXMtc0FqEj13RHcM"
app = Flask(__name__)


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    first_name = message['message']["from"]["first_name"]
    if "document" in message['message']:
        if message['message']['document']["mime_type"]:
            print("file id : ", message['message']['document']["file_id"])
            myFileId = message['message']['document']["file_id"]

    else:
        txt = message['message']['text']
        print("txt-->", txt)
    print("chat_id-->", chat_id)

    return chat_id, first_name


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


admin_list = [583427713, 1236034796]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, first_name = parse_message(msg)
        if chat_id in admin_list:
            print("an admin")
            tel_send_message(
                chat_id, f'hello {first_name} your id : {chat_id} I love you so much will you marry me? ❤️')
            # print("type is ", txt.type)
            # if txt == "/hi":
            #     tel_send_message(chat_id, "Hello!!")
            # else:
            #     tel_send_message(chat_id, 'from webhook')

            return Response('ok', status=200)
        else:
            tel_send_message(
                chat_id, f'your id is :{chat_id} and you are not an admin')
            print("not an admin")
            return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
