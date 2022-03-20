from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='5237824603:AAFfdut2L_pyuoiX4vovfjhyJgMnXovqL-I')  #токен бота
dp = Dispatcher(bot)  # отправляет данные в функции


@dp.message_handler()  # декоратор ? Принимает все текстовые сообщения
async def get_message(message: types.Message):  # функция сбора текстового сообщения
    # chat_id = message.chat.id  # чат id
    # chat_text = message.text  # текст сообщения
    # print(chat_id)  # печатаем id
    # print(chat_text)
    # print(sent_message.to_python)

    # sent_photo = await bot.send_photo(chat_id=-703237659,
    #                      photo='http://hobby.tomsk.ru/images/news/1032.jpg')
    # print(sent_photo.photo)

    # new_title = await bot.set_chat_title(chat_id=-703237659, title='Супер')
    # print(new_title)
    # chat_link = await bot.export_chat_invite_link(chat_id=-703237659)
    # print(chat_link)

    bot_id = await bot.get_me()
    print(bot_id.username)

executor.start_polling(dp)  # собирает Updates
