import pymysql
import datetime

connection = pymysql.connect(host="localhost", user="root", password="root", database="poll_app")
cursor = connection.cursor()
user_login = None


def main_menu():
    if user_login is None:
        print("Вы еще не авторизованы, для прохождения опроса необходимо авторизоваться или зарегистрироваться")
        print("Нажмите 1 для регистрации\nНажмите 2 для авторизации")
    print("""Нажмите 3 для просмотра доступных опросов
        Нажмите 4 для прохождения опроса""")
    result = input()
    try:
        if (int(result) == 1 or int(result) == 2) and user_login is not None:
            print("Вы уже авторизованы")
        elif int(result) == 1:
            register_user()
        elif int(result) == 2:
            login_user()
        elif int(result) == 3:
            poll_list()
        else:
            select_poll()
    except ValueError:
        print("Введите число")
        main_menu()
    except Exception as e:
        print(e)
        print("Неизвестная ошибка")


def register_user():
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    login = input("Введите логин: ")

    if (len(login) < 4):
        print("Логин должен состоять минимум из 4 символов")
        main_menu()
    elif age.isdigit() is False:
        print("Возраст должен быть целочисленным")
        main_menu()

    cursor.execute("SELECT id FROM Users WHERE login = %s ", (login,))
    result = cursor.fetchone()
    if result:
        print("Пользователь с таким именем уже существует")
        main_menu()

    cursor.execute("INSERT INTO Users (user_name, age, login) VALUES (%s, %s, %s)", (name, age, login,))
    connection.commit()
    print("Вы зарегались!")
    main_menu()


def login_user():
    login = input("Введите логин ")
    cursor.execute("SELECT id FROM Users WHERE login = %s", (login,))
    result = cursor.fetchone()
    if not result:
        print("Пользователь с таким логином не найден")
        main_menu()
    else:
        global user_login
        user_login = result[0]
        print("Вы успешно авторизовались")
        main_menu()


def poll_list():
    cursor.execute("SELECT id, title from Polls")
    polls = cursor.fetchall()
    user_polls = []
    if user_login is not None:
        cursor.execute(f"SELECT poll_id FROM Results WHERE user_id = {user_login}")
        user_polls = [int(x[0]) for x in cursor.fetchall()]
    else:
        print("Авторизируйтесь")
        main_menu()
    if len(polls) == 0:
        print("Нет доступных опросов")
    for poll in polls:
        if poll[0] in user_polls:
            print(poll[1] + " - Пройден")
        else:
            print(poll[1])
    main_menu()


def select_poll():
    if user_login is None:
        print("Авторизируйтесь")
        main_menu()
    else:
        cursor.execute(
            f"SELECT id, title FROM Polls WHERE id not in (SELECT poll_id FROM Results WHERE user_id={user_login})")
        available_polls = cursor.fetchall()
        if len(available_polls) == 0:
            print("Нет доступных опросов")
            main_menu()
        else:
            print("Введите номер опроса")
            for poll in available_polls:
                print(poll[0], "-", poll[1])
            poll_id = input()
            if int(poll_id) in [x[0] for x in available_polls]:
                ask_quest(int(poll_id))
            else:
                print("Данного опроса не существует")
                main_menu()


def ask_quest(poll_id: int):
    cursor.execute(f"SELECT questions FROM Polls WHERE id = {poll_id} ")
    result = cursor.fetchone()[0]
    quests = result.split(";")
    answers = []
    for quest in quests:
        answer = input(quest.strip() + "\n")
        answers.append(answer)
    print("Ваши ответы:")
    for quest, answer in zip(quests, answers):
        print(quest + ":" + answer)
    print("Отправить резы? да/нет")
    send_answer = input()
    if send_answer == "да":
        cursor.execute("INSERT INTO Results (answers, answer_date, poll_id, user_id) VALUES(%s, %s, %s, %s)",
                       (";".join(answers), datetime.datetime.today().date(), poll_id, user_login))
        connection.commit()
        print("Успех")
    else:
        print("вы отменили")
    main_menu()


if __name__ == "__main__":
    print("Привет!\nЭто приложение для заполнения опросов")
    main_menu()
