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



if __name__== '__main__':
    print_all_car()