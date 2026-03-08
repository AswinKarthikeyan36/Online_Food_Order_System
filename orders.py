from database import cursor, conn

def place_order():
    user_id = int(input("Enter user id: "))
    food_id = int(input("Enter food id: "))
    quantity = int(input("Enter quantity: "))

    cursor.execute(
        "INSERT INTO orders(user_id,food_id,quantity,order_date) VALUES(%s,%s,%s,CURDATE())",
        (user_id, food_id, quantity)
    )

    conn.commit()
    print("Order placed successfully")