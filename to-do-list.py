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
        print(str(row[0]) + " " + str(row[1]))

def add_task(connection):
    print("Adding task")
    task = input("Enter task name: ")
    if task == "0":
        print("Return to menu")
    else:
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO task (task) VALUES (?)""", (task,))
        connection.commit()
        print("Task has been added!")

create_table(connection)

while True:
    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Quit program")

    user_choice = int(input("Choose option: "))
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)
        
    if user_choice == 4:
        break

connection.close()    