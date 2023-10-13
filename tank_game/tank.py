from constants_file.tank_constants import TANK_OPTIONS
import tkinter_logging_main
from collections import deque
import sqlite3

loger = tkinter_logging_main.Logger()


class Tank:
    def __init__(self):
        self.name = None
        self.x = 0
        self.y = 0
        self.target = [5, 5]
        self.shots = {"North": 0, "South": 0, "East": 0, "West": 0}
        self.directions = deque(["North", "East", "South", "West"])
        self.direction = self.directions[0]
        self.board_size = 10
        self.score = 100

    def turn_right(self):
        loger.logger.info(f"{self.name} turned right")
        print("Tank turned left")
        self.directions.rotate(1)
        self.direction = self.directions[0]

    def turn_left(self):
        loger.logger.info(f"{self.name} turned left")
        print("Tank turned right")
        self.directions.rotate(-1)
        self.direction = self.directions[0]

    def board(self):
        board = [['*' for _ in range(self.board_size)] for _ in range(self.board_size)]

        x, y = self.x, self.y
        direction_icon = {
            "North": "^",
            "South": "v",
            "East": ">",
            "West": "<",
        }
        tank_icon = direction_icon[self.direction]
        board[y][x] = tank_icon
        target_x, target_y = self.target[0], self.target[1]
        board[target_y][target_x] = 'O'

        for row in board:
            print(' '.join(row))

    def is_within_board(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def move(self, direction_x, direction_y):
        loger.logger.info(f"Tank moved to {direction_x}, {direction_y}")

        if self.direction == "North":
            direction_x, direction_y = (0, -1)
        elif self.direction == "South":
            direction_x, direction_y = (0, 1)
        elif self.direction == "East":
            direction_x, direction_y = (1, 0)
        elif self.direction == "West":
            direction_x, direction_y = (-1, 0)
        print(f"Tank moved to {self.direction}")

        new_x = self.x + direction_x
        new_y = self.y + direction_y
        if [new_x, new_y] == self.target:
            print("You can't move to the target location!")
        elif self.is_within_board(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.score -= 5
        else:
            print("YOU CANT MOVE THERE!")

    def is_next_to_target(self):
        x_diff = self.x - self.target[0]
        y_diff = self.y - self.target[1]
        return abs(x_diff) + abs(y_diff) <= 3

    def shoot(self):
        loger.logger.info(f"{self.name} shot at {self.direction}")

        x_diff = abs(self.x - self.target[0])
        y_diff = abs(self.y - self.target[1])
        print(f"X diff: {x_diff}, Y diff: {y_diff}")

        if x_diff > 3 or y_diff > 3:
            self.score -= 10
            print("You missed!")
            loger.logger.info(f"{self.name} missed!")

        if (self.direction == "North" and self.y > self.target[1] and self.x == self.target[0]) or \
                (self.direction == "South" and self.y <= self.target[1] and self.x == self.target[0]) or \
                (self.direction == "East" and self.x < self.target[0] and self.y == self.target[1]) or \
                (self.direction == "West" and self.x > self.target[0] and self.y == self.target[1]):
            self.score += 50
            self.shots[self.direction] += 1
            print("You shot and hit the target!")
            loger.logger.info(f"{self.name} shot and hit the target!")
        else:
            self.score -= 10
            print("You missed!")
            loger.logger.info(f"{self.name} missed!")

    def perform_action(self, choice):
        loger.logger.info(f"{self.name} performed action {choice}")
        actions = {
            1: (0, 1),
            2: self.turn_left,
            3: self.turn_right,
            4: self.shoot,
            5: self.top_players,
            6: self.save_score,
            7: self.exit_game,
        }

        try:
            action = actions.get(choice)
            if action:
                if callable(action):
                    action()
                else:
                    direction_x, direction_y = action
                    self.move(direction_x, direction_y)
            else:
                print("Invalid choice!")
        except ValueError as e:
            print(f"An error occurred: {e}")
            loger.logger.error(f"An error occurred: {e}")

    def game(self):
        print("Welcome to Tank Game!")
        self.name = input("What is your name?: ")
        loger.logger.info(f"Player: {self.name} started Tank game")

        while True:
            print(TANK_OPTIONS)
            choice = input("Choose an option: ")
            choice = int(choice)
            self.perform_action(choice)
            self.board()
            print("Score:", self.score)


    def save_score(self):
        loger.logger.info(f"Player: {self.name} saved score")
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            scores = [score.strip().split() for score in scores]

        found = False
        for i, score in enumerate(scores):
            if score[0] == self.name:
                scores[i][1] = str(self.score)
                found = True
                break

        if not found:
            scores.append([self.name, str(self.score)])

        with open("scores.txt", "w") as file:
            for score in scores:
                file.write(" ".join(score) + "\n")

    def top_players(self):
        loger.logger.info(f"Player: {self.name} checked top players")
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            scores = [score.strip().split() for score in scores]
            scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
            print(scores[:5])

    def exit_game(self):
        loger.logger.info(f"Player: {self.name} exited Tank game")
        exit()