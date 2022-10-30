import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from bot_token import key
from func import write_message, upload_photo

authorize = vk_api.VkApi(token=key)  # Авторизуемся в ВК для управления нашей группой, используя token
longpoll = VkLongPoll(authorize)  # Выбираем тип используемого API - Long Poll API, бывает еще Callback API
upload = VkUpload(authorize)  # Загрузчик изображений на сервер в ВК

keyboard = VkKeyboard(one_time=False)  # создаем клавиатуру для бота

keyboard.add_button('К следующему', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('В избранное', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('В черный список', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('Список избранных', color=VkKeyboardColor.SECONDARY)






for event in longpoll.listen():  # Запускаем бесконечный цикл, начинаем слушать сервер ВК
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # И если тип события это новое сообщение и оно для меня и в нем есть текст
        received_message = event.text  # Сохраняем полученное сообщение
        sender = event.user_id  # Получаем ID пользователя, с которым общаемся

        if received_message.lower() in ('привет', 'начать'):
            write_message(authorize, sender, keyboard, 'Добрый день')
        elif received_message.lower() == 'в избранное':
            write_message(authorize, sender, keyboard, 'Вызываем функцию добавления в избранное')
        elif received_message.lower() == 'к следующему':
            write_message(authorize, sender, keyboard, 'Вызываем функцию перехода к следующему')
        elif received_message.lower() == 'список избранных':
            write_message(authorize, sender, keyboard, 'Вызываем функцию вывода списка избранных')
        elif received_message.lower() == 'в черный список':
            write_message(authorize, sender, keyboard, 'Вызываем функцию добавления в ЧС')
        else:
            res = []
            picture_url = 'https://vdp.mycdn.me/getImage?id=411588037337&idx=0&thumbType=32'
            picture_url2 = 'https://www.mam4.ru/media/upload/user/5422/19/6170.jpg'
            picture_url3 = 'https://avatanplus.com/files/resources/mid/5ab5736f0579416254cae9ae.png'
            res.append(upload_photo(upload,picture_url))
            res.append(upload_photo(upload,picture_url2))
            res.append(upload_photo(upload,picture_url3))
            attch = ','.join(res)
            print(res)
            write_message(authorize, sender, keyboard, 'Ничего не понятно, но очень интересно', attachment=attch)

