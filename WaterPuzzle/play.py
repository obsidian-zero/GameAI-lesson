"""
@DATE: 2021/7/14
@Author: Ziqi Wang
@File: play.py
"""
from Waterpuzzle.waterpuzzle import WaterPuzzle


if __name__ == '__main__':
    # for _ in range(100):
    game = WaterPuzzle('levels/2.txt')
    game.run(True)
