'''
This module prepares some new features to give the user the best experience.
It prepares the project folder and the database of the application and some other important actions.
'''


from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
import sqlite3
import getpass
import random
import ctypes
import sys
import os

wrong_letters = []

accepted_inputs = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

basic_level_words_list = [
    'Banana', 'Apple', 'Tomato', 'Potato', 'Green', 'Yellow', 'Bedroom', 'Balloon', 'Drink',
    'Bubble', 'Cheese', 'Cookie', 'Door', 'Dinner', 'Floor', 'Address', 'Jelly', 'Soda', 'Wolf',
    'Pepper', 'Summer', 'Sweet', 'Window', 'Book', 'Dollar', 'Feet', 'Coffee', 'Water', 'Fox',
    'Hill', 'Hammer', 'Noon', 'Room', 'Tall', 'Tool', 'Week', 'Wood', 'Ladder', 'Sugar', 'Bee',
    'Mirror', 'Puzzle', 'Rabbit', 'School', 'Tunnel', 'Letter', 'Coconut', 'Pineapple', 'Ant',
    'Notebook', 'Notification', 'Truth', 'Rare', 'Pillow', 'Kick', 'Professor', 'Chicken', 'Bat',
    'Common', 'Classic', 'Paradise', 'Hell', 'Wheel', 'Wall', 'Pen', 'Chair', 'eye', 'Honey',
    'Bag', 'Sun', 'Moon', 'Cat', 'Dog', 'Hat', 'Fish', 'Shoes', 'Tree', 'Rain', 'Milk', 'Ball', 
    'Bed', 'Fan', 'Nose', 'Hand', 'Deer', 'Old', 'Yong', 'Gray', 'Blue', 'White', 'Black', 'Pizza',
    'Pasta', 'Glue', 'Cube', 'Car', 'Baker', 'Painter', 'Waiter', 'Barber', 'Builder', 'Gardener',
    'Seller', 'Dentist', 'Owl', 'Lion', 'Bird', 'Cow', 'Pig', 'Horse', 'Sheep', 'Frog', 'Bear', 
    'Rat', 'Lamp', 'Egg', 'Salad', 'Soup', 'Cake', 'Cafe', 'Tea', 'Sad', 'Hungry', 'Thirsty', 'Arm',
    'Finger', 'Chest', 'Front', 'Back', 'Skin', 'Hen', 'Mother', 'Father', 'Brother', 'Sister',
    'Uncle', 'Cousin', 'Wife', 'Son', 'Laptop',
]

intermediate_level_words_list = [
    'Computer', 'Programming', 'Mountain', 'Orange', 'Planet', 'Star', 'Galaxy', 'Spirit',
    'Plant', 'Yard', 'Kitchen', 'Truck', 'Race', 'Raid', 'Express', 'Toilet', 'Joker', 'Earth',
    'Blank', 'Punch', 'Karate', 'Judo', 'England', 'Hole', 'Habit', 'Core', 'Culture', 'Mars',
    'Uranus', 'Pluto', 'Pattern', 'Torch', 'Plastic', 'Liquid', 'Camel', 'Compleat', 'Love',
    'Engineering', 'Driver', 'Soldier', 'River', 'Bottle', 'Jungle', 'Holiday', 'Track', 'Music',
    'Forest', 'Basket', 'Village', 'Pirate', 'Castle', 'Machine', 'Airport', 'Boat', 'Dark', 'Light',
    'Monster', 'Butterfly', 'Candle', 'Planetarium', 'Table', 'Firefighter', 'Private', 'Postman',
    'Cup', 'Spoon', 'Phone', 'Snow', 'Bus', 'Duck', 'Dress', 'Sunlight', 'Sight', 'Policy',
    'Glass', 'Rocket', 'Garden', 'Doctor', 'Writer', 'Cloud', 'Friend', 'Fact', 'Police', 'Law',
    'Energy', 'Result', 'Answer', 'Bridge', 'Island', 'Artist', 'Programmer', 'Legal', 'Speed',
    'Nation', 'Shadow', 'Signal', 'Hunter', 'Office', 'Dream', 'Rubik', 'Long', 'Circle', 'Cleaner',
    'Triangle', 'Rectangle', 'Little', 'Bookshelf', 'Chef', 'Cooker', 'Teacher', 'Nurse', 'Farmer',
    'Cashier', 'Brush', 'Plate', 'Metal', 'Bull', 'Clock', 'Bread', 'Rise', 'Beef', 'Carrot', 
    'Juice', 'Head', 'Ear', 'Mouth', 'Neck', 'Shoulder', 'Angry', 'Happy', 'Exiting', 'Knee',
    'Foot', 'Brain', 'Teeth', 'Headache', 'Toothache', 'Eyebrow', 'Fire', 'Afraid', 'Kickboxing',
    'Mushroom', 'Husband', 'Plaster', 'Jupiter', 'Homeless',
]

