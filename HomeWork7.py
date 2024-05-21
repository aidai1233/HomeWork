import sqlite3
student = sqlite3.connect('student.db')
cursor = student.cursor()
#
# cursor.execute('''DROP TABLE IF EXISTS студенты''')

cursor.execute('''CREATE TABLE IF NOT EXISTS студенты(
имя TEXT,
фамилия TEXT,
год  DATE,
хобби TEXT,
баллы INTEGER
)''')

cursor.execute('''
INSERT INTO студенты (имя, фамилия, год, хобби, баллы)
VALUES
('Айдай','Саматова',2004,'кулинария',12),
('Айтунук','Нурланбекова',2004,'рисовать',13),
('Бекзат', 'Касымов', 2003, 'футбол', 10),
('Гульжан', 'Айтбаева', 2005, 'чтение', 6),
('Даурен', 'Темирбеков', 2002, 'шахматы', 10),
('Ерболат', 'Сулейманов', 2004, 'музыка', 7),
('Жанар', 'Койшыбаева', 2001, 'рисование', 9),
('Камиль', 'Ержанов', 2003, 'программирование', 9),
('Лаура', 'Ирбулатова', 2004, 'танцы', 11),
('Мадина', 'Турсунова', 2005, 'плавание', 5)
''')
student.commit()

cursor.execute('''SELECT * FROM студенты WHERE LENGTH(фамилия) > 10''')
long_surname_students = cursor.fetchall()
print("Студенты с фамилией больше 10 символов: ")
for student in long_surname_students:
    print(student)


cursor.execute('''
UPDATE студенты SET имя="genius" WHERE баллы > 10''')



cursor.execute('''
SELECT * FROM студенты WHERE имя = 'genius'
''')
genius_students = cursor.fetchall()
print("\nСтуденты с именем 'genius':")
for student in genius_students:
    print(student)
cursor.execute('''
DELETE FROM студенты WHERE rowid % 2 = 0
''')

cursor.close()

