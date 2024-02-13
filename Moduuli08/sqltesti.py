import mysql.connector


def airport (name):
    sql = f"SELECT location from game where screen_name='{name}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}")
    return



connection = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit= True
)
name = input("Enter your name: ")
airport(name)