import time

import pandas as pd
import re
import keyboard
from clipBoardManager import ClipBoardManager

db = pd.read_csv('./db.csv')


def query_question(title):
    for i in range(len(db)):
        if title in db.loc[i, 'title']:
            question = db.loc[i]
            print(question['title'])
            print(question['choices'])
            print(question['answer'])


def callback():
    time.sleep(0.1)
    query_question(ClipBoardManager.get_text_from_clipboard())


keyboard.add_hotkey("ctrl+c", callback)
keyboard.wait()
