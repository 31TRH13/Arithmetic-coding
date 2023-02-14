import random
import os

"""
Прогрмамма генерирует случайные тексты длинной от 500 до 3000 символом
"""

def gen():
    length = random.randint(500,3000)
    text = ""
    for i in range(length):
        text += chr(random.randint(65,90))
    return text


for i in range(1,101):
    text_file = open(f"./texts/{i}/input.txt","w")
    text_file.write(gen())
    text_file.close()


