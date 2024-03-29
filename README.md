#### _Проект был создан Олегом Сунгуровским <safasgasc.asfg@gmail.com>_

# Задание

Задачу, которую должен решать бот:

1. В боте должно быть меню из 3 кнопок: «Получить информацию по товару», «Остановить уведомления», «получить информацию
   из БД».
2. Нажимая на кнопку «Получить информацию по товару» Пользователь отправляет в бота артикул товара с Wildsberries (
   например: 211695539).
3. Бот должен выдать информацию о товаре (карточке) - Название, артикул, цена, рейтинг товара, количество товара НА ВСЕХ
   СКЛАДАХ.
   Все эти данные легко получаются по
   запросу: https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={артикул товара}
4. Под сообщением, которые присылает бот должна быть inline-кнопка - «подписаться». По нажатию на которую должны
   приходить уведомления в бот каждые 5 минут с сообщением, что было выше. (Название, артикул, цена, рейтинг товара,
   количество товара НА ВСЕХ СКЛАДАХ)
5. При нажатии на кнопку «Остановить уведомления» - уведомления останавливаются.
6. При нажатии на кнопку «получить информацию из БД» бот должен прислать сообщение с последними 5 записями из БД.

Бот должен быть написан на Python 3.9+, с использованием библиотек: Aiogram 3. Реализуйте взаимодействие с базой данных
для сохранения истории запросов (используйте SQLAlchemy и PostgreSQL). Должны сохраняться id пользователя, время
запроса, артикул товара. Бота упаковать в docker. Запустить на своем сервере. Прислать ссылку на бота. Прислать ссылку
на репозиторий с кодом.

## Запуск приложения через Docker

1. Клонировать репозиторий с помощью git:
   ```bash
     git clone git@github.com:oleg-sung/TgWbBot.git
   ```
   Далее перейдите в папку проекта:
   ```bash
    cd TgWbBot
    ```   
2. Создать файл **.env** в папке корневой папке со следующими полями:
   ```
   # Bot Settings

   TOKEN=<секретный ключ для Телеграм бота>
   
   Database settings
   POSTGRES_DB=<название базы данных>
   POSTGRES_USER=<пользователь базы данных>
   POSTGRES_PASSWORD=<пороль для пользователя>
   POSTGRES_PORT=<порт базы данных (5432)>
   POSTGRES_HOST=<хост базы данных (postgres)>

   ```   
3. Сборка и запуск контейнера:
    ```bash
    docker-compose build
    ```
    ```bash
    docker-compose up 
    ```
4. Бод будет доступен в телеграмме