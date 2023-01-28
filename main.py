from telebot.async_telebot import AsyncTeleBot
from telebot import types
import asyncio
import os
from collections import defaultdict
from model import get_predict
from tg_token import get_token

token = get_token()
bot = AsyncTeleBot(token)

markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
help_item = types.KeyboardButton('Help')
first_item = types.KeyboardButton('Send first photo')
second_item = types.KeyboardButton('Send second photo')
result_item = types.KeyboardButton('Get result photo')

markup.add(first_item, second_item, result_item, help_item)


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
        Hi there, I am StyleBot. I am here to transfer style from first your photo to second your photo.\
 Use buttons to send me two photos and get result.""",
                       reply_markup=markup)

flag_first = defaultdict(bool)
flag_second = defaultdict(bool)
flag_action = defaultdict(int)


@bot.message_handler(content_types=['text'])
async def reply_for_commands(message):
    global flag_action
    if message.text == 'Help':
        await bot.reply_to(message, """\
        Use "Send first photo" button and send photo from witch you want to transfer style.\n
Use "Send second photo" button and send photo to what you want to transfer style.\n
Use "Get result photo" button to get result photo with transferred style.\n
Use "Help" button to see this text.""")
    elif message.text == 'Send first photo':
        flag_action[str(message.chat.id)] = 1
        await bot.reply_to(message, """Now send me first photo.""")
    elif message.text == 'Send second photo':
        flag_action[str(message.chat.id)] = 2
        await bot.reply_to(message, """Now send me second photo.""")
    elif message.text == 'Get result photo':
        path = 'chats/' + str(message.chat.id) + '/file_'
        flag_first[str(message.chat.id)] = os.path.exists(path + '1.jpg')
        flag_second[str(message.chat.id)] = os.path.exists(path + '2.jpg')
        if flag_first[str(message.chat.id)] and flag_second[str(message.chat.id)]:
            result_message = await bot.send_message(message.chat.id, '<i>Working with your photos...</i>',
                                                    parse_mode='HTML',
                                                    disable_web_page_preview=True)
            get_predict(path + '1.jpg', path + '2.jpg', 'chats/' + str(message.chat.id) + '/result.jpg')
            await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Done!</i>',
                                        parse_mode='HTML')
            with open('chats/' + str(message.chat.id) + '/result.jpg', 'rb') as new_file:
                await bot.send_photo(message.chat.id, new_file)
        elif not flag_first[str(message.chat.id)] and not flag_second[str(message.chat.id)]:
            await bot.reply_to(message, """Please send me first and second photos.""")
        elif not flag_first[str(message.chat.id)]:
            await bot.reply_to(message, """Please send me first photo.""")
        elif not flag_second[str(message.chat.id)]:
            await bot.reply_to(message, """Please send me second photo.""")
        else:
            await bot.reply_to(message, """Please dont do such things with me.""")
    else:
        await bot.reply_to(message, """\
        Please write command "/start" and use buttons.""")


@bot.message_handler(content_types=['photo'])
async def receive_photo(message):
    global flag_first, flag_second, flag_action
    if flag_action[str(message.chat.id)] == 1 or flag_action[str(message.chat.id)] == 2:
        result_message = await bot.send_message(message.chat.id, '<i>Downloading your photo...</i>', parse_mode='HTML',
                                                disable_web_page_preview=True)
        file_path = await bot.get_file(message.photo[-1].file_id)
        downloaded_file = await bot.download_file(file_path.file_path)
        path = 'chats/' + str(message.chat.id)
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + '/file_' + str(flag_action[str(message.chat.id)]) + '.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        await bot.edit_message_text(chat_id=message.chat.id, message_id=result_message.id, text='<i>Done!</i>',
                                    parse_mode='HTML')

        if flag_action[str(message.chat.id)] == 1:
            flag_first[str(message.chat.id)] = os.path.exists(path + '/file_1.jpg')
        elif flag_action[str(message.chat.id)] == 2:
            flag_second[str(message.chat.id)] = os.path.exists(path + '/file_2.jpg')
        else:
            await bot.reply_to(message, """Please dont do such things with me.""")
        flag_action[str(message.chat.id)] = 0
    else:
        await bot.reply_to(message, """Please use buttons for choosing what photo you want to send.""")


asyncio.run(bot.polling())
