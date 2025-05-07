import sqlite3

DATABASE = 'CARS_FINAL.db'
#hello

def print_all_car():
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('CARS_FINAL.db')
        cursor = db.cursor()
        sql = "SELECT * FROM CARS;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely
        print(f"name                            top_speed     manufactor")

        for car in results:
            print(f"{car[2]:34} {car[1]:<15} {car[3]}")
            #print(f"name: {car[2]} top speed : {car[1]} manufactor : {car[3]}")
        db.close

def print_top_speed():
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('CARS_FINAL.db')
        cursor = db.cursor()
        sql = "SELECT top_speed,name FROM CARS ORDER BY top_speed DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely
        print(f"top_speed")

        for car in results:
            print(f"{car[0]:}")
            #print(f"name: {car[2]} top speed : {car[1]} manufactor : {car[3]}")
        db.close


while True:
    user_input = input("\nWhat would like to do.\n1. Print all cars\n2. Print top_speed\n7. exit\n")
    if user_input == "1":
        print_all_car()
    elif user_input == "2":
        print_top_speed()
    elif user_input == "3":
        pass
    elif user_input == "7":
        break
    else:
        print("Thats not an option\n")
