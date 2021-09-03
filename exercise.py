import mysql.connector

# set up the sql connection
con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word you want a definition for : ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
result = cursor.fetchall()

if result:
    for res in result:
        print(res[1])
else:
    print("No word found.")