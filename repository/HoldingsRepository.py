from model.HoldingsModel import Holding
from database_connector import get_db_connection
from mysql.connector import Error


class HoldingsRepository:
    
    @staticmethod
    def getAllHoldings():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM HOLDINGS')
            result = cursor.fetchall()
            holdings = [Holding(*item).to_dict() for item in result]
            cursor.close()
            conn.close()
            return holdings
            
        except Error as error:
            conn.close()
            cursor.close()
            return -1
            
if __name__ == '__main__':
    print(HoldingsRepository.getAllHoldings())