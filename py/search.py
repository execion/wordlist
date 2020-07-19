from database import *

try:
    table = input("\nTable: ")
    while True:
        with connection.cursor() as cursor:
            print("\nTable: {}".format(table.capitalize()))
            word = input("Word: ")
            if word == "-quit":
                break
            sql = "SELECT word, meaning FROM {} WHERE word=\"{}\";".format(table, word)
            cursor.execute(sql)
            response = cursor.fetchall()
            if len(response) > 0:
                result = response[0]["meaning"].split(", ")
                print(result)
            else:
                print("Not found")
finally:
    connection.close()