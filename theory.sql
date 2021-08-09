INSERT - добавление данных в таблицу;
SELECT - выборка данных из таблиц, в том числе при создании сводной выборки из нескольких таблиц;

Пример:
INSERT INTO <table_name>(<colum1>,<column2>,...) VALUES (<value1>, <value2>,...)
или
INSERT INTO <table_name> VALUES (<value1>, <value2>,...)

SELECT colum1, column2, ... FROM <table_name> WHERE <условие>

Дрцгие усовные операторы:
= , == , > , < , >= , <= , != , BETWEEN

AND, OR, NOT, IN, NOT IN

SELECT * FROM users
WHERE old IN(19,32) AND score <= 1000 OR sex = 1
ORDER BY old DESC (ASC) # по убыванию (возрастанию)
LIMIT <max> [OFFSET offset] # количество строк на вывод, offset - смещение
или
LIMIT <offset, max> # количество строк на вывод, offset - смещение


UPDATE - изменение данных в записях

DELETE - удаление записей из таблицы

UPDATE имя_таблицы SET имя_столбца = новое_значение WHERE условние

Например: 
UPDATE users SET score = 1000 WHERE rowid=1 

UPDATE users SET score = score+500  WHERE sex=2 

UPDATE users SET score = 1500  WHERE name LIKE 'Федор'

% - любое продолжение строки;
_ - любой символ;

UPDATE users SET score = score+100 WHERE name LIKE 'M%'


DELETE FROM имя_таблицы WHERE условие 

Например:
DELETE FROM users WHERE rowid IN (2,5) 

Агрегирование и группировка записей

SELECT count(имя_столбца) as count   FROM games WHERE user_id = 1

count()
sum()
avr()
min()
max()

Поиск уникальный значений:
SELECT count(DISTINCT user_id) as count from games

GROUP BY < имя_поля >

Например:
SELECT user_id, sum(score) as sum
from games
where score > 300
group by user_id
order by sum desc

JOIN - формирование сводных отчетов

JOIN < таблица > ON < условие связывания >

SELECT name, sex, games.score FROM games

JOIN users ON games.user_id = users.rowid # соединяет две таблицы по ключу

аналогично:
SELECT name, sex, games.score FROM users, games
сшивает две таблицыб выводит много лишних данных

LEFT JOIN

SELECT < поля > FROM < таблицы >
JOIN < таблица1 > JOIN < таблица2 > ... JOIN < таблица3 >
ON < условие связывания >


UNION - объединение таблиц

SELECT score, `from` FROM tab1
UNION SELECT val, type FROM tab2











 