professional_level_words_list = [
    'Smartphone', 'Professional', 'Jupyter', 'Saturn', 'Mercury', 'Blanket', 'Knight',
    'Playground', 'Beautiful', 'Nightmare', 'Minecraft', 'Taekwondo', 'Gas', 'Accelerate',
    'Interstellar', 'Solid', 'Chemistry', 'Algorithm', 'Strategy', 'Behavior', 'Electricity', 
    'Database', 'Astronomy', 'Instrument', 'Festival', 'Experiment', 'Microphone', 'Universe', 
    'Astronaut', 'Satellite', 'Philosophy', 'Volcano', 'Mathematics', 'Survivor', 'Animation', 
    'Champion', 'Explorer', 'Magician','Discovery', 'Language', 'Workshop', 'Psychology', 
    'Scientist', 'Electrician', 'Composer', 'Ambition', 'Engineer', 'Adventure', 'Evolution', 
    'Daughter', 'Inception', 'Gravity', 
]

expert_level_words_list = [
    'Gladiator', 'Redemption', 'Helicopter', 'Runway', 'Lecture', 'Framework', 'Module', 
    'Revolution', 'Cryptocurrency', 'Artificial', 'Astrophysics', 'Synchronization', 
    'Unpredictable', 'Philosophical', 'Thermodynamics', 'Psychologist', 'Microscopic',
    'Cinematography', 'Electromagnetic', 'Cryptography', 'Cybersecurity', 'Interpreter', 
    'Phenomenon', 'Architecture', 'International', 'Biotechnology', 'Personality',
]


def message_box(title: str, text: str, number: int) -> None:
    return ctypes.windll.user32.MessageBoxW(0, text, title, number)


