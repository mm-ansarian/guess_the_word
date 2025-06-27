'''
This module initializes and runs the main application using PyQt6 for the GUI.
'''


from PyQt6 import QtWidgets
import gui as ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    screen = app.primaryScreen()
    screen_width = screen.availableGeometry().width()
    screen_height = screen.availableGeometry().height()
    main_window.resize(screen_width, screen_height)
    main_window.showMaximized()

    ui = ui.MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec())
