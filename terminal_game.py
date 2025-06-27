'''
This is a module that allows you to run the game in your terminal.
So there is no GUI or anything else when you use this file to play the game.
'''


from random import randint
from sys import exit


easy_level_words_list = [
    'Banana', 'Apple', 'Tomato', 'Potato', 'Green', 'Yellow', 'Bedroom', 'Balloon',
    'Bubble', 'Cheese', 'Cookie', 'Door', 'Dinner', 'Floor', 'Address', 'Jelly', 
    'Pepper', 'Summer', 'Sweet', 'Window', 'Book', 'Dollar', 'Feet', 'Coffee', 
    'Hill', 'Hammer', 'Noon', 'Room', 'Tall', 'Tool', 'Week', 'Wood', 'Ladder', 
    'Mirror', 'Puzzle', 'Rabbit', 'School', 'Tunnel', 'Letter', 'Coconut', 'Pineapple',
    'Notebook', 'Notification', 'Truth', 'Rare', 'Pillow', 'Kick'
]
medium_level_words_list = [
    'Computer', 'Programming', 'Mountain', 'Python', 'Orange', 'Planet', 'Star', 'Galaxy',
    'Plant', 'Yard', 'Kitchen', 'Truck', 'Race', 'Raid', 'Express', 'Toilet', 'Joker', 'Earth',
    'Blank', 'Punch', 'Karate'
]
hard_level_words_list = [
    'Smartphone', 'Professional', 'Jupyter', 'Mercury', 'Blanket', 'Redemption', 'Knight',
    'Playground', 'Beautiful', 'Nightmare', 'Gladiator', 'Metallica', 'Minecraft', 'Taekwondo', 
    'Interstellar',
]
legendry_level_words_list = [
     
]

print('\n\n\n\n\n')
print(
    '''
                            **********************************
                            **********************************
                            **********************************
                            **********************************
                            ********* Guess the word *********
                            **********************************
                            **********************************
                            **********************************
                            **********************************
''')
print('\n\n')
print('Welcome to this game.\n\nYou should guess some words in this game.\n')
print('Pay attention that you can guess only one letter each turn.\n')
print("Let's start playing right now!\n")


while True:
    level = input('Which level are you going to play? Easy, medium, hard or legendry(e/m/h/l)? ')
    print('\n')
    if level.lower() not in ['e', 'm', 'h', 'l']:
        print('Invalid Input.')
        exit()
    
    elif level.lower() == 'e':
        if len(easy_level_words_list) == 0:
            print(
            'You have reached the limit of playing in easy level;' +
            '\nYou can choose another level ^__^\n'
            )
            continue
        number_of_turns = 15
        selected_word = easy_level_words_list[randint(0, len(easy_level_words_list) - 1)]
        easy_level_words_list.remove(selected_word)
    elif level.lower() == 'm':
        if len(medium_level_words_list) <= 0:
            print(
            'You have reached the limit of playing in medium level;' +
            '\nYou can choose another level ^__^\n'
            )
            continue
        number_of_turns = 10
        selected_word = medium_level_words_list[randint(0, len(medium_level_words_list) - 1)]
        medium_level_words_list.remove(selected_word)
    elif level.lower() == 'h':
        if len(hard_level_words_list) <= 0:
            print(
            'You have reached the limit of playing in hard level;' +
            '\nYou can choose another level ^__^\n'
            )
            continue
        number_of_turns = 5
        selected_word = hard_level_words_list[randint(0, len(hard_level_words_list) - 1)]
        hard_level_words_list.remove(selected_word)
    elif level.lower() == 'l':
        if len(legendry_level_words_list) <= 0:
            print(
            'You have reached the limit of playing in legendry level;' +
            '\nYou can choose another level ^__^\n'
            )
            continue
        number_of_turns = 3
        selected_word = legendry_level_words_list[randint(0, len(legendry_level_words_list) - 1)]
        legendry_level_words_list.remove(selected_word)
    

    displaying_list = ['_ '] * len(selected_word) 

    while True:
        if number_of_turns == 0:
            print(f'Word = {selected_word}')
            print('Oops! You reached the limit of your turns; You lose.\n\n')
            break

        print(f'Just {number_of_turns} turns remaining.')
        guessed_letter = input(
            f'Guess the word or one of the letters of the word "{''.join(displaying_list)}": '
        )

        print('\n')

        if len(guessed_letter) > 1:
            if guessed_letter.lower() == selected_word.lower():
                displaying_list = selected_word
            else:
                number_of_turns -= 3
        elif guessed_letter.lower() in selected_word.lower():
            for i in range(len(selected_word)):
                if guessed_letter.lower() == selected_word.lower()[i]:
                    displaying_list[i] = selected_word[i] 
        else:
            number_of_turns -= 1

        if ''.join(displaying_list) == selected_word or displaying_list == selected_word:
            print(f'Word = {selected_word}')
            print('Congratulations! You successfully guessed the word.\n\n')
            break
    
    ask = input('Do you want to play again(y / n)? ')
    if ask.lower() == 'y':
        print('\n\n')
        continue
    print('\nOk.')
    break

    
print('\n\n\n\n\n')
