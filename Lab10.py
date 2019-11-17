import sqlite3, base64, webbrowser
userInput = 0
#Initializing the database
connect = sqlite3.connect('week10.db')
connect.row_factory = lambda cursor, row: row[0]
cursor = connect.cursor()

#If the user inputs an invalid number, the program asks for input again
while userInput < 1 or userInput > 24:
    userInput = input("Please make a selection between 1 and 24! ")
    #Exiting the program if the user inputs q
    if userInput == "q":
        exit()
    userInput = int(userInput)
    #Opens the web browser to the google maps address selected
    if userInput >= 1 and userInput <= 24:
        userTuple = (userInput, )
        cursor.execute('SELECT link FROM Lab10 WHERE id=?', userTuple)
        webbrowser.open(base64.b64decode(cursor.fetchone()))
        #Asks the user for the name of the city and country, then commits it to the database
        cityName = input("What's the name of the city selected? ")
        countryName = input("Which country is the city in? ")
        insertedData = (cityName, countryName, userInput)
        cursor.execute('UPDATE Lab10 SET (City,Country) = (?,?) WHERE id=?', insertedData)
        connect.commit()
        connect.close()