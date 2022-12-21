import psycopg2
from config import Style

conn = psycopg2.connect("dbname='gxpUsers' user='postgres' password='' host='localhost'")
cursor = conn.cursor()

cursor.execute('''
SELECT * FROM users

''')

users = (cursor.fetchall())
for user in users:
    userID = user[0]
    userlastName = user[1]
    userFirstName = user[2]
    patranymic = user[3]
    year_of_birth = user[4]
    department = user[5]
    job_title = user[6]

    print(Style.GREEN + f'''User ID: {userID}
Фамилия: {userlastName}
Имя: {userFirstName}
Отчество: {patranymic}
Год рождения: {year_of_birth}
Отдел: {department}
Должность: {job_title}
''')
    print('-' * 30)
