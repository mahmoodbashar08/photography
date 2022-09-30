from db import add_values
from randomstring import myRandomString
from telegram.ext import  CommandHandler, MessageHandler, Updater, MessageHandler, filters
admin_list = [] # add list of user id who can use the telegram bot


def start(update, context):
    update.message.reply_text("hello please send a file of image to upload it to the website \n for help please send /help")


def photo(update, context):
    update.message.reply_text(f"this is an image please send a file")


def text(update, context):
    file_type = update.message.text
    update.message.reply_text(f"your text where {file_type} for help please send /help")


def document(update, context):
    user_id = update.effective_user.id
    if user_id in admin_list:
        print(update.message)
        if "text" in update.message.to_dict():
            update.message.reply_text("this is an text please send /help to help you")
        elif "document" in update.message.to_dict():
            file_type = update.message["document"]["mime_type"]
            if file_type == "image/png" or file_type == "image/jpeg":
                fileId = update.message.document.file_id
                fileName = update.message.document.file_name
                print("file id is : ", fileId)
                
                # here is the code to get the file

                currentFile = update.message.document.get_file()
                currentFile.download("static/uploads/" + fileName)
                file_download_id = myRandomString()
                add_values(fileName, file_download_id,
                        'uploads/' + fileName, user_id)
                update.message.reply_text("your website/"+file_download_id)

            else:
                update.message.reply_text("please send an pnj file or jpg file")  
    else:
        update.message.reply_text(f"your id is {user_id} and you are not an admin")
updater = Updater(
    "bot Token", use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(filters.Filters.text, text))
dp.add_handler(MessageHandler(filters.Filters.document, document))
dp.add_handler(MessageHandler(filters.Filters.photo, photo))
updater.start_polling()
