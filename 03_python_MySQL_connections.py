import mysql.connector

# ========================================================================================

# Connect to MySQL

conn = mysql.connector.connect(
    host="localhost",       # usually localhost
    user="root",            # MySQL username
    password="Dota2DayNightHuntr@2026",  # MySQL password
    database="library_db"      # database name
)

cursor = conn.cursor()
print("Connected to Database!")

# ========================================================================================

# Show all members

cursor.execute("""
SELECT *
FROM members
""")

# cursor.execute("""
# SELECT *
# FROM borrow
# """)

members = cursor.fetchall()
for m in members:
    print(m)

# ========================================================================================

# # Add a new member

# new_member = ("Harry Maharjan", "harry@example.com")

# cursor.execute("""
# INSERT INTO members (name, email) 
# VALUES (%s, %s)
# """, (new_member))

# conn.commit()
# print("New member added!")

# ========================================================================================

# # Update a member’s email

# cursor.execute("""
# UPDATE members
# SET email = 'jekenmaharjan@gmail.com'
# WHERE id = 1
# """)

# conn.commit()
# print("Member email updated!")

# ========================================================================================

# # Delete a member safely

# member_id = 3

# # First delete borrow records
# cursor.execute("""
# DELETE
# FROM borrow
# WHERE member_id = %s
# """, (member_id,))

# # Then delete the member
# cursor.execute("""
# DELETE
# FROM members
# WHERE id = %s
# """, (member_id,))

# conn.commit()
# print(f"Member {member_id} and their borrow records deleted safely!")

# ========================================================================================

# # Fetch overdue books

# cursor.execute("""
# SELECT id, book_id, member_id, borrow_date
# FROM borrow
# WHERE return_date IS NULL
# AND borrow_date < CURDATE() - INTERVAL 7 DAY
# """)

# overdue_books = cursor.fetchall()

# for b in overdue_books:
#     print(b)

# ========================================================================================

# Close the connection

cursor.close()
conn.close()
print("Connection closed.")

