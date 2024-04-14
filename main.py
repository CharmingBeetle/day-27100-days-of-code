import random
import time
import os

def rolldice(sides):
  dice = random.randint(1, sides)  
  return dice

def health(): 
  dice6 = rolldice(6)
  dice12 = rolldice(12)
  hth = ((dice6 * dice12) / 2) + 10
  return hth

def strength():
  dice6 = rolldice(6)
  dice12 = rolldice(12)
  st = ((dice6 * dice12) / 2) + 12
  return st

while True:
    print("Welcome to War of the Worlds Character Builder! 🎊")
    name = input("🥰 What is your character's name? ")  
    type = input("What is your character's type? (👨‍🦲 human, 🤡 elf, 🎅 wizard, 🐵 orc): ")
    print("Your character is", name, "and is a", type)
    time.sleep(1)
    print("Health:", health())
    time.sleep (1)
    print("Strength:", strength())
    time.sleep(1)
    play = input("Would you like to play again?: y / n ")
    if play == "y":
      print("You may proceed...")
      time.sleep(1)
      continue
    else:
      print("Thank you for playing!")
      break
        
  
  
    