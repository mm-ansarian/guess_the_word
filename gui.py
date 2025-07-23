'''
This module defines the user interface for the Guess the Word application using PyQt6.
It sets up the main window, widgets and signal-slot connections.
'''


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from options import *
import sys


class MainWindow(QtWidgets.QMainWindow):
    def setup_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setObjectName('main_window')
        main_window.setWindowTitle(_translate('main_window', 'Guess the Word'))
        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, 'main_icon.ico')
        else:
            icon_path = os.path.join(os.path.dirname(__file__), 'icons', 'main_icon.ico')
        icon = QtGui.QIcon(QtGui.QPixmap(icon_path))
        main_window.setWindowIcon(icon)

        self.font = QtGui.QFont()
        self.font.setFamily('MV Boli')
        self.font.setPointSize(94)

        self.central_widget = QtWidgets.QWidget(parent=main_window)
        self.central_widget.setObjectName('centralwidget')
        main_window.setCentralWidget(self.central_widget)

        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setObjectName('gridLayout')
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        spacer_item1 = QtWidgets.QSpacerItem(
            250, 20, 
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        spacer_item2 = QtWidgets.QSpacerItem(
            250, 20, 
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Minimum
        )

        self.grid_layout.addItem(spacer_item1, 0, 0, 1, 1)
        self.grid_layout.addItem(spacer_item2, 0, 2, 1, 1)
        
        self.starting_label = QtWidgets.QLabel(parent=self.central_widget)
        self.starting_label.setEnabled(True)
        self.starting_label.setFont(self.font)
        self.starting_label.setObjectName('starting_label')
        self.starting_label.setText(_translate('main_window', 'Guess the Word'))
        self.starting_label.setStyleSheet('color: rgb(170, 0, 255);')

        self.grid_layout.addWidget(self.starting_label, 1, 1, 1, 1)

        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName('menubar')
        main_window.setMenuBar(self.menubar)

        self.font.setPointSize(30)

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName('VerticalLayout')

        self.welcome_label = QtWidgets.QLabel(parent=self.central_widget)
        self.welcome_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.welcome_label.setFont(self.font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setObjectName('WelcomeLabel')
        self.welcome_label.setText(_translate('MainWindow', 'Welcome to this game!'))
        self.welcome_label.setStyleSheet('color: rgb(170, 0, 255);')

        self.vertical_layout.addWidget(self.welcome_label)
        
        self.choose_label = QtWidgets.QLabel(parent=self.central_widget)
        self.choose_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.choose_label.setFont(self.font)
        self.choose_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.choose_label.setObjectName('ChooseLabel')
        self.choose_label.setText(_translate('MainWindow', 'Please choose your game level:'))
        self.choose_label.setStyleSheet('color: rgb(170, 0, 255);')

        spacer_item3 = QtWidgets.QSpacerItem(
            20, 20, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.vertical_layout.addWidget(self.choose_label)
        self.vertical_layout.addItem(spacer_item3)
        
        self.basic_lvl_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.basic_lvl_button.setFont(self.font)
        self.basic_lvl_button.setObjectName('BasicLVLButton')
        self.basic_lvl_button.setText(_translate('MainWindow', 'Basic'))
        self.basic_lvl_button.setStyleSheet('color: green;')

        self.vertical_layout.addWidget(self.basic_lvl_button)
        
        self.intermediate_lvl_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.intermediate_lvl_button.setFont(self.font)
        self.intermediate_lvl_button.setObjectName('IntermediateLVLButton')
        self.intermediate_lvl_button.setText(_translate('MainWindow', 'Intermediate'))
        self.intermediate_lvl_button.setStyleSheet('color: blue;')

        self.vertical_layout.addWidget(self.intermediate_lvl_button)
        
        self.professional_lvl_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.professional_lvl_button.setFont(self.font)
        self.professional_lvl_button.setObjectName('ProfessionalLVLButton')
        self.professional_lvl_button.setText(_translate('MainWindow', 'Professional'))
        self.professional_lvl_button.setStyleSheet('color: orange;')

        self.vertical_layout.addWidget(self.professional_lvl_button)

        self.expert_lvl_button = QtWidgets.QPushButton(parent=self.central_widget)
        self.expert_lvl_button.setFont(self.font)
        self.expert_lvl_button.setObjectName('LegendryLVLButton')
        self.expert_lvl_button.setText(_translate('MainWindow', 'Expert'))
        self.expert_lvl_button.setStyleSheet('color: red;')

        self.vertical_layout.addWidget(self.expert_lvl_button)

        self.grid_layout.addLayout(self.vertical_layout, 1, 1, 1, 1)
        spacer_item4 = QtWidgets.QSpacerItem(
            20, 20, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.grid_layout.addItem(spacer_item4, 2, 1, 1, 1)
        spacer_item5 = QtWidgets.QSpacerItem(
            20, 15, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.grid_layout.addItem(spacer_item5, 0, 1, 1, 1)
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(2, 4)
        self.grid_layout.setRowStretch(2, 2)

        self.tab_widget = QtWidgets.QTabWidget(parent=self.central_widget)

        self.font.setPointSize(14)
        self.tab_widget.setFont(self.font)
        self.tab_widget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tab_widget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setMovable(False)
        self.tab_widget.setTabBarAutoHide(False)
        self.tab_widget.setObjectName('tabWidget')
        self.tab_widget.setStyleSheet('color: rgb(170, 0, 255);')

        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setFont(self.font)
        self.main_tab.setObjectName('main_tab')

        self.vertical_layout = QtWidgets.QVBoxLayout(self.main_tab)
        self.vertical_layout.setObjectName('verticalLayout')
        self.vertical_layout1 = QtWidgets.QVBoxLayout()
        self.vertical_layout1.setSpacing(0)
        self.vertical_layout1.setObjectName('VerticalLayout1')

        self.font.setPointSize(36)
        self.word_label = QtWidgets.QLabel(parent=self.main_tab)
        self.word_label.setFont(self.font)
        self.word_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_label.setObjectName('WordLabel')
        self.word_label.setText(_translate('MainWindow', 'Word'))
        self.word_label.setStyleSheet('color: rgb(170, 0, 255);')

        self.vertical_layout1.addWidget(self.word_label)

        self.font.setPointSize(36)
        self.guessing_label = QtWidgets.QLabel(parent=self.main_tab)
        self.guessing_label.setFont(self.font)
        self.guessing_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guessing_label.setObjectName('Guessing_Label')
        self.guessing_label.setText(_translate('MainWindow', '_ _ _ _'))
        self.guessing_label.setStyleSheet('color: rgb(170, 0, 255);')

        spacer_item6 = QtWidgets.QSpacerItem(
            20, 40, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.vertical_layout1.addWidget(self.guessing_label)
        self.vertical_layout1.addItem(spacer_item6)

        self.horizontal_layout1 = QtWidgets.QHBoxLayout()
        self.horizontal_layout1.setSpacing(4)
        self.horizontal_layout1.setObjectName('HorizontalLayout1')

        self.vertical_layout2 = QtWidgets.QVBoxLayout()
        self.vertical_layout2.setObjectName('VerticalLayout2')

        self.font.setPointSize(28)
        self.current_score_label = QtWidgets.QLabel(parent=self.main_tab)
        self.current_score_label.setFont(self.font)
        self.current_score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_score_label.setObjectName('CurrentScoreLabel')
        self.current_score_label.setText(_translate('MainWindow', 'Current score'))
        self.current_score_label.setStyleSheet('color: rgb(15, 202, 12);')

        self.vertical_layout2.addWidget(self.current_score_label)

        self.font.setPointSize(28)
        self.current_score_number_label = QtWidgets.QLabel(parent=self.main_tab)
        self.current_score_number_label.setFont(self.font)
        self.current_score_number_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_score_number_label.setObjectName('CurrentScoreNumber')
        self.current_score_number_label.setText(_translate('MainWindow', '0'))
        self.current_score_number_label.setStyleSheet('color: rgb(15, 202, 12);')

        self.vertical_layout2.addWidget(self.current_score_number_label)
        self.horizontal_layout1.addLayout(self.vertical_layout2)
        self.vertical_layout3 = QtWidgets.QVBoxLayout()
        self.vertical_layout3.setObjectName('VerticalLayout3')
        self.attempts_left_label = QtWidgets.QLabel(parent=self.main_tab)

        self.font.setPointSize(28)
        self.attempts_left_label.setFont(self.font)
        self.attempts_left_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.attempts_left_label.setObjectName('TurnsLabel')
        self.attempts_left_label.setText(_translate('MainWindow', 'Attempts left'))
        self.attempts_left_label.setStyleSheet('color: orange;')
        
        self.vertical_layout3.addWidget(self.attempts_left_label)

        self.font.setPointSize(28)
        self.attempts_left_number_label = QtWidgets.QLabel(parent=self.main_tab)
        self.attempts_left_number_label.setFont(self.font)
        self.attempts_left_number_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.attempts_left_number_label.setObjectName('TurnsNumber')
        self.attempts_left_number_label.setText(_translate('MainWindow', '3'))
        self.attempts_left_number_label.setStyleSheet('color: orange;')

        self.vertical_layout3.addWidget(self.attempts_left_number_label)
        self.horizontal_layout1.addLayout(self.vertical_layout3)
        self.vertical_layout4 = QtWidgets.QVBoxLayout()
        self.vertical_layout4.setObjectName('VerticalLayout4')

        self.font.setPointSize(28)
        self.high_score_label = QtWidgets.QLabel(parent=self.main_tab)
        self.high_score_label.setFont(self.font)
        self.high_score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.high_score_label.setObjectName('HighLabel')
        self.high_score_label.setText(_translate('MainWindow', 'High score'))
        self.high_score_label.setStyleSheet('color: rgb(0, 0, 255)')

        self.vertical_layout4.addWidget(self.high_score_label)

        self.font.setPointSize(28)
        self.high_score_number_label = QtWidgets.QLabel(parent=self.main_tab)
        self.high_score_number_label.setFont(self.font)
        self.high_score_number_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.high_score_number_label.setObjectName('HighNumber')
        self.high_score_number_label.setText(_translate('MainWindow', '37'))
        self.high_score_number_label.setStyleSheet('color: rgb(0, 0, 255)')

        self.vertical_layout4.addWidget(self.high_score_number_label)
        self.horizontal_layout1.addLayout(self.vertical_layout4)
        self.vertical_layout1.addLayout(self.horizontal_layout1)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.vertical_layout1.addItem(spacerItem7)

        self.font.setPointSize(28)
        self.wrong_guessed_letters_label = QtWidgets.QLabel(parent=self.main_tab)
        self.wrong_guessed_letters_label.setFont(self.font)
        self.wrong_guessed_letters_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wrong_guessed_letters_label.setObjectName('WrongGuessedLettersLabel')
        self.wrong_guessed_letters_label.setText(_translate('MainWindow', 'Wrong letters'))
        self.wrong_guessed_letters_label.setStyleSheet('color: red;')

        self.vertical_layout1.addWidget(self.wrong_guessed_letters_label)

        self.font.setPointSize(28)
        self.wrong_guessed_letters = QtWidgets.QLabel(parent=self.main_tab)
        self.wrong_guessed_letters.setFont(self.font)
        self.wrong_guessed_letters.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wrong_guessed_letters.setObjectName('WrongGuessedLetters')
        self.wrong_guessed_letters.setText(_translate('MainWindow', 'A B C F J K'))
        self.wrong_guessed_letters.setStyleSheet('color: red;')

        spacer_item8 = QtWidgets.QSpacerItem(
            20, 40, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )
        spacer_item9 = QtWidgets.QSpacerItem(
            40, 20, 
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Minimum
        )

        self.vertical_layout1.addWidget(self.wrong_guessed_letters)
        self.vertical_layout1.addItem(spacer_item8)

        self.horizontal_layout2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout2.setObjectName('HorizontalLayout2')
        self.horizontal_layout2.addItem(spacer_item9)

        self.font.setPointSize(28)
        self.word_textbox = QtWidgets.QLineEdit(parent=self.main_tab)
        self.word_textbox.setFont(self.font)
        self.word_textbox.setInputMask('')
        self.word_textbox.setText('')
        self.word_textbox.setMaxLength(1)
        self.word_textbox.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.word_textbox.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.word_textbox.setObjectName('WordTextBox')
        self.word_textbox.setPlaceholderText(_translate('MainWindow', 'Enter a letter'))
        self.word_textbox.setStyleSheet('''QLineEdit {
			color: rgb(170, 0, 255);
			border: 1px solid;
			border-radius: 6px;
			padding-left: 10px;
			padding-bottom: 5px;
            text-align: center;
		}''')

        self.hide_button = QtWidgets.QPushButton(parent=self.main_tab)
        self.hide_button.setFont(self.font)
        self.hide_button.setText('Submit')
        self.hide_button.setVisible(False)
        
        spacer_item9 = QtWidgets.QSpacerItem(
            40, 20, 
            QtWidgets.QSizePolicy.Policy.Expanding, 
            QtWidgets.QSizePolicy.Policy.Minimum
        )

        self.horizontal_layout2.addWidget(self.word_textbox)
        self.horizontal_layout2.addItem(spacer_item9)
        self.horizontal_layout2.setStretch(0, 1)
        self.horizontal_layout2.setStretch(1, 1)
        self.horizontal_layout2.setStretch(2, 1)
        
        self.vertical_layout1.addLayout(self.horizontal_layout2)
        
        spacer_item10 = QtWidgets.QSpacerItem(
            20, 40, 
            QtWidgets.QSizePolicy.Policy.Minimum, 
            QtWidgets.QSizePolicy.Policy.Expanding
        )

        self.vertical_layout1.addItem(spacer_item10)
        self.vertical_layout1.setStretch(0, 2)
        self.vertical_layout1.setStretch(1, 2)
        self.vertical_layout1.setStretch(2, 3)
        self.vertical_layout1.setStretch(3, 2)
        self.vertical_layout1.setStretch(4, 2)
        self.vertical_layout1.setStretch(5, 2)
        self.vertical_layout1.setStretch(6, 2)
        self.vertical_layout1.setStretch(7, 3)
        self.vertical_layout1.setStretch(8, 1)
        self.vertical_layout1.setStretch(9, 2)
        self.vertical_layout.addLayout(self.vertical_layout1)
        
        self.tab_widget.addTab(self.main_tab, '')
        
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName('settings')
        
        self.font.setPointSize(20)
        self.game_LVL_label = QtWidgets.QLabel(parent=self.settings)
        self.game_LVL_label.setGeometry(QtCore.QRect(0, 10, 161, 33))
        self.game_LVL_label.setText(_translate('MainWindow', 'Game level: '))
        self.game_LVL_label.setFont(self.font)
        self.game_LVL_label.setObjectName('GameLVLLabel')
        self.game_LVL_combo = QtWidgets.QComboBox(parent=self.settings)
        self.game_LVL_combo.setEnabled(True)
        self.game_LVL_combo.setGeometry(QtCore.QRect(180, 10, 170, 40))
        
        self.font.setPointSize(16)
        self.game_LVL_combo.setFont(self.font)
        self.game_LVL_combo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.game_LVL_combo.setEditable(False)
        self.game_LVL_combo.setMaxVisibleItems(10)
        self.game_LVL_combo.setObjectName('GameLVLCombo')
        self.game_LVL_combo.addItem('')
        self.game_LVL_combo.addItem('')
        self.game_LVL_combo.addItem('')
        self.game_LVL_combo.addItem('')
        self.game_LVL_combo.setCurrentText(_translate('MainWindow', 'Basic'))
        self.game_LVL_combo.setItemText(0, _translate('MainWindow', 'Basic'))
        self.game_LVL_combo.setItemText(1, _translate('MainWindow', 'Intermediate'))
        self.game_LVL_combo.setItemText(2, _translate('MainWindow', 'Professional'))
        self.game_LVL_combo.setItemText(3, _translate('MainWindow', 'Expert'))
        
        self.font.setPointSize(20)
        self.game_color_label = QtWidgets.QLabel(parent=self.settings)
        self.game_color_label.setGeometry(QtCore.QRect(0, 70, 171, 33))
        self.game_color_label.setFont(self.font)
        self.game_color_label.setObjectName('GameColorLabel')
        self.game_color_label.setText(_translate('MainWindow', 'Color theme:'))
        
        self.font.setPointSize(16)
        self.game_color_combo = QtWidgets.QComboBox(parent=self.settings)
        self.game_color_combo.setEnabled(True)
        self.game_color_combo.setGeometry(QtCore.QRect(180, 70, 170, 40))
        self.game_color_combo.setFont(self.font)
        self.game_color_combo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.game_color_combo.setObjectName('GameColorCombo')
        self.game_color_combo.addItem('')
        self.game_color_combo.setItemText(0, _translate('MainWindow', 'Light'))
        
        self.font.setPointSize(20)
        self.game_cache_label = QtWidgets.QLabel(parent=self.settings)
        self.game_cache_label.setGeometry(QtCore.QRect(0, 130, 161, 33))
        self.game_cache_label.setFont(self.font)
        self.game_cache_label.setObjectName('GameCacheLabel')
        self.game_cache_label.setText(_translate('MainWindow', 'Game cache:'))
        
        self.font.setPointSize(20)
        self.clear_cache_btn = QtWidgets.QPushButton(parent=self.settings)
        self.clear_cache_btn.setGeometry(QtCore.QRect(180, 130, 170, 41))
        self.clear_cache_btn.setFont(self.font)
        self.clear_cache_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_cache_btn.setObjectName('ClearCacheBtn')
        self.clear_cache_btn.setText(_translate('MainWindow', 'Clear cache'))
        self.font.setPointSize(20)
        self.clear_cache_btn.setStyleSheet('color: rgb(255, 0, 0);')
        
        self.font.setPointSize(20)
        self.change_LVL_btn = QtWidgets.QPushButton(parent=self.settings)
        self.change_LVL_btn.setGeometry(QtCore.QRect(370, 10, 130, 40))
        self.change_LVL_btn.setFont(self.font)
        self.change_LVL_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.change_LVL_btn.setObjectName('ChangeLevelBtn')
        self.change_LVL_btn.setText(_translate('MainWindow', 'Change'))
        self.change_LVL_btn.setStyleSheet('color: rgb(170, 0, 255);')
        
        self.tab_widget.addTab(self.settings, '')
        self.grid_layout.addWidget(self.tab_widget, 0, 0, 1, 1)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 18))
        self.menubar.setObjectName('menubar')
        main_window.setMenuBar(self.menubar)

        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.main_tab), _translate('MainWindow', 'Main tab'))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.settings), _translate('MainWindow', 'Settings'))
        self.game_LVL_combo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.setup_signals()
        self.setup_shortcuts()
        self.setup_database()

    def setup_database(self):    
        if Database.tables_exist():
            self.loading_page(3, self.init_main_game_signal)
        else:
            self.loading_page(8, self.choose_level_page)
            Database.setup_database()

    def setup_signals(self):
        self.tab_widget.currentChanged.connect(lambda: UiReactions.tab_index_changed(self))
        self.basic_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'basic'))
        self.intermediate_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'intermediate'))
        self.professional_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'professional'))
        self.expert_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'expert'))
        self.change_LVL_btn.clicked.connect(lambda: UiReactions.change_LVL_btn_clicked(self))
        self.clear_cache_btn.clicked.connect(lambda: UiReactions.clear_cache_signal(self))
        self.game_LVL_combo.activated.connect(
            lambda: UiReactions.game_LVL_changed_signal(self, self.game_LVL_combo.currentText())
        )

    def setup_shortcuts(self):
        tab_shortcut1 = QtGui.QShortcut(QtGui.QKeySequence('Alt+Right'), self.tab_widget)
        tab_shortcut2 = QtGui.QShortcut(QtGui.QKeySequence('Alt+Down'), self.tab_widget)
        tab_shortcut3 = QtGui.QShortcut(QtGui.QKeySequence('Alt+Left'), self.tab_widget)
        tab_shortcut4 = QtGui.QShortcut(QtGui.QKeySequence('Alt+Up'), self.tab_widget)
        tab_shortcut1.activated.connect(lambda: UiReactions.next_tab_shortcut(self))
        tab_shortcut2.activated.connect(lambda: UiReactions.next_tab_shortcut(self))
        tab_shortcut3.activated.connect(lambda: UiReactions.previous_tab_shortcut(self))
        tab_shortcut4.activated.connect(lambda: UiReactions.previous_tab_shortcut(self))

        self.word_textbox.returnPressed.connect(lambda: UiReactions.letter_submitted(self))

    def loading_page(self, interval, func, text='Guess the Word'):
        self.starting_label.setVisible(False)
        self.welcome_label.setVisible(False)
        self.choose_label.setVisible(False)
        self.basic_lvl_button.setVisible(False)
        self.intermediate_lvl_button.setVisible(False)
        self.professional_lvl_button.setVisible(False)
        self.expert_lvl_button.setVisible(False)
        self.tab_widget.setHidden(True)
        self.starting_label.setText(text)
        self.starting_label.setVisible(True)
        QTimer.singleShot(interval*1000, func)

    def init_main_game_signal(self):
        self.starting_label.setVisible(False)
        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.setHidden(False)
        self.game_LVL_combo.setEnabled(False)
        self.word_textbox.setFocus()
        self.grid_layout.addWidget(self.tab_widget, 0, 0, 3, 3)
        PrimaryActions.choose_random_word(PrimaryActions, obj=self)

    def choose_level_page(self):
        self.starting_label.setVisible(False)
        self.welcome_label.setVisible(True)
        self.choose_label.setVisible(True)
        self.basic_lvl_button.setVisible(True)
        self.intermediate_lvl_button.setVisible(True)
        self.professional_lvl_button.setVisible(True)
        self.expert_lvl_button.setVisible(True)


