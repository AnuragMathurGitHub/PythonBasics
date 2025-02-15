#!/bin/python3

import math
import os
import random
import re
import sys

class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
        self.change = 0

    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        elif money < req_items * self.item_price:
            raise ValueError("Not enough coins")
        else:
            self.num_items -= req_items
            self.change = money - req_items * self.item_price
            return self.change

if __name__ == '__main__': 
    output_path = os.environ.get('OUTPUT_PATH', 'output.txt')
    with open(output_path, 'w') as fptr:
        num_items, item_coins = map(int, input().split())
        machine = VendingMachine(num_items, item_coins)

        n = int(input())
        for _ in range(n):
            num_items, num_coins = map(int, input().split())
            try:
                change = machine.buy(num_items, num_coins)
                fptr.write(str(change) + "\n")
            except ValueError as e:
                fptr.write(str(e) + "\n")
