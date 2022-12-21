import psycopg2
from config import Style

# def connect():
try:
    conn = psycopg2.connect("dbname='gxpUsers' user='postgres' password='' host='localhost'")
    cursor = conn.cursor();
    print(Style.GREEN + 'Успешно подключен к базе данных!\n')

except:
    print(Style.RED + 'Не могу подключиться к базе данных!')

try:
    user = int(input(Style.MAGENTA + 'Введите ID удаляемого пользователя: '))
    sql = f" DELETE FROM users WHERE user_id = {user} "
    cursor.execute(sql)
    conn.commit();
    conn.close();
    print(Style.RED + f'\nУдален пользователь под ID: {user}')
except:
    print(Style.RED + 'Пользователь не найден')
