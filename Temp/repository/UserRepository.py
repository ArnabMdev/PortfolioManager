from model.UserModel import User
from database_connector import get_db_connection
from mysql.connector import Error


class HoldingsRepository:
    
    @staticmethod
    def getAllUsers():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM USERS')
            result = cursor.fetchall()
            holdings = [User(*item).to_dict() for item in result]
            cursor.close()
            conn.close()
            return holdings
            
        except Error as error:
            print(error)
            cursor.close()
            conn.close()
            return -1
        
    @staticmethod
    def getUser(user_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM HOLDINGS WHERE asset_id = %s',(user_id,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            if(result):
                holding = User(*result).to_dict()
                return holding
            else:
                return -1
                
        except Error as error:
            print(error)
            cursor.close()
            conn.close()
            return -1
    
    @staticmethod
    def addUser(user:User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            insertstmnt = 'INSERT INTO USERS VALUES (%s,%s,%s)'
            data = (user.user_id, user.user_name, user.password)
            cursor.execute(insertstmnt,data)
            conn.commit()
            affected_rows = cursor.rowcount
            print(affected_rows)
            cursor.close()
            conn.close()
            return affected_rows
        except Error as error:
            print(error)
            cursor.close()
            conn.close()
            return -1
    
    @staticmethod
    def updateUser(user:User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            updatestmnt = 'UPDATE USERS SET user_name = %s, password = %s, WHERE user_id = %s'
            data = (user.user_name, user.password, user.user_id)
            cursor.execute(updatestmnt, data)
            conn.commit()
            affected_rows = cursor.rowcount
            print(affected_rows)
            cursor.close()
            conn.close()
            return affected_rows
        except Error as error:
            print(error)
            cursor.close()
            conn.close()
            return -1

    @staticmethod
    def deleteUser(user_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM USERS WHERE user_id = %s',(user_id,))
            affected_rows = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return affected_rows
        except Error as error:
            print(error)
            cursor.close()
            conn.close()
            return -1