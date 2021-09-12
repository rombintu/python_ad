# Python AD

## Description. Concept
Сущности: 
* Клиенты
* Группы
* Хосты
* Политики
* Хранилище*

Описание:
• Политики. Набор правил, регулирующий права доступа к хосту или группе хостов
• Хосты имеют метку уровня доступа, необходимого для использования

Функции: 
* Создание гибких политик
* Создание клиентов и групп
* Сбор логов с хостов*


## Requirements
```
sudo apt-get install python-django python3
pip3 install django
```

## Install and run
```
git clone https://github.com/rombintu/python_ad.git
cd python_ad
python3 manage.py migrate
python3 manage.py runserver
Go to http://127.0.0.1:8000/
```