class UiReactions(MainWindow):
    def __init__(self):
        super().setup_ui(self)

    def tab_index_changed(self):
        self.change_LVL_btn.setEnabled(True)
        self.game_LVL_combo.setEnabled(False)

    def next_tab_shortcut(self) -> None:
        if self.tab_widget.currentIndex() == 0:
            self.tab_widget.setCurrentIndex(1)

        elif self.tab_widget.currentIndex() == 1:
            self.tab_widget.setCurrentIndex(2)

        elif self.tab_widget.currentIndex() == 2:
            self.tab_widget.setCurrentIndex(0)
    
    def previous_tab_shortcut(self) -> None:
        if self.tab_widget.currentIndex() == 2:
            self.tab_widget.setCurrentIndex(1)

        elif self.tab_widget.currentIndex() == 1:
            self.tab_widget.setCurrentIndex(0)

        elif self.tab_widget.currentIndex() == 0:
            self.tab_widget.setCurrentIndex(2)

    def choose_level_signal(self, level):
        self.choose_label.setVisible(False)
        self.welcome_label.setVisible(False)
        self.basic_lvl_button.setVisible(False)
        self.intermediate_lvl_button.setVisible(False)
        self.professional_lvl_button.setVisible(False)
        self.expert_lvl_button.setVisible(False)
        Database.edit_level(level=level)
        self.loading_page(1, self.init_main_game_signal, text='.Loading.')

    def change_LVL_btn_clicked(self):
        status = message_box(
            title='Attention',
            text="Changing the game level will set your current score to 0. Do you want to continue?",
            number=36
        )
        self.game_LVL_combo.setEnabled(True)
        self.change_LVL_btn.setEnabled(False)

    def game_LVL_changed_signal(self, level):
        self.game_LVL_combo.setEnabled(False)
        Database.edit_level(level=level.lower())
        result = Database.fetch_everything()
        self.current_score_number_label.setText('0')
        self.high_score_number_label.setText(str(result['high_score']))
        self.loading_page(1, self.init_main_game_signal, text='.Loading.')

    def letter_submitted(self):
        if self.word_textbox.text() != '':
            PrimaryActions.one_letter_chose(
                PrimaryActions, self, self.word_textbox.text().lower()
            )
            self.word_textbox.setText('')

    def clear_cache_signal(self):
        status = message_box(
            title='!! Be careful !!',
            text="If you clear the cache of this game, all your data such as your level, maximum score and played words will be deleted and it's like running the program for the first time. Are you sure you want to clear the cache?",
            number=52
        )
        if status == 6:
            Database.clear_cache()
            self.setup_database()
            self.current_score_number_label.setText('0')
            self.loading_page(8, self.choose_level_page, text='Guess the Word')
        else:
            pass
