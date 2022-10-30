from bot import Bot
from bot_token import key
from vk_api.longpoll import VkEventType

bot = Bot(key)

for event in bot.longpoll.listen():  # Запускаем бесконечный цикл, начинаем слушать сервер ВК
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # И если тип события это новое сообщение и оно для меня и в нем есть текст
        received_message = event.text  # Сохраняем полученное сообщение
        sender = event.user_id  # Получаем ID пользователя, с которым общаемся

        if received_message.lower() in ('привет', 'начать'):
            bot.write_message(sender, 'Добрый день')
        elif received_message.lower() == 'в избранное':
            bot.write_message(sender, 'Вызываем функцию добавления в избранное')
        elif received_message.lower() == 'к следующему':
            bot.write_message(sender, 'Вызываем функцию перехода к следующему')
        elif received_message.lower() == 'список избранных':
            bot.write_message(sender, 'Вызываем функцию вывода списка избранных')
        elif received_message.lower() == 'в черный список':
            bot.write_message(sender, 'Вызываем функцию добавления в ЧС')
        else:
            res = []
            picture_url = 'https://vdp.mycdn.me/getImage?id=411588037337&idx=0&thumbType=32'
            picture_url2 = 'https://www.mam4.ru/media/upload/user/5422/19/6170.jpg'
            picture_url3 = 'https://avatanplus.com/files/resources/mid/5ab5736f0579416254cae9ae.png'
            # res.append(bot.upload_photo(picture_url))
            # res.append(bot.upload_photo(picture_url2))
            # res.append(bot.upload_photo(picture_url3))
            attch = ','.join(res)
            print(res)
            bot.write_message(sender, 'Ничего не понятно, но очень интересно!\nВоспользуйтесь одной из моих возможностей')  # , attachment=attch