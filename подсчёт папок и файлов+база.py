import os
import sqlite3
print("Скрипт считает папки и графические файлы")
print("----------------------------------------")
d=input("Введите каталог: ")
dd=0
ff=0

with sqlite3.connect('database.db') as db:
	cursor = db.cursor()
	query = ''' CREATE TABLE IF NOT EXISTS table1 (name TEXT) '''
	cursor.execute(query)

print(os.walk(d))

for dirpath, dirnames, filenames in os.walk(d):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
        dd+=1
    # перебрать файлы
    for filename in filenames:
    	if "jpg" in filename or "png" in filename or "jpeg" in filename or "JPG" in filename:
	        print("Файл:", os.path.join(dirpath, filename), ff)
	        cursor.execute("INSERT INTO table1 VALUES(?);", [os.path.join(dirpath, filename)])
	        ff+=1
db.commit()
print("папок: ",dd)
print("файлов: ",ff)

input()