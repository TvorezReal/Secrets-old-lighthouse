import sqlite3

def create_tables():
    conn = sqlite3.connect('game_database.db')
    cursor = conn.cursor()

    # Таблица персонажей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT,
        description TEXT,
        photo BLOB
    )''')

    # Таблица сцен
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scenes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        options TEXT,
        photo BLOB,
        scene_text TEXT,
        transition_hint TEXT
    )''')

    # Таблица диалогов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dialogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scene_id INTEGER,
        text TEXT,
        changeable_text_id INTEGER,
        FOREIGN KEY(scene_id) REFERENCES scenes(id),
        FOREIGN KEY(changeable_text_id) REFERENCES texts(id)
    )''')

    # Таблица текстов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        variant TEXT
    )''')

    # Таблица связей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS relationships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_scene_id INTEGER,
        to_scene_id INTEGER,
        condition TEXT,
        FOREIGN KEY(from_scene_id) REFERENCES scenes(id),
        FOREIGN KEY(to_scene_id) REFERENCES scenes(id)
    )''')

    # Таблица текущего состояния игры
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS game_state (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        current_scene INTEGER,
        inventory TEXT,
        status TEXT,
        FOREIGN KEY(current_scene) REFERENCES scenes(id)
    )''')

    # Фиксация и закрытие соединения
    conn.commit()
    conn.close()
def print_table_fields():
    conn = sqlite3.connect('game_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    for table_name in tables:
        table_name = table_name[0]
        cursor.execute(f'PRAGMA table_info({table_name})')
        columns = cursor.fetchall()
        print(f"Таблица '{table_name}':")
        for column in columns:
            print(column[1], end=', ')
        print('\n')

# Вызов функций
create_tables()
print_table_fields()

