import httpx
from lxml import etree
import pandas as pd
from http.cookiejar import MozillaCookieJar
import re
import os

netscape_cookie_file = './cookies.txt'
url = "https://www.yooc.me/group/6167499/exam/302086/detail"

jar = MozillaCookieJar(netscape_cookie_file)
jar.load()
res = httpx.get(url, cookies=jar)
html = etree.HTML(res.text)
question_boards = html.xpath('//div[@class="question-board"]')


def parse_single_choice(question_board: etree._Element):
    question = {}
    score_board = question_board[0]
    title_board = question_board[1]
    choice_board = question_board[2]
    answer_board = question_board[3]

    question['title'] = title_board.text
    answer = answer_board[0].text
    assert answer.startswith('正确答案')
    question['answer'] = answer
    question['choices'] = []
    for choice in choice_board:
        question['choices'].append(choice.text)
    return question


def record_question(question: dict):
    db_path = './db.csv'
    if not os.path.exists(db_path):
        df = pd.DataFrame(columns=['title', 'choices', 'answer'])
        df.to_csv(db_path, index=False)
    db = pd.read_csv(db_path)
    # if this question is already in the db, do nothing
    if question['title'] in db['title'].values:
        return False
    db = db.append(question, ignore_index=True)
    db.to_csv(db_path, index=False)
    return True


for question_board in question_boards:
    ### single choice
    question = parse_single_choice(question_board)
    record_question(question)
