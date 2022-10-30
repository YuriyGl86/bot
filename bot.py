import requests
from io import BytesIO

from vk_api.utils import get_random_id
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class Bot:

    def __init__(self, key):
        self.authorize = vk_api.VkApi(token=key)  # Авторизуемся в ВК для управления нашей группой, используя token
        self.longpoll = VkLongPoll(
            self.authorize)  # Выбираем тип используемого API - Long Poll API, бывает еще Callback API
        self.upload = VkUpload(self.authorize)  # Загрузчик изображений на сервер в ВК

    @staticmethod
    def __get_keyboard_for_bot():
        keyboard = VkKeyboard(one_time=False)  # создаем клавиатуру для бота
        keyboard.add_button('К следующему', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('В избранное', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('В черный список', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Список избранных', color=VkKeyboardColor.SECONDARY)
        keyboard_for_bot = keyboard.get_keyboard()
        return keyboard_for_bot

    def write_message(self, sender, message, attachment=None):
        self.authorize.method('messages.send',
                              {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                               'attachment': attachment,
                               'keyboard': self.__get_keyboard_for_bot()})

    def upload_photo(self, url):
        img = requests.get(url).content
        f = BytesIO(img)

        response = self.upload.photo_messages(f)[0]

        owner_id = response['owner_id']
        photo_id = response['id']
        access_key = response['access_key']
        attachment = f'photo{owner_id}_{photo_id}'  # _{access_key}
        return attachment