class Database:
    base_path = os.path.join('C:/Users', getpass.getuser(), 'AppData', 'Local')
    os.chdir(base_path)

    @classmethod
    def setup_app_folder(cls):
        if not os.path.exists('Guess the Word'):
            os.mkdir('Guess the Word')
            os.chdir('./Guess the Word')
            with sqlite3.connect('database.sqlite3') as db:
                pass
        os.chdir(os.path.join(cls.base_path, 'Guess the Word'))

    @classmethod
    def tables_exist(cls):
        cls.setup_app_folder()
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            try:
                db_cursor.execute('''
                    SELECT * FROM used_words
                ''').fetchall()
                db_cursor.execute('''
                    SELECT * FROM extra
                ''').fetchall()
            except:
                return False
            else: 
                return True

    @classmethod
    def setup_database(cls):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            db_cursor.execute('''
                CREATE TABLE IF NOT EXISTS extra
                (
                    id INTEGER PRIMARY KEY,
                    level TEXT NOT NULL,
                    max_score INTEGER DEFAULT 0,
                    is_active BOOLEAN DEFAULT FALSE
                )
            ''')
            db_cursor.execute('''
                CREATE TABLE IF NOT EXISTS used_words
                (
                    id INTEGER PRIMARY KEY,
                    level TEXT NOT NULL,
                    word TEXT NOT NULL
                )
            ''')
            try:
                db_cursor.execute('''
                    INSERT INTO extra (id, level, max_score, is_active)
                    VALUES (?, ?, ?, ?)
                ''', (1, 'basic', 0, True))
                db_cursor.execute('''
                    INSERT INTO extra (id, level, max_score)
                    VALUES (?, ?, ?)
                ''', (2, 'intermediate', 0))
                db_cursor.execute('''
                    INSERT INTO extra (id, level, max_score)
                    VALUES (?, ?, ?)
                ''', (3, 'professional', 0))
                db_cursor.execute('''
                    INSERT INTO extra (id, level, max_score)
                    VALUES (?, ?, ?)
                ''', (4, 'expert', 0))
            except:
                pass
            finally:
                db.commit()
    @classmethod
    def edit_level(cls, level):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            db_cursor.execute('''
                UPDATE extra
                SET is_active = ?
                WHERE level = ?
            ''', (True, level))
            db_cursor.execute('''
                UPDATE extra
                SET is_active = ?
                WHERE level != ?
            ''', (False, level))
            db.commit()

    @classmethod
    def edit_max_score(cls, level, score):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            db_cursor.execute('''
                UPDATE extra
                SET max_score = ?
                WHERE level = ?
            ''', (score, level))
            db.commit()

    @classmethod
    def edit_used_words_table(cls, level, word):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            db_cursor.execute('''
                INSERT INTO used_words (level, word)
                    VALUES (?, ?)
                ''', (level, word))
            db.commit()

    @classmethod
    def clear_words_table(cls, level):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            db_cursor.execute('''
                DELETE FROM used_words
                WHERE level = ?
                ''', (level,))
            db.commit()

    @classmethod
    def fetch_everything(cls):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            extra_data = db_cursor.execute('''
                SELECT * FROM extra
                WHERE is_active = ?
            ''', (True,)).fetchall()
            used_words_data = db_cursor.execute('''
                SELECT word FROM used_words
                WHERE level = ?
            ''', (extra_data[0][1],)).fetchall()
            result = {
                'level': extra_data[0][1], 
                'high_score': extra_data[0][2], 
                'used_words': [row[0] for row in used_words_data]}
            return result
    
    @classmethod
    def clear_cache(cls):
        with sqlite3.connect('database.sqlite3') as db:
            db_cursor = db.cursor()
            db_cursor.execute("""
                DROP TABLE IF EXISTS used_words;
            """)
            db_cursor.execute("""
                DROP TABLE IF EXISTS extra;
            """)
            db.commit()
    

