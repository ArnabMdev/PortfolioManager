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
            print(error)
            cursor.close()
            conn.close()
            return -1
        
    @staticmethod
    def getHolding(asset_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM HOLDINGS WHERE asset_id = %s',(asset_id,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            if(result):
                holding = Holding(*result).to_dict()
                return holding
            else:
                return -1
                
        except Error as error:
            print(error)
            cursor.close()
            conn.close()
            return -1
    
    @staticmethod
    def addHolding(holding:Holding):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            insertstmnt = 'INSERT INTO HOLDINGS VALUES (%s,%s,%s,%s,%s)'
            data = (holding.asset_id, holding.ticker, holding.asset_type, holding.qty, holding.avg_price)
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
    def updateHolding(holding:Holding):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            updatestmnt = 'UPDATE HOLDINGS SET ticker = %s, asset_type = %s, qty = %s, avg_price = %s WHERE asset_id = %s'
            data = (holding.ticker, holding.asset_type, holding.qty, holding.avg_price, holding.asset_id)
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
    def deleteHolding(asset_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM HOLDINGS WHERE asset_id = %s',(asset_id,))
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
            
            
            
         
            
if __name__ == '__main__':
    hold = Holding(2,'GOOGLE','stock',1,100)
    print(HoldingsRepository.deleteHolding(2))
    print(HoldingsRepository.getAllHoldings())
