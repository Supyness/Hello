import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time
import requests

def write_msg(user_id, random_id, message):
    vk_session.method('messages.send', {'user_id': user_id, "random_id": random_id, 'message': message})
    
token = "e96d71a03facb3c5a2b81ad52f19427587aef7c518d0cf8dee0e0ff372cb41643c5ba98bdaa6f55673e5d"
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            message = str(event.text)
            print(event.user_id)
            print(event.text)
            if event.from_user:
                r = requests.get('https://the-class.ru/project1425/admin_bot.php?message=' + message + '&user_id=' + str(event.user_id))
                print(r.content)
                print(r.text)
                write_msg(event.user_id, event.random_id, r.text)