class MessageWindow(QWidget):
    def __init__(self, message, color, button_text, on_button_click, icon_path=None):
        super().__init__()
        self._on_close_callback = on_button_click
        self.setWindowTitle('Result')
        self.setFixedSize(320, 180)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {color};
                border-radius: 10px;
                border: 2px solid black;
            }}
        """)

        if icon_path:
            icon = QtGui.QIcon(QtGui.QPixmap(icon_path))
            self.setWindowIcon(icon)

        layout = QVBoxLayout()

        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Weight.Bold))
        label.setStyleSheet("color: white;")
        layout.addWidget(label)

        btn = QPushButton(button_text)
        btn.setStyleSheet("background-color: white; color: black; font-weight: bold; padding: 6px;")
        btn.clicked.connect(lambda: self._handle_button(on_button_click))
        layout.addWidget(btn)

        self.setLayout(layout)

    def _handle_button(self, func):
        if func:
            func()
        self.close()

    def closeEvent(self, event):
        if hasattr(self, '_on_close_callback') and self._on_close_callback:
            self._on_close_callback()
        event.accept()

    @classmethod
    def show_victory(cls, on_button_click=None):
        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, 'icons', 'correct_icon.ico')
        else:
            icon_path = os.path.join(os.path.dirname(__file__), 'icons', 'correct_icon.ico')

        win = cls(
            f"🎉 Congratulations!\n\nYou guessed it!\nWord: {PrimaryActions.chosen_word}",
            "#38a169",
            "Play Another Turn",
            on_button_click,
            icon_path 
        )
        win.show()
        return win

    @classmethod
    def show_defeat(cls, on_button_click=None):
        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, 'icons', 'wrong_icon.ico')
        else:
            icon_path = os.path.join(os.path.dirname(__file__), 'icons', 'wrong_icon.ico')

        lose = cls(
            f"💀 Game Over!\n\nYou're out of attempts.\nThe word was: {PrimaryActions.chosen_word}",
            "#e53e3e",
            "Play Another Turn",
            on_button_click,
            icon_path  
        )
        lose.show()
        return lose
    
    
class PrimaryActions:
    def choose_random_word(self, obj):
        result = Database.fetch_everything()
        self.level = result.get('level')
        high_score = result.get('high_score')
        used_words = result.get('used_words')
        self.chosen_word = ''
        if self.level == 'basic':
            if len(used_words) >= len(basic_level_words_list):
                Database.clear_words_table(self.level)
            else:
                self.chosen_word = random.choice(basic_level_words_list)
                while self.chosen_word in used_words:
                    self.chosen_word = random.choice(basic_level_words_list)
            obj.attempts_left_number_label.setText('18')
            obj.game_LVL_combo.setCurrentIndex(0)

        elif self.level == 'intermediate':
            if len(used_words) >= len(intermediate_level_words_list):
                Database.clear_words_table(self.level)
            else:
                self.chosen_word = random.choice(intermediate_level_words_list)
                while self.chosen_word in used_words:
                    self.chosen_word = random.choice(intermediate_level_words_list)
            obj.attempts_left_number_label.setText('13')
            obj.game_LVL_combo.setCurrentIndex(1)

        elif self.level == 'professional':
            if len(used_words) >= len(professional_level_words_list):
                Database.clear_words_table(self.level)
            else:
                self.chosen_word = random.choice(professional_level_words_list)
                while self.chosen_word in used_words:
                    self.chosen_word = random.choice(professional_level_words_list)
            obj.attempts_left_number_label.setText('7')
            obj.game_LVL_combo.setCurrentIndex(2)

        elif self.level == 'expert':
            if len(used_words) >= len(expert_level_words_list):
                Database.clear_words_table(self.level)
            else:
                self.chosen_word = random.choice(expert_level_words_list)
                while self.chosen_word in used_words:
                    self.chosen_word = random.choice(expert_level_words_list)
            obj.attempts_left_number_label.setText('5')
            obj.game_LVL_combo.setCurrentIndex(3)
        
        self.displaying_list = ['-'] * len(self.chosen_word)
        obj.guessing_label.setText(' '.join(self.displaying_list))
        obj.high_score_number_label.setText(str(high_score))
        wrong_letters.clear()
        obj.wrong_guessed_letters.setText('_____________')    

    def one_letter_chose(self, obj, submitted_letter):
        global wrong_letters
        if submitted_letter in accepted_inputs:
            if submitted_letter in self.chosen_word.lower():
                for i in range(len(self.chosen_word.lower())):
                    if submitted_letter == self.chosen_word.lower()[i]:
                        self.displaying_list[i] = self.chosen_word[i]
                obj.guessing_label.setText(' '.join(self.displaying_list))   
                if ''.join(obj.guessing_label.text().split(' ')) == self.chosen_word:
                    obj.current_score_number_label.setText(
                        str(int(obj.current_score_number_label.text()) + 1)
                    )
                    wrong_letters.clear()
                    if int(obj.current_score_number_label.text()) > int(obj.high_score_number_label.text()):
                        obj.high_score_number_label.setText(obj.current_score_number_label.text())
                        Database.edit_max_score(
                            level=self.level,
                            score=int(obj.high_score_number_label.text())
                        )
                    Database.edit_used_words_table(level=self.level, word=self.chosen_word)
                    MessageWindow.show_victory(
                            on_button_click=lambda: obj.loading_page(1, obj.init_main_game_signal, text='.Loading.')
                    )

            else:
                if submitted_letter not in wrong_letters:
                        wrong_letters.append(submitted_letter) 
                        obj.wrong_guessed_letters.setText(' '.join(wrong_letters))
                        obj.attempts_left_number_label.setText(
                            str(int(obj.attempts_left_number_label.text()) - 1)
                        )
                if int(obj.attempts_left_number_label.text()) <= 0:
                    obj.guessing_label.setText(self.chosen_word) 
                    wrong_letters.clear()
                    if (int(obj.current_score_number_label.text()) - 2) >= 0:
                        obj.current_score_number_label.setText(
                            str(int(obj.current_score_number_label.text()) - 2)
                        )
                    else:
                        obj.current_score_number_label.setText('0')
                        
                    Database.edit_used_words_table(level=self.level, word=self.chosen_word)
                    MessageWindow.show_defeat(
                        on_button_click=lambda: obj.loading_page(1, obj.init_main_game_signal, text='.Loading.')
                    )
