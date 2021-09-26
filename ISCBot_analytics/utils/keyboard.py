from aiogram import types


def main_keyboard():
    list_button = [
        types.KeyboardButton(text="Количество пользователей"),
        types.KeyboardButton(text="Количество пользователей класса"),
        types.KeyboardButton(text="Создать рассылку"),
        types.KeyboardButton(text="Удалить класс")
    ]
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*list_button)
    return keyboard


def all_schools(schools: list):
    """Клавиатура всех классов для просмотра пользователей"""
    list_button = [types.InlineKeyboardButton(text=f'{i[1]}  {i[2]}', callback_data=f'cls{i[0]}') for i in schools]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*list_button)
    return keyboard


def all_schools_for_delete(schools: list):
    """Клавиатура всех классов для удаления выбранного класса"""
    list_button = [types.InlineKeyboardButton(text=f'{i[1]}  {i[2]}', callback_data=f'dlt{i[0]}') for i in schools]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*list_button)
    return keyboard
