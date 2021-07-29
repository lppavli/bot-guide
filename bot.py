# -*- coding: utf-8 -*-
import vk_api, random, time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


token = ""


vk = vk_api.VkApi(token = token)
vk._auth_token()


photos = ['photo-199392102_457239040', 'photo-199392102_457239053',
          'photo-199392102_457239054', 'photo-199392102_457239071',
          'photo-199392102_457239056', 'photo-199392102_457239057',
          'photo-199392102_457239061', 'photo-199392102_457239070',
          'photo-199392102_457239060', 'photo-199392102_457239062',
          'photo-199392102_457239063', 'photo-199392102_457239064',
          'photo-199392102_457239065', 'photo-199392102_457239069',
          'photo-199392102_457239067', 'photo-199392102_457239068',
          'photo-199392102_457239072', 'photo-199392102_457239073',
          'photo-199392102_457239074', 'photo-199392102_457239075',
          'photo-199392102_457239085', 'photo-199392102_457239077',
          'photo-199392102_457239078', 'photo-199392102_457239079',
          'photo-199392102_457239080', 'photo-199392102_457239086',
          'photo-199392102_457239088', 'photo-199392102_457239089',
          'photo-199392102_457239090', 'photo-199392102_457239091',
          'photo-199392102_457239092', 'photo-199392102_457239093',
          'photo-199392102_457239094', 'photo-199392102_457239095',
          'photo-199392102_457239096', 'photo-199392102_457239101',
          'photo-199392102_457239105', 'photo-199392102_457239107',
          'photo-199392102_457239108', 'photo-199392102_457239109',
          'photo-199392102_457239110', 'photo-199392102_457239111',
          'photo-199392102_457239112']
flag = 0

# Стандартная клавиатура
keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Закончить экскурсию', VkKeyboardColor.SECONDARY)
keyboard.add_button('Выход', VkKeyboardColor.NEGATIVE)

# Клавиатура главного меню
keyboard_menu = VkKeyboard(one_time=True)
keyboard_menu.add_button('Изба', VkKeyboardColor.PRIMARY)
keyboard_menu.add_line()
keyboard_menu.add_button('Животный мир', VkKeyboardColor.POSITIVE)
keyboard_menu.add_line()
keyboard_menu.add_button('Промышленное развитие города', VkKeyboardColor.PRIMARY)
keyboard_menu.add_line()
keyboard_menu.add_button('Выход', VkKeyboardColor.NEGATIVE)

