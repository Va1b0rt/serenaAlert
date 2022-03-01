from datetime import datetime

from pyrogram import Client
from pyrogram.types import Message

import db_worker

api_id = 0
api_hash = ''


def message_checker():
    with Client('session', api_id, api_hash) as client:
        return message_processor(client.get_history(-1001511672343)[0])
        #return message_processor(client.get_history('@qwertingo')[0])


def message_processor(message: Message):
    last_id = db_worker.select_message()[0][2]
    if last_id != message.message_id:
        db_worker.update_message(last_id, f'{datetime.now().strftime("%d-%m-%Y %H:%M")}',
                                 message.text, str(message.message_id))

        return f'{datetime.now().strftime("%d-%m-%Y %H:%M")}  {message.text} '


if __name__ == '__main__':
    print(message_checker())
