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
        print(f"   Name                         Top_speed      Manufactor       Horse_power")

        for car in results:
            print(f"{car[2]:34} {car[1]:<15} {car[3]:<20} {car[4]}")
            #print(f"Name: {car[2]} Top speed : {car[1]} Manufactor : {car[3]}")
        

def print_top_speed():
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('CARS_FINAL.db')
        cursor = db.cursor()
        sql = "SELECT top_speed,name FROM CARS ORDER BY top_speed DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely
        print(f"Top_speed        Name")

        for car in results:
            print(f"{car[0]:<10} {car[1]:}")
            #print(f"name: {car[2]} top speed : {car[1]} manufactor : {car[3]}")
        

def print_manufacturers():
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('CARS_FINAL.db')
        cursor = db.cursor()
        sql = "SELECT manufactor FROM CARS;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely
        print(f"Manufactor")

        for car in results:
            print(f"{car[0]:}")
            #print(f"name: {car[2]} top speed : {car[1]} manufactor : {car[3]}")
        

def print_horse_power():
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('CARS_FINAL.db')
        cursor = db.cursor()
        sql = "SELECT horse_power,name FROM CARS ORDER BY top_speed DESC;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely
        print(f"Horse_power        Name")

        for car in results:
            print(f"{car[0]:<12} {car[1]:}")
            #print(f"name: {car[2]} top speed : {car[1]} manufactor : {car[3]}")

# def print_get_car():
#      with sqlite3.connect(DATABASE) as db:
#         cursor = db.cursor()
#         sql = "SELECT * FROM manufactor WHERE name = 'Ferrari';"
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         #Print them nicely
#         for car in results:
#             print(f"{car[0]:<12} {car[1]:}")
#             #print(f"name: {car[2]} top speed : {car[1]} manufactor : {car[3]}")

Ferrari = sql = "SELECT * FROM manufactor WHERE name = 'Ferrari';"

while True:
    user_input = input("\nWhat car would you like to see?. \n1. Ferrari\n2. Bugatti\n3. Koenigsegg\n4. Porsche\n5. Nissan\n6. Rust-eze\n7. exit\n")
    if user_input == "1":
        print(Ferrari)
    elif user_input == "2":
        print_top_speed()
    elif user_input == "3":
        print_manufacturers()
    elif user_input == "4":
        print_horse_power()
    elif user_input == "7":
        print('Goodbye')
        break
    else:
        print("Thats not an option\n")


        



# while True:
#     user_input = input("\nWhat would like to do.\n1. Print all cars\n2. Print top_speed\n3. Print all manufacturers\n4. Print horse_power\n7. exit\n")
#     if user_input == "1":
#         print_all_car()
#     elif user_input == "2":
#         print_top_speed()
#     elif user_input == "3":
#         print_manufacturers()
#     elif user_input == "4":
#         print_horse_power()
#     elif user_input == "7":
#         print('Goodbye')
#         break
#     else:
#         print("Thats not an option\n")

print_get_car()
