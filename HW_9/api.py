import requests
import json
from tok import token
from task_calc import calculator
from task_dec_to_bin import dec_to_bin
from task_negafib import negafib
from questions import quest

url = "https://api.telegram.org/"


def send_bottom(chat_id, text_1, text_2, text_3, text_4):
    headers = {'Content-Type': 'application/json'}
    data = {"chat_id": str(chat_id),
            "text": "Выберете пункт меню",
            "reply_markup": {
                "keyboard": [[{"text": text_1}, {"text": text_2}],
                             [{"text": text_3}, {"text": text_4}]],
                "resize_keyboard": True,
                "one_time_keyboard": True}}
    requests.post(f'{url}bot{token}/sendmessage?', data=json.dumps(data), headers=headers)


def send_message(chat_id, text):
    requests.get(f'{url}bot{token}/sendmessage?chat_id={chat_id}&text={text}')


class MyTelBot:
    def __init__(self):
        response = json.loads(requests.get(f'{url}bot{token}/getupdates').text)
        if response['ok']:
            print("Бот стартанул")
            if response['result']:
                self.update_id = response['result'][-1]['update_id'] + 1
            else:
                self.update_id = None
        self.chats = {}

    def run_bot(self):
        while True:
            response = json.loads(requests.get(f'{url}bot{token}/getupdates?timeout=10&offset={self.update_id}').text)
            if response['ok']:
                if response['result']:
                    for msg in response['result']:
                        chat_id = msg['message']['chat']['id']
                        text = msg['message']['text']

                        if self.chats.get(chat_id):
                            self.chats[chat_id].processing_message(text)
                        else:
                            first_name = msg['message']['chat']['first_name']
                            chat = Chat(chat_id, first_name)
                            self.chats[chat_id] = chat
                            chat.processing_message(text)

                    self.update_id = response['result'][-1]['update_id'] + 1


class Chat:

    def __init__(self, chat_id, first_name):
        self.chat_id = chat_id
        self.first_name = first_name
        self.calc = False
        self.dec_to_bin = False
        self.negafib = False
        self.quiz = False
        self.operation = ("Вычислить_выражение", "Десятичное_в_двоичное", "Числа_НегаФибоначчи", "Викторина")

    def processing_message(self, text):
        if self.calc:
            send_message(self.chat_id, f'Ответ {calculator(text)}')
            self.calc = False
            send_bottom(self.chat_id, *self.operation)
        elif self.dec_to_bin:
            send_message(self.chat_id, f'Ответ {dec_to_bin(text)}')
            self.dec_to_bin = False
            send_bottom(self.chat_id, *self.operation)
        elif self.negafib:
            send_message(self.chat_id, negafib(text))
            self.negafib = False
            send_bottom(self.chat_id, *self.operation)
        elif self.quiz:
            pass
        else:
            match text:
                case "/start":
                    send_message(self.chat_id, f'Привет {self.first_name}')
                    send_bottom(self.chat_id, *self.operation)
                case "Вычислить_выражение":
                    self.calc = True
                    send_message(self.chat_id, 'Введите математическое выражение')
                case "Десятичное_в_двоичное":
                    self.dec_to_bin = True
                    send_message(self.chat_id, 'Введите десятичное число')
                case "Числа_НегаФибоначчи":
                    self.negafib = True
                    send_message(self.chat_id, 'Введите число и я выведу числа НегаФибоначчи')
                case "Викторина":
                    self.quiz = True
                    run_quiz = Quiz
                case _:
                    send_bottom(self.chat_id, *self.operation)


class Quiz:
    def __init__(self):
        self.end_quest = len(quest) - 1
        self.current_quest = 0

    def ask_question(self):
        pass
