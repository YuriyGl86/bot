from bot.bot import Bot
from bot.bot_token import key



bot = Bot(key)


for event in bot.longpoll.listen():  # Запускаем бесконечный цикл, начинаем слушать сервер ВК
    if event.type == bot.VkEventType.MESSAGE_NEW and event.to_me and event.text:  # И если тип события это новое сообщение и оно для меня и в нем есть текст
        received_message = event.text  # Сохраняем полученное сообщение
        sender = event.user_id  # Получаем ID пользователя, с которым общаемся

        user = bot.get_user_info(sender)
        print(user)

        if received_message.lower() in ('привет', 'начать'):
            bot.write_message(sender, 'Добрый день')
        elif received_message.lower() == 'в избранное':
            bot.write_message(sender, 'Вызываем функцию добавления в избранное')
        elif received_message.lower() == 'к следующему':
            candidate = bot.send_candidate(sender)
        elif received_message.lower() == 'список избранных':
            bot.write_message(sender, 'Вызываем функцию вывода списка избранных')
        elif received_message.lower() == 'в черный список':
            bot.write_message(sender, 'Вызываем функцию добавления в ЧС')
        else:
            bot.write_message(sender, 'Ничего не понятно, но очень интересно!\nЛучше воспользуйтесь одной из моих возможностей')  # , attachment=attch

