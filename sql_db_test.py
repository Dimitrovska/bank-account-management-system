import mysql.connector

# Опит за връзка към MySQL сървъра
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # парола
        database="bank_db"  # име на базадата данни в mysql
    )

    if connection.is_connected():
        print("✅ Успешно се свърза с базата данни!")
        db_Info = connection.get_server_info()
        print("MySQL Server version:", db_Info)

except mysql.connector.Error as err:
    print("❌ Грешка при свързване:", err)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔌 Връзката е затворена.")
