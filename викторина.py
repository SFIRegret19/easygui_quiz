from easygui import *

score = 0

possible = ['А. Джон Кеннеди','Б. Франклин Рузвельт','В. Рональд Рейган']
q1 = buttonbox('Кто из президентов США написал свой собственный рассказ про Шерлока Холмса?',choices=possible)
if q1 == possible[1]:
    score += 20
else:
    score -= 10
possible = ['А. Налог на тунеядство','Б. Налог на трусость','В. Налог на отсутствие сапог']
q2 = buttonbox('Какую пошлину ввели в XII  веке в Англии для того чтобы заставить мужчин пойти на войну?',choices=possible)
if q2 == possible[1]:
    score += 20
else:
    score -= 10
possible = ['А. От подателей за провоз парфюмерии','Б. От сборов за нестиранные носки','В. От налога на туалеты']
q3 = buttonbox('Откуда пошло выражение «деньги не пахнут?',choices=possible)
if q3 == possible[2]:
    score += 20
else:
    score -= 10 
possible = ['А. На плавки','Б. На пальмы','В. На солнце']
q4 = buttonbox('Туристы, приезжающие на Майорку, обязаны заплатить налог…',choices=possible)
if q4 == possible[2]:
    score += 20
else:
    score -= 10
possible = ['А. «Простоквашино»','Б. «Винни-Пух»','В. «Старик и море»','Г. «Ну, погоди!»']
q5 = buttonbox('Российский мультфильм, удостоенный «Оскара», — это…',choices=possible)
if q5 == possible[2]:
    score += 20
else:
    score -= 10
msgbox('''
Ты прошёл тест!
Твоё количество очков:
''' + str(score))
if score <= 50 and score > 0:
    msgbox('Твоя интуиция тебя подводит')
elif score > 50:
    msgbox('Сегодня твой день!!!')
else:
    msgbox('...ОК...')
    msgbox('Доп ворос ))')
    possible = ['!Да!','Д!а','Да!','!Да']
    q6 = buttonbox('Нравится прогать',choices=possible)
    if q6 == possible[1] or q6 == possible[0] or q6 == possible[3] or q6 == possible[4]:
        score += 10000
        msgbox('''
            Ты ответил на доп вопрос!
            Твоё количество очков:
            ''' + str(score) + '''
            МЕГА ХАРОШШШ
            ''')