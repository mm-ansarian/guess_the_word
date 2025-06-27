'''
This module defines the user interface for the Guess the Word application using PyQt6.
It sets up the main window, widgets and signal-slot connections.
'''


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from functools import partial
from options import Options
import sys 


class MainWindow(QtWidgets.QMainWindow):
    def setup_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setObjectName("main_window")
        main_window.setWindowTitle(_translate("main_window", "Guess the Word"))

        self.font = QtGui.QFont()
        self.font.setFamily("MV Boli")
        self.font.setPointSize(94)

        self.centralwidget = QtWidgets.QWidget(parent=main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)

        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.grid_layout.setObjectName("gridLayout")

        spacer_item1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        spacer_item2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.grid_layout.addItem(spacer_item1, 0, 0, 1, 1)
        self.grid_layout.addItem(spacer_item2, 0, 2, 1, 1)
        
        self.starting_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.starting_label.setEnabled(True)
        self.starting_label.setFont(self.font)
        self.starting_label.setObjectName("starting_label")
        self.starting_label.setText(_translate("main_window", "Guess the Word"))

        self.grid_layout.addWidget(self.starting_label, 1, 1, 1, 1)

        self.menubar = QtWidgets.QMenuBar(parent=main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(main_window)

        QTimer.singleShot(3000, self.choose_level_page)

        self.font.setPointSize(30)

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("VerticalLayout")

        self.welcome_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.welcome_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.welcome_label.setFont(self.font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setObjectName("WelcomeLabel")
        self.welcome_label.setText(_translate("MainWindow", "Welcome to this game!"))
        self.vertical_layout.addWidget(self.welcome_label)
        
        self.choose_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.choose_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.choose_label.setFont(self.font)
        self.choose_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.choose_label.setObjectName("ChooseLabel")
        self.choose_label.setText(_translate("MainWindow", "Please choose your game level:"))
        self.vertical_layout.addWidget(self.choose_label)
        
        spacer_item3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vertical_layout.addItem(spacer_item3)
        
        self.basic_lvl_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.basic_lvl_button.setFont(self.font)
        self.basic_lvl_button.setObjectName("BasicLVLButton")
        self.basic_lvl_button.setText(_translate("MainWindow", "Basic"))
        self.vertical_layout.addWidget(self.basic_lvl_button)
        
        self.intermediate_lvl_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.intermediate_lvl_button.setFont(self.font)
        self.intermediate_lvl_button.setObjectName("IntermediateLVLButton")
        self.intermediate_lvl_button.setText(_translate("MainWindow", "Intermediate"))
        self.vertical_layout.addWidget(self.intermediate_lvl_button)
        
        self.professional_lvl_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.professional_lvl_button.setFont(self.font)
        self.professional_lvl_button.setObjectName("ProfessionalLVLButton")
        self.professional_lvl_button.setText(_translate("MainWindow", "Professional"))
        self.vertical_layout.addWidget(self.professional_lvl_button)

        self.expert_lvl_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.expert_lvl_button.setFont(self.font)
        self.expert_lvl_button.setObjectName("LegendryLVLButton")
        self.expert_lvl_button.setText(_translate("MainWindow", "Expert"))
        self.vertical_layout.addWidget(self.expert_lvl_button)

        self.grid_layout.addLayout(self.vertical_layout, 1, 1, 1, 1)
        spacer_item4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)

        self.grid_layout.addItem(spacer_item4, 2, 1, 1, 1)
        spacer_item5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.grid_layout.addItem(spacer_item5, 0, 1, 1, 1)

        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(2, 4)
        self.grid_layout.setRowStretch(2, 2)

        self.welcome_label.setVisible(False)
        self.choose_label.setVisible(False)
        self.basic_lvl_button.setVisible(False)
        self.intermediate_lvl_button.setVisible(False)
        self.professional_lvl_button.setVisible(False)
        self.expert_lvl_button.setVisible(False)
        self.vertical_layout.setEnabled(False)

        Options.setup_app_folder(Options)
        Options.setup_database(Options)

        self.setup_signals()

    def setup_signals(self):
        self.basic_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'basic'))
        self.intermediate_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'intermediate'))
        self.professional_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'professional'))
        self.expert_lvl_button.clicked.connect(lambda: UiReactions.choose_level_signal(self, 'expert'))

    def choose_level_page(self):
        self.starting_label.setVisible(False)
        del self.starting_label
        self.welcome_label.setVisible(True)
        self.choose_label.setVisible(True)
        self.basic_lvl_button.setVisible(True)
        self.intermediate_lvl_button.setVisible(True)
        self.professional_lvl_button.setVisible(True)
        self.expert_lvl_button.setVisible(True)


class UiReactions(MainWindow):
    def __init__(self):
        super().setup_ui(self)

    def choose_level_signal(self, level):
        self.choose_label.setVisible(False)
        self.welcome_label.setVisible(False)
        self.basic_lvl_button.setVisible(False)
        self.intermediate_lvl_button.setVisible(False)
        self.professional_lvl_button.setVisible(False)
        self.expert_lvl_button.setVisible(False)
        self.level = level
        print(self.level)
