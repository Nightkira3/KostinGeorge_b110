__author__ = 'Костин Георгий'


import math
import random


class Character(object):

    def __init__(self, name, MAX_hp, base_speed, priority="Normal", mindset_multiplier=1.0):
        self.MAX_hp = MAX_hp
        self.base_hp = MAX_hp
        self.base_speed = base_speed
        self.priority = priority
        self.mindset_multiplier = mindset_multiplier
        self.name = name
        self.move_pool = {}

    def __repr__(self):
        return (f"{self.name} - {self.base_hp} / {self.MAX_hp} HP,"
                f" {self.mindset_multiplier} mindset, {self.base_speed} speed")


class Move(object):

    def __init__(self, description="", self_damage=0, damage=0, mindset_multiplier=1.0, opponent_mindset_multiplier=1.0,
                 speed_boost=0, opponent_speed_boost=0, priority="Normal"):
        self.__doc__ = description
        self.self_damage = self_damage
        self.damage = damage
        self.mindset_multiplier = mindset_multiplier
        self.opponent_mindset_multiplier = opponent_mindset_multiplier
        self.speed_boost = speed_boost
        self.opponent_speed_boost = opponent_speed_boost
        self.priority = priority

    def __call__(self, attacker=None, opponent=None):
        if attacker is not None:
            attacker.priority = self.priority
            attacker.mindset_multiplier *= self.mindset_multiplier
            attacker.base_speed += self.speed_boost
            attacker.base_hp -= math.floor(self.self_damage *
                                           attacker.mindset_multiplier)
            attacker.base_hp = min(max(attacker.base_hp, 0), attacker.MAX_hp)

        if opponent is not None:
            opponent.mindset_multiplier *= self.opponent_mindset_multiplier
            opponent.base_speed += self.speed_boost
            opponent.base_hp -= math.floor(self.damage *
                                           attacker.mindset_multiplier)
            opponent.base_hp = min(max(opponent.base_hp, 0), opponent.MAX_hp)


class Berserker(Character):
    def __init__(self):
        Character.__init__("Berserker", 250, 75)
        self.move_pool = {"1": Move(" Jab - Быстрая, легкая атака. Наносит противнику 30 базового урона",
                                    damage=30, priority="Fast"),
                          "2": Move(" Reaper - Медленная, сильная атака. Наносит 65 базового урона противнику и "
                                    "30 базового урона пользователю", self_damage=30, damage=65, priority="Slow"),
                          "3": Move(" PumpUp - Нормальная скорость. Улучшает мышление пользователя ( x 1.25 )",
                                    mindset_multiplier=1.25)}


class Priest(Character):
    def __init__(self):
        Character.__init__(self, "Priest", 220, 80)
        self.move_pool = {"1": Move(" Heal - Движение с нормальной скоростью. "
                                    "Восстанавливает пользователю базовые 30 здоровья", self_damage=-30),
                          "2": Move(" Scourge - Атака с нормальной скоростью. Наносит 40 базового урона противнику",
                                    damage=40),
                          "3": Move(" Meditate - Движение с нормальной скоростью. "
                                    "Улучшает мышление пользователя (x 1.35)", mindset_multiplier=1.35)}


class Trickster(Character):

    class Bag_o_tricks(Move):

        def __call__(self, attacker, opponent):
            self.damage = random.uniform(-1, 1) * 100
            self.self_damage = random.uniform(-1, 1) * 50
            Move.__call__(self, attacker, opponent)

    class Swapper(Move):

        def __call__(self, attacker, opponent):
            attacker.priority = self.priority
            attacker.base_hp, opponent.base_hp = opponent.base_hp, attacker.base_hp
            attacker.MAX_hp, opponent.MAX_hp = opponent.MAX_hp, attacker.MAX_hp

    def __init__(self):
        Character.__init__(self, "Trickster", 175, 100)
        self.move_pool = {"1": Trickster.Bag_o_tricks(" Bag-O-Tricks - Движение с нормальной скоростью. "
                                                      "Увеличивает или уменьшает HP противника  от 0 до 100, "
                                                      "а HP пользователя - от 0 до 50"),
                          "2": Move(" Tease - A Normal-speed move. Reduces the Mindset of the Opponent (x 0.8)",
                                    mindset_multiplier=1.05, opponent_mindset_multiplier=0.8),
                          "3": Trickster.Swapper(" Swapper - Движение с нормальной скоростью. "
                                                 "Меняет HP пользователя на HP противника")}

