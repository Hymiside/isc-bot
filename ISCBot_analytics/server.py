import logging
import time

from aiogram import Bot, Dispatcher, types, executor

from utils import db
from utils import keyboard
from ISCBot import server


bot_anal = Bot(token='')
dp_anal = Dispatcher(bot_anal)

logging.basicConfig(level=logging.INFO)


@dp_anal.message_handler(commands='start')
async def start(message: types.Message):
    if message.from_user.id == 599516086:
        await message.answer('Управляй ботом с помощью кнопок', reply_markup=keyboard.main_keyboard())
    else:
        await message.answer('Этот бот только для админа')


@dp_anal.message_handler(lambda message: message.text == "Количество пользователей")
async def number_of_users(message: types.Message):
    number = len(db.return_user_id())
    await message.answer(f'Количество пользователей:  {number}')


@dp_anal.message_handler(lambda message: message.text == "Количество пользователей класса")
async def choose_number_of_class(message: types.Message):
    schools = db.return_all_schools()
    await message.answer('Выбери класс', reply_markup=keyboard.all_schools(schools))


@dp_anal.callback_query_handler(lambda c: c.data and c.data.startswith('cls'))
async def number_of_class(callback_query: types.CallbackQuery):
    school_id = int(callback_query.data[3:])
    number_of_users_in_class = len(db.return_number_of_users_in_class(school_id))
    await callback_query.message.answer(f'Количество пользователей в этом классе:  {number_of_users_in_class}')
    await callback_query.answer()


@dp_anal.message_handler(lambda message: message.text == "Создать рассылку")
async def create_newsletter(message: types.Message):
    await message.answer('Введи текст рассылки, но в начале поставь *')


@dp_anal.message_handler(lambda message: message.text.startswith('*'))
async def send_newsletter(message: types.Message):
    text = message.text.strip('*').strip()
    list_user_ids = db.return_user_id()

    for user_id in list_user_ids:
        time.sleep(0.3)
        await server.bot.send_message(*user_id, text)
    await message.answer('Рассылка ушла')


@dp_anal.message_handler(lambda message: message.text == "Удалить класс")
async def choose_delete_class(message: types.Message):
    schools = db.return_all_schools()
    await message.answer('Выбери класс для удаления', reply_markup=keyboard.all_schools_for_delete(schools))


@dp_anal.callback_query_handler(lambda c: c.data and c.data.startswith('dlt'))
async def delete_class(callback_query: types.CallbackQuery):
    school_id = int(callback_query.data[3:])
    db.delete_class(school_id)
    await callback_query.message.answer('Класс успешно удален')
    await callback_query.answer()


if __name__ == '__main__':
    executor.start_polling(dp_anal, skip_updates=True)