while True:

    try:
        messages = vk.method("messages.getConversations",
                             {"offset":0, "count":20, "filter":"unanswered"})
        if messages["count"] >=1:
            text = messages['items'][0]['last_message']['text']
            user_id = messages['items'][0]['last_message']['from_id']

            if flag == 0:
                vk.method("messages.send", {"user_id":user_id, "message":"Привет! Я бот-экскурсовод. Предлагаю вместе прогуляться по Музею Комсомольской славы г.Людиново. Если вы находитесь в Музее, то напишите мне «привет», и мы начнём.",
                "random_id":random.randint(1, 1000)})
                flag = 1
            elif text.lower() == '*' or text.lower() == 'закончить экскурсию':
                vk.method("messages.send", {"user_id":user_id, "message":"Давайте продолжим. Выберите направление", "random_id":random.randint(1, 1000),
                "keyboard": keyboard_menu.get_keyboard()})
                flag = 4
            elif text.lower() == '-' or text.lower() == 'выход':
                vk.method("messages.send", {"user_id":user_id, "message":"Спасибо, что посетили наш музей. С нетерпением ждем вас ещё. До свидания!", "random_id":random.randint(1, 1000)})
                flag = 0
            elif text.lower() == 'привет' and flag == 1:
                vk.method("messages.send", {"user_id":user_id, "message":"Отлично, начнем! Наш музей был построен и открыт в 1970 г. И назывался музеем Комсомольской славы имени героев Людиновского подполья. В 1971 году на Людиновском тепловозостроительном заводе открылся музей боевой и трудовой славы. В декабре 2016 г. музей стал филиалом «Калужского объединенного музея-заповедника» и сейчас называется Музейно-краеведческим центром «Музей комсомольской славы». В 2020 году мы отпраздновали 50-летие Музея.", "random_id":random.randint(1, 1000)})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239040", "random_id":random.randint(1,1000)})
                flag = 2
            elif flag == 2:
                vk.method("messages.send", {"user_id":user_id, "message":"Посмотрите направо. На витрине, посвященной 50-летию Музея Комсомольской Славы представлена капсула с посланием молодёжи 2020 года, заложенная при открытии музея 8 июля 1970 года, текст послания, приветственные адреса по случаю 50-летия музея, фото Е.М. \Тяжельникова, секретаря ЦК ВЛКСМ", "random_id":random.randint(1, 1000)})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239053",
                                            "random_id":random.randint(1,1000)})
                flag = 3
            elif flag == 3:
                vk.method("messages.send", {"user_id":user_id, "message":"Давайте продолжим. Выберите направление", "random_id":random.randint(1, 1000),
                                            "keyboard": keyboard_menu.get_keyboard()})
                flag = 4
            elif flag == 4 and (text == '1' or text.lower() == 'изба'):
                vk.method("messages.send", {"user_id": user_id, "message": "Русская изба расположена на первом этаже в отдельной комнате. Как дойдете, напишите что-нибудь",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 10
            elif flag == 10:
                vk.method("messages.send", {"user_id": user_id, "message": "Русская изба всегда была ладной, добротной и самобытной. Архитектура её свидетельствует о верности многовековым традициям, их стойкости и уникальности. Её планировка, конструкция и внутреннее убранство создавались на протяжении многих лет.",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239054",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 11
            elif flag == 11:
                vk.method("messages.send", {"user_id": user_id, "message": "Перед входом в избу мы видим сени. Сени необходимы для предотвращения проникновения холода в дом. Кроме сохранения тепла сени также использовались для хранения коромысла и других нужных вещей, именно здесь многие делали чуланы для продуктов. Давайте рассмотрим нашу экспозицию поближе. В наших сенях можно увидеть ступу с песном(1) - приспособления для измельчения зерна, прялку(2) и моталку для нее(3), гребень(4), безмен(5) - рычажные весы, рубанок(6), бур(7) и пилу(8)",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239071",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 12
            elif flag == 12:
                vk.method("messages.send", {"user_id": user_id, "message": 'В правом углу комнаты расположен Красный угол. Это самый светлый и важный угол, поскольку именно его считали священным местом в доме. По традиции при строительстве ему выделяли место на восточной стороне. Здесь обязательно висели иконы и вышитые рушники.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 13
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239062",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
            elif flag == 13:
                vk.method("messages.send", {"user_id": user_id, "message": "Быт русской избы вращался вокруг печи. Она служила местом для приготовления пищи, отдыха, обогрева и даже банных процедур. Наверх вели ступени, в стенах имелись ниши для разной утвари. Топка всегда была с железными заслонами. Печь в традиционных русских избах всегда размещалась напротив красного угла. Именно её считали главным элементом дома, поскольку на печи готовили еду, спали, она обогревала весь дом.", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239056",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 14
            elif flag == 14:
                vk.method("messages.send", {"user_id": user_id, "message": 'Рядом с печью располагался Печной угол. Его также называли "бабий угол", поскольку именно здесь находилась вся кухонная утварь. Его отделяла занавеска или даже деревянная перегородка. Сюда практически никогда не заходили мужчины из своей семьи. Огромным оскорблением владельцев дома был приход чужого мужчины за занавеску в печной угол. Здесь женщины стирали и сушили вещи, готовили еду, лечили детей и гадали. Практически каждая женщина занималась рукоделием, а самым спокойным и удобным местом для этого был именно печной угол. Вышивка, шитьё, роспись - это самые популярные виды рукоделия девушек и женщин того времени.',
                "random_id":random.randint(1,1000)})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239057",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 15
            elif flag == 15:
                vk.method("messages.send", {"user_id": user_id, "message": 'Слово "костюм" от французского означает "обычай". Костюм выполняет не только практическую функцию, но и создает облик человека той эпохи. Давайте поближе его рассмотрим. В качестве головного убора девушки носили чепец(1). Традиционным одеянием девушек была юбка-понева(5), которая запахивалась вокруг талии. Она одевалась поверх рубахи(2). Дополняли образ нагрудное укражение - гайтан(3), занавеска или передник(4) и барановский платок(6).', "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id,
                "attachment": "photo-199392102_457239070", "random_id":random.randint(1,1000)})
                vk.method("messages.send", {"user_id": user_id,
                "message": 'Основой мужского костюма была рубаха. Небольшой разрез спереди стягивали на пуговицу или крепили шнуром. Рубахи носили на выпуск и обязательно подпоясывали нешироким поясом. Шили их из белой, синей, красной ткани, украшая вышивкой.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239060", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 16
            elif flag == 16:
                vk.method("messages.send", {"user_id": user_id, "message": 'Значительное место в избе занимал деревянный ткацкий стан - кросно, на нем женщины ткали. Его отдельные детали нередко украшались круглыми розетками - знаками солнца, а также скульптурными изображениями коней.', "random_id":random.randint(1,1000)})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239063",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 17
            elif flag == 17:
                vk.method("messages.send", {"user_id": user_id, "message": 'Русское подворье с его налаженным бытом и земледельчеством всегда обставлялось большим количеством предметов утвари и орудий труда.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Русский самовар',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239064",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Сундук и рубель (с помощью рубеля крестьянки разглаживали льняные увлажненные холсты, намотанные на скалку)',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239065",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Зыбка с пологом. Для новорожденного подвешивали у потолку избы нарядную люльку (зыбку, колыбельку). Мягко покачиваясь, она убаюкивала младенца. Полог (занавеска) защищал младенца от "нечистой силы"', "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239069",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Русская гармонь. Подарок музею от В.О. Хованского. Гармонь принадлежала его отцу, который погиб на фронте', "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239067",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Керосиновая лампа.', "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239068", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 3
            elif flag == 4 and (text == '2' or text.lower() == 'животный мир'):
                vk.method("messages.send", {"user_id": user_id, "message":
                "Отлично. Чтобы попасть в уголок природы нашего района, поверните направо. Как дойдете, напишите что-нибудь",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 18
            elif flag == 18:
                vk.method("messages.send", {"user_id": user_id, "message": 'Наш район расположен в юго-западной части Калужской области, на среднерусской равнине. Умеренно жаркое лето и умеренно холодная зима характерны для климата Людиновского района. Зимой нередки оттепели, а в мае-июне может грянуть заморозок. С животным миром нашего района вам поможет экспозиция "Флора и фауна Людиновского края".',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239072",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "На живописном полотне, написанном художником В.О.Хованским, изображена природа Людиновского района: водная гладь, лес, ковром расстилаются луга. Кстати, наше озеро Ломпадь, что на реке Неполоть, – самое крупное в Калужской области рукотворное водохранилище. Оно входит в список особо охраняемых природных территорий Калужской области. Кроме него, в этот список входят луг Калуганово, урочище Молевское.",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239073",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 19
            elif flag == 19:
                vk.method("messages.send", {"user_id": user_id, "message": "Богата и фауна нашего района. В лесах можно встретить различных животных. Чтобы узнать о каких животных пойдет речь, вам предстоит отгадать несколько загадок.",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Эту хитрую плутовку \nЗнают здешние леса. \nКто наводит страх на зайцев? \nЭто рыжая…", "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                flag = 20
            elif flag == 20:
                if text.lower() == 'лиса':
                    vk.method("messages.send", {"user_id": user_id, "message": "Молодец! Правильно.",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "Ты был очень близко! Это была лиса.",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Лисица - один из самых красивых хищников. Окрас шкурки рыжий, хвост длинный и пушистый, морда длинная и узкая, а глаза умные и хитрые.",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239074",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Нашли?",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Идем дальше. \nХищный маленький зверек, \nНо не норка, не хорек. \nБелочка в дупле боится, \nЧто ее найдет… ", "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                flag = 22
            elif flag == 22:
                if text.lower() == 'куница':
                    vk.method("messages.send", {"user_id": user_id, "message": "Молодец! Это правильно!",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "Это куница. Ты был близко! Не растраивайся!", "random_id":random.randint(1,1000),
                    "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Куница - зверек хищный. Гибкая, ловкая, быстрая, она хорошо лазает по деревьям, отлично бегает по земле.", "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239075",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "И так, следующая загадка. \nЗверь ушастый, летом серый, \nА зимою снежно-белый. \nЯ его не испугался, \nЦелый час на ним гонялся. Кто это?",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 23
            elif flag == 23:
                if text.lower() == 'заяц':
                    vk.method("messages.send", {"user_id": user_id, "message": "Ого! А ты мастер отгадывать загадки!", "random_id":random.randint(1,1000),
                    "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "Это заяц. Но ты был рядом.", "random_id":random.randint(1,1000),
                    "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Заяц-беляк живет в лесу - это лесной заяц. Много у зайцев врагов: и лисы, и собаки охотничьи. Но все равно зайцев много. Потому что заяц летом буро-серый, а зимой белый.",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239085",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Пришло время для следующей загадки. \nПо деревьям ловко скачет, \nИ в дупло орешки прячет. \nЧто же это за зверек? \nУгадай скорей,дружок!",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 24
            elif flag == 24:
                if text.lower() == 'белка':
                    vk.method("messages.send", {"user_id": user_id, "message": "Правильно! Ты меня поражаешь!", "random_id":random.randint(1,1000),
                    "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "К сожалению, это была белка. В следующий раз у тебя точно получится.",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Белка - удивительный  зверек. Долго можно им любоваться! Всю свою жизнь белка проводит на деревья. На землю спускается лишь для того, чтобы сорвать гриб, подобрать упавшую шишку.", "random_id":random.randint(1,1000), \
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239077", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Красивая, не правда ли?", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 25
            elif flag == 25:
                vk.method("messages.send", {"user_id": user_id, "message": "А сколько у нас птиц! Гнездятся в наших местах серые цапли, аисты и множество других пернатых, включая редкие виды. Чтобы узнать, какие птицы у нас водятся, тебе нужно отгадать следующие загадки.", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Клюв короткий, ну и что, \nЗа то вижу далеко, \nБрови красные, дугой, \nХвостик, словно веер мой! Что это за птица?", "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                flag = 26
            elif flag == 26:
                if text.lower() == 'тетерев':
                    vk.method("messages.send", {"user_id": user_id, "message": "Верно! Это тетерев.", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "Ты был близко! Это тетерев.", "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Тетерев. Близкий родственник глухаря. Тетерев - птица осторожная. Живет он в основном на деревьях. Летом и осенью тетеревов чаще всего можно увидеть на земле - тут они кормятся.", "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239078",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Идем дальше. \nКак на речку прилетает, \nСразу в воду залезает. \n«Кря» — нырнула на минутку \nВы узнали? Это …",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 27
            elif flag == 27:
                if text.lower() == 'утка':
                    vk.method("messages.send", {"user_id": user_id, "message": "Молодец! Все верно!",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "Это утка. Но не расстраивайся, в следующий раз получится!",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Кряква обыкновенная - это довольна крупная птица. Кряква прекрасно плавает, ныряет лишь будучи раненной. Под водой может проплывать десятки метров.",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239079",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": "Пришло время для следующей загадки. \nЯ по дереву стучу, \nЧервячка добыть хочу, \nХоть и скрылся под корой — \nВсё равно он будет мой! Кто это?",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 28
            elif flag == 28:
                if text.lower() == 'дятел':
                    vk.method("messages.send", {"user_id": user_id, "message": "Ты отгадал! Молодец!",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                else:
                    vk.method("messages.send", {"user_id": user_id, "message": "Это дятел! Но ты был рядом!",
                    "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Черный дятел (желна). Клюв у желны такой крепкий, что доску расщепить может. Эту птицу называют "лесным санитаром", и недаром: своим клювом птица выдалбливает жуков-короедов из ствола дерева.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239080",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Чтобы ознакомиться с остальными обитателями леса, вы можете осмотреть список, который находится правее вас. Как закончите, напишите мне.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 3
            elif flag == 4 and (text == '3' or text.lower() == 'промышленное развитие города'):
                vk.method("messages.send", {"user_id": user_id, "message": 'Чтобы познакомиться с промышленной историей г.Людиново, пройдите налево. Как дойдете, напишите что-нибудь. ',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 29
            elif flag == 29:
                vk.method("messages.send", {"user_id": user_id, "message": 'У вас, наверное, есть вопрос: "Откуда произошло название "Людиново"?". По одной из версий, название города происходит от древнерусского имени "Людин", что означает простолюдин - крестьянин-ремесленник, мастеровой человек.', "random_id":random.randint(1,1000)})
                vk.method("messages.send", {"user_id": user_id, "message": 'Первое упоминание о Людинове относится к 1626 году. В то время это была небольшая деревушка, затерявшаяся среди непроходимых брянских лесов.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239086",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 30
            elif flag == 30:
                vk.method("messages.send", {"user_id": user_id, "message": 'Помимо лесов и рек наш край богат различными полезными ископаемыми - это пески, известняки, железная руда, каменный уголь, практически все, что необходимо для выплавки железа.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239088",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239089",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Зная эти богатства нашего края, сюда ранней весной 1732 года приехал Никита Никитович Демидов – сын тульского оружейника Никиты Демидова(Антуфьева), чтобы выбрать место для строительства нового железоделательного завода, в соответствии с Указом Петра I, в котором говорилось "…Соизволяется всем и каждому дается воля какого бы чина и достоинства ни был, во всех местах, как на собственных, так и на чужих землях, искать, плавить, варить и чистить всякие металлы и минералы…"',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239090",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239091",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 31
            elif flag == 31:
                vk.method("messages.send", {"user_id": user_id, "message": 'Место было выбрано удачно. Вскоре, на реке Неполоть были построены 2 плотины и созданы верхнее (Людиновское) и нижнее (Сукремльское) водохранилища. В 1738 году на Сукремльском водохранилище был основан чугунолитейный завод, и давал он железо для достройки Людиновского завода. В 1745 году на Людиновском водохранилище был построен железоделательный завод (ныне тепловозостроительный). Первой продукцией завода были чугун, железо, предметы домашней утвари, сельскохозяйственные орудия производства.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239092",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239093",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 32
            elif flag == 32:
                vk.method("messages.send", {"user_id": user_id, "message": 'Три поколения Демидовых владели  Людиновским и Сукременским заводами. Но в 1820 г. Петр Евдокимович Демидов продает заводы Ивану Акимовичу Мальцову. Еще до покупки Людиновского и Сукремльского заводов И.А.Мальцов построил в этом районе целый ряд предприятий для выработки стекла и стеклянной посуды. В 1840-х годах принадлежащие И. А. Мальцову владения стали принимать значительные размеры.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239094",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Наиболее значительные успехи в развитии машиностроения связаны с сыном И.А.Мальцова - Сергея Ивановича Мальцова.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239095",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 33
            elif flag == 33:
                vk.method("messages.send", {"user_id": user_id, "message": 'В 1841 году на Людиновском заводе выпущены первые русские рельсы для постройки Николаевской (в настоящее время Октябрьской) железной дороги. В 1858 году на Людиновском заводе были собраны первые в России три парохода, плававшие по Волге, Десне и Днепру.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239096",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239112",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 34
            elif flag == 34:
                vk.method("messages.send", {"user_id": user_id, "message": 'Сергей Иванович создает огромный промышленный округ. Мальцовский промышленный округ называли "империя в империи", он практически никому не подчинялся. В этой "империи" выпускали даже свои собственные деньги, ходившие как разменная монета.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Разнообразной была и продукция, выпускавшаяся на заводах Мальцова: это патентованные печи для обогрева больших помещений и цехов, оборудование для первых в России водопроводов, печи для ванных комнат, предметы домашней утвари: чугунная посуда, утюги и т.п. ',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": 'photo-199392102_457239101',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": 'photo-199392102_457239105',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 35
            elif flag == 35:
                vk.method("messages.send", {"user_id": user_id, "message": '26 сентября 1856 года Людиново посетил Великий князь Михаил Николаевич для производства лафетов и ядер во время Крымской войны.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": 'photo-199392102_457239107',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 36
            elif flag == 36:
                vk.method("messages.send", {"user_id": user_id, "message": 'В 1867 г. Министерство путей сообщения обратилось к заводчикам – создать свое отечественное паровозо- и вагоностроение. Для организации и серийного производства требовалась более совершенная техника и специалисты с более обширными специальными знаниями и навыками. Из Англии Мальцов привозит оборудование и приглашает французских специалистов по постройке паровозов и по постройке вагонов англичанина Смитта. В двух верстах от Брянска начинает строить Радицкий паровозо- вагонный завод.',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": 'photo-199392102_457239108',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "message": 'Первые узкоколейные паровозы были изготовлены Людиновским заводом в 1870 г. В период с 1871 −1877 гг. было выпущено 49 паровозов, которые превзошли достоинством паровозы французских, австрийских и ряда других заводов и на Московской политехнической выставке получили большую золотую медаль и аттестат первой степени.', "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": "photo-199392102_457239109",
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 37
            elif flag == 37:
                vk.method("messages.send", {"user_id": user_id, "message": 'К концу ХIХ века Людиново это уже большое заводское село. В центре села возвышался, обустроенный стараниями Сергея Ивановича Мальцова, величественный Казанский собор, который называли "восьмое чудо света", большая базарная площадь, на которой стоял памятник царю Александру II. Он был открыт в 1903 г. на собранные народные деньги. В 1918 г. памятник снесли, и на его месте был установлен памятник И.И.Фокину. В годы Великой Отечественной войны памятник взорвали. В 1950 г. был установлен новый памятник И.Фокину чуть ближе к заводу.', "random_id":random.randint(1,1000),
                "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": 'photo-199392102_457239110',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                vk.method("messages.send", {"user_id": user_id, "attachment": 'photo-199392102_457239111',
                "random_id":random.randint(1,1000), "keyboard": keyboard.get_keyboard()})
                flag = 3

                #uploader = vk_api.upload.VkUpload(vk)
                #img = uploader.photo_messages("muzey.jpg")
                #media_id = str(img[0]['id'])
                #owner_id = str(img[0]['owner_id'])
                #print("photo" + owner_id + "_" + media_id)
            else:
                vk.method("messages.send", {"user_id": user_id, "message": "Извините, я Вас не понимаю. Попробуйте еще раз.", "random_id":random.randint(1,1000),
                "keyboard": keyboard_menu.get_keyboard()})
    except Exception:
        time.sleep(1)
