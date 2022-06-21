import sqlite3

connection = sqlite3.connect("to-do-list.db")

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE task(task text)""")
    except:
        pass

def show_tasks(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT rowid, task FROM task""")
    result = cursor.fetchall()

    for row in result:
        print(str(row[0]) + " - " + row[1])


def add_task(connection):
    print("Adding task.")
    task = input("Enter task name: ")
    if task == "0":
        print("Return to menu.")
    else:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        connection.commit()
        print("Task has been added!=.")

def delete_task(connection):
    task_index = int(input("Enter task's number to delete: "))

    cursor = connection.cursor()
    rows_deleted = cursor.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
    connection.commit()

    if rows_deleted == 0:
        print("This task doesn't exists!")
    else:
        print("Task has been removed.")

create_table(connection)

while True:
    print()
    print("[1] - [Show] task list")
    print("[2] - [Add] task to list")
    print("[3] - [Delete] task from list")
    print("[4] - [Exit]")

    user_choice = int(input("Choose an option: "))
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

connection.close()