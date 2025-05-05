print('Hello again, World!')


DATABASE = 'cars.db'
#hello

def print_all_car():
    speed = input('What speed: ')
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('cars.db')
        cursor = db.cursor()
        sql = "SELECT car_name,top_speed FROM car WHERE top_speed > ?;"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall()
        #Print them nicely

        for car in results:
            print(f"Car: {car[0]} Top Speed : {car[1]}")



if __name__== '__main__':
    print_all_car()