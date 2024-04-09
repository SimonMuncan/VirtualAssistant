import sqlite3


class updateSQL():
    def sqlInsertDelete(sqlQuery):
        try:
            # Establish connection to the SQLite database
            con = sqlite3.connect("database.db")
            # Create a cursor object to execute SQL queries
            cur = con.cursor()
            # Execute the SQL query for insert or delete operation
            cur.execute(sqlQuery)
            # Commit the transaction to save changes
            con.commit()
        except sqlite3.Error as error:
            # Handle any errors that occur during SQL execution
            print("Failed to execute the above query", error)


