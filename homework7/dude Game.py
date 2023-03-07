__author__ = 'Костин Георгий'

import sys
import os
import time
from Characters import *


class Game(object):

    mode_options = {'1': ('Игрок 1', 'Комп.'), '2': ('Комп.1', 'Комп.2'), '3': ('Игрок 1', 'Игрок 2')}
    game_mode = ''
    game_mode_choice = ''

    character_options = {'1': Berserker, '2': Priest, '3': Trickster}
    move_order = ''

    def __init__(self):
        ...

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def introduction(self):
        game.clear_screen()
        time.sleep(0.3)
        game.clear_screen()

    def choose_game_mode(self):
        while True:
            self.game_mode_choice = input("В каком режиме битвы, вы хотели бы поиграть: \
                \n1) Игрок vs Комп. \
                \n2) Комп.1 vs Комп.2 \
                \n3) Игрок 1 vs Игрок 2 \
                \n\
                \n0) Выход.\n\n")

            game.clear_screen()

            if self.game_mode_choice == '0':
                sys.exit()
            try:
                self.game_mode = self.mode_options[self.game_mode_choice]
                return None
            except KeyError:
                print("Пожалуйста, выберите один из перечисленных вариантов.\n")
                time.sleep(1)

    def character_selection(self, controller_index):
        while True:
            character_choice = input("Кого выберет " + self.game_mode[controller_index] + ":\
                \n1) Берсеркер\
                \n2) Священник\
                \n3) Обманщик\
                \n4) Рандомный выбор\
                \n\
                \n0) Выход.\n\n")

            game.clear_screen()

            if character_choice == '0':
                sys.exit()
            elif character_choice == '4':
                character_choice = str(random.randint(1, 3))

            try:
                return self.character_options[character_choice]
            except KeyError:
                print("Пожалуйста, выберите один из перечисленных вариантов.\n")
                time.sleep(1)

    def hp_check(self, controller_1, controller_2):
        if controller_1.base_hp <= 0:
            if controller_2.base_hp > 0:
                self.clear_screen()
                print("Победил игрок № 2!")
                sys.exit()
            else:
                self.clear_screen()
                print("Ничья!!!")
                sys.exit()
        elif controller_2.base_hp <= 0:
            self.clear_screen()
            print("Победил игрок № 1!")
            sys.exit()
        else:
            pass

    def player_choose_move(self, controller, controller_index):
        while True:
            move_choice = input(self.game_mode[controller_index] + ", выберите действие:\
            \n1)" + controller.move_pool['1'].__doc__ + "\
            \n2)" + controller.move_pool['2'].__doc__ + "\
            \n3)" + controller.move_pool['3'].__doc__ + "\n\n")

            try:
                controller.move = controller.move_pool[move_choice]
                return None
            except KeyError:
                game.clear_screen()
                print("Пожалуйста, выберите один из перечисленных вариантов.\n")
                time.sleep(1)

    def comp_choose_move(self, controller):
        controller.move = controller.move_pool[random.choice(['1', '2', '3'])]

    def priority_and_speed_check(self, controller1, controller2):
        if controller1.priority > controller2.priority:
            return True
        elif controller1.priority == controller2.priority:
            if controller1.base_speed > controller2.base_speed:
                return True
            elif controller1.base_speed == controller2.base_speed:
                return bool(random.randint(0, 1))
            else:
                return False
        else:
            return False

    def update(self, controller1, controller2):
        print(self.game_mode[0],
              " HP:", str(Player_1.base_hp), "\n", self.game_mode[0],
              "Скорость: x", str(Player_1.mindset_multiplier), "\n")
        print(self.game_mode[1], 
              " HP:", str(Player_2.base_hp), "\n", self.game_mode[1],
              "Скорость: x", str(Player_2.mindset_multiplier), "\n")
        print("\n\n")

    def move_collection(self, controller1, controller2):
        if self.game_mode_choice == '1':
            self.update(Player_1, Player_2)
            self.player_choose_move(Player_1, 0)
            self.clear_screen()

            self.update(Player_1, Player_2)
            self.comp_choose_move(Player_2)
            self.clear_screen()

        elif self.game_mode_choice == '2':
            self.update(Player_1, Player_2)
            self.comp_choose_move(Player_1)
            self.clear_screen()

            self.update(Player_1, Player_2)
            self.comp_choose_move(Player_2)
            self.clear_screen()

        else:
            self.update(Player_1, Player_2)
            self.player_choose_move(Player_1, 0)
            self.clear_screen()

            self.update(Player_1, Player_2)
            self.player_choose_move(Player_2, 1)
            self.clear_screen()

    def move_application(self, controller1, controller2):
        if self.priority_and_speed_check(Player_1, Player_2):
            Player_1.move(Player_1, Player_2)
            self.hp_check(Player_1, Player_2)

            Player_2.move(Player_2, Player_1)
            self.hp_check(Player_1, Player_2)
        else:
            Player_2.move(Player_2, Player_1)
            self.hp_check(Player_1, Player_2)

            Player_1.move(Player_1, Player_2)
            self.hp_check(Player_1, Player_2)


game = Game()
game.introduction()
game.choose_game_mode()

(Player_1, Player_2) = (game.character_selection(0)(), game.character_selection(1)())
while True:
    game.move_collection(Player_1, Player_2)
    game.move_application(Player_1, Player_2)
