## Introduction
"Guess the Word" is an entertaining and simple game about the English words.
If you like, you can run it in terminal(the terminal version of this game is available right now). Or you can play this game in its own special GUI!

## How to Play
In this game, a word is selected. You don't know what is the selected word and you should find the selected word by guessing each letter of the word.
For example for the word "Play", "_ _ _ _" will be shown to you and you have a limit of turns to guess the letters; if you guess the "p" and "a" letters, the shown 
word will transform to "P _ a _". If you could guess all the letters or whole the word successfully(before finishing your turns), you win; otherwise
you lose.
You will discover the other things and the different methods after playing the game for several times. 😊

## How to Run

#### With Terminal
To run this game in your terminal, follow the steps below:
  1. Install `python3` on your system.
  2. Clone the project repository using `git`:
     ```bash
     git clone git@github.com:mm-ansarian/guess_the_word.git
     ```
     or
     ```bash
     git clone https://github.com/mm-ansarian/guess_the_word.git
     ```
  3. Open the project folder.
  4. Run `terminal_game.py`(using your IDE or your terminal).
  5. Enjoy 😉

#### Using the application(Including GUI and the best features)
We have also provided you a very beautiful graphical user interface so you can run this game as a 
executable file that allows you to have more facilities.
After installing `python3`, cloning the project and installing the requirements using `pip install -r requirements.txt` command, You can run the game easily by running `app.py`. 
But, if you want to have an executable fila from this project and run it as a real application, follow the steps bellow:
  1. Install `python3` on your system.
  2. Clone the project repository using `git`:
     ```bash
     git clone git@github.com:mm-ansarian/guess_the_word.git
     ```
     or
     ```bash
     git clone https://github.com/mm-ansarian/guess_the_word.git
     ```
  3. Install the required packages in your virtual environment.
     ```bash
     pip install -r requirements.txt
     ```
  4. Install the `pyintaller` package in your venv or system.
     ```bash
     pip install pyinstaller
     ```
  5. Use this command to make `Guess the Word.exe` in your current directory:
      ```bash
      pyinstaller --noconfirm --onefile --windowed --icon "<path_to_the_project_folder>\icons\Main_icon.ico" --name "Guess the Word" --add-data "<path_to_the_project_folder>\icons\Main_icon.ico;." --add-data "<path_to_the_project_folder>\icons;icons/"  "<path_to_the_project_folder>\app.py"
      ```
  6. Enjoy 😉🎉

**If you notice any bugs or problems, I'll be very grateful if you tell me or help me to develop this application 🌱**


## Details
- **Operation System**: Windows 10/11
- **Programming language**: Python3
- **Database**: SQLite3
- **GUI**: QT6

## TODO
- [X] Develop the application(with a beautiful GUI and the best features).
- [ ] Add dark mode feature.
- [ ] Style the project`s source code.
- [ ] Using the best algorithms and design patterns for the project as the final step.
     
