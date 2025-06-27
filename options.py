'''
This module prepares some new features to give the user the best experience.
It prepares the project folder and the database of the application.
'''


import sqlite3
import getpass
import os


class Options:
    def setup_app_folder(self):
        username = getpass.getuser()
        os.chdir(f'C://Users/{username}/AppData/Local/')
        if not os.path.exists('Guess the Word'):
            os.mkdir('Guess the Word')
            os.chdir('./Guess the Word')

    def setup_database(self):
        db = sqlite3.connect('database.sqlite3')
        db_cursor = db.cursor()
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS extra
            (
                id INTEGER PRIMARY KEY,
                level TEXT NOT NULL,
                max_score INTEGER DEFAULT 0
            )
        ''')
        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS used_words
            (
                id INTEGER PRIMARY KEY,
                word TEXT NOT NULL
            )
        ''')
        db.commit()
        db_cursor.close()
        db.close()
