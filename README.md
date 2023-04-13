На сайте ФСТР ведёт базу горных перевалов, которая пополняется туристами
https://pereval.online/

Будет использоваться Agile-подход

Этап1. Необходимо создать БД Postgres, разработать класс по работе с БД и один метод для REST API.
Этап2. Разработать еще три метода для Rest API (задеплоить своё решение на сервере - не обязательно)
Этап3. Подготовить документацию. Покрыть код тестами (не обязательно)
####Этап 1

Создание базы данных.
Создание класса по работе с данными, с помощью которого добавлены новые значения в таблицу перевалов.
Написание REST API, который вызывает метод из класса по работе с данными.
Результат метода: JSON
status — код HTTP, целое число: 500 — ошибка при выполнении операции; 400 — Bad Request (при нехватке полей); 200 — успех.
message — строка: Причина ошибки (если она была); Отправлено успешно; Если отправка успешна, дополнительно возвращается id вставленной записи.
id — идентификатор, который был присвоен объекту при добавлении в базу данных.
127.0.0.1/перевал

####Этап 2

Добавлено в REST API ещё три метода

GET /submitData/ — получить одну запись (перевал) по её id
PATCH /submitData/ — отредактировать существующую запись (замена), если она в статусе new. Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. Метод принимает тот же самый json, который принимал уже реализованный тобой метод submitData. Возвращаются 2 значения: status и message
GET /submitData/?user__email= — список данных обо всех объектах, которые пользователь с почтой отправил на сервер.
####Этап 3

Добавлена в Readme.md документацию к REST API
Документация с помощью Swagger
Покрыть код тестами
