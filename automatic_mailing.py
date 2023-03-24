import smtplib
import os
from dotenv import load_dotenv


site_link = 'https://dvmn.org/referrals/vv9B9AG73k2SuDbGrhsmNWOKHJwx7wiqKDO1NvOx/'
friend_name = 'Ivan'
my_name = 'Gazinyr'
recipient_email_address = 'Gazinyr19@yandex.ru'
load_dotenv()
sender_email_address = os.environ['SENDER_EMAIL_ADDRESS']
password = os.environ['PASSWORD']
letter = f'''From: {sender_email_address}
To: {recipient_email_address}
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8";'''
email_text = f'''{letter}

Привет, %friend_name%! %my_name% приглашает \
тебя на сайт %website%!

%website% — это новая версия онлайн-курса по 
программированию. 
Изучаем Python и не только. Решаем задачи. 
Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в 
программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся \
в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно \
разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и \
получить уведомление о релизе сразу на имейл.'''
email_text = email_text.replace('%website%', site_link)
email_text = email_text.replace('%friend_name%', friend_name)
email_text = email_text.replace('%my_name%', my_name)
email_text = email_text.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(sender_email_address, password)
server.sendmail(sender_email_address, recipient_email_address, email_text)
server.quit()
