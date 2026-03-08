from database import cursor, conn

def view_menu():
    cursor.execute("SELECT * FROM food_items")
    items = cursor.fetchall()

    for item in items:
        print(item)