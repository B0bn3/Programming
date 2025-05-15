import sqlite3

DATABASE = 'CARS_FINAL.db'

def print_all_car():
    #This function prints all data 
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('CARS_FINAL.db')
        cursor = db.cursor()
        sql = "SELECT * FROM CARS;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely
        print(f"   Name                         Top_speed      Manufactor       Horse_power")

        for car in results:
            print(f"{car[2]:34} {car[1]:<15} {car[3]:<15} {car[4]}")
            #print(f"Name: {car[2]} Top speed : {car[1]} Manufactor : {car[3]}")
        

def print_top_speed():
    #This function prints the top speed of ever car
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
    #This function prints the manufactor of every car
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
    #This function prints the horse power of every car
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

def print_get_car(car):
     #This function allows the user to choose a speific manfacuturer
     with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM manufactor WHERE name = ?;", (car,))
        results = cursor.fetchall()
        if results:
            print(f"\nResults for {ask}:")
            print(f"Name      Manufactor")
            for car in results:
                print(f"{car[2]:<12} {car[1]:}")
        else:
            print(f"Sorry, {ask} is not an option in the database.")


while True:
    user_input = input("\nWhat would you like to do..\n1. See a speific manufacturer\n2. Print top_speed\n3. Print all manufacturers\n4. Print horse_power\n5. Print all cars\n7. exit\n")
    if user_input == "1":
        ask = input('What car would you like to see? ')
        print_get_car(ask)
    elif user_input == "2":
        print_top_speed()
    elif user_input == "3":
        print_manufacturers()
    elif user_input == "4":
        print_horse_power()
    elif user_input == "5":
        print_all_car()
    elif user_input == "7":
        print('Goodbye')
        break
    else:
        print("Thats not an option\n")