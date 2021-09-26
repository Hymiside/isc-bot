import sqlite3


conn = sqlite3.connect('../ISCBot/utils/service.db', check_same_thread=False)
cursor = conn.cursor()


def return_user_id() -> list:
    """Возвращает список всех user_id из БД, для количества пользователей"""
    cursor.execute(f"SELECT user_id FROM users")
    return cursor.fetchall()


def return_all_schools() -> list:
    """Возвращает все школы в боте для регистрации пользователя"""
    not_format = cursor.execute(f"SELECT id, school_name, class_name FROM schools").fetchall()
    all_schools = [tuple_schools for tuple_schools in not_format]
    return all_schools


def return_number_of_users_in_class(school_id: int) -> list:
    """Возвращает список user_id выбранной школы для просмотра количества пользователей"""
    cursor.execute(f"SELECT user_id FROM users WHERE school_id=?", (school_id, ))
    return cursor.fetchall()


def delete_class(school_id: int):
    """Удаляет выбранный класса"""
    cursor.execute(f"DELETE FROM homework WHERE school_id=?", (school_id,))
    cursor.execute(f"DELETE FROM timetable WHERE school_id=?", (school_id,))
    cursor.execute(f"DELETE FROM users WHERE school_id=?", (school_id,))
    cursor.execute(f"DELETE FROM schools WHERE id=?", (school_id, ))
    conn.commit()
