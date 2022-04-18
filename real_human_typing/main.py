import time
import random


def real_human_typing(word):
    word = word
    counter = 0
    for i in range(len(word)):
        time.sleep(round(random.random(), 1))
        print(word[i])
        i += 1


real_human_typing("Hello")
