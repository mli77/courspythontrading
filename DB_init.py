import sqlite3
import uuid

'''
Ceci est un long commentaire
'''
class Initializer(object):
    
    def execute(self):
        # On se connecte à la base de données (elle va être créée la première fois)
        conn = sqlite3.connect('mabase.db')
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS cotations (
                  id INTEGER PRIMARY KEY,
                  symbol_id TEXT,
                  time_exchange TEXT,
                  price REAL,
                  size REAL
            ) 
        ''')

        c.execute("INSERT INTO cotations (symbol_id, time_exchange, price, size) VALUES (?, ?, ?, ?)", ('AAPL', '2024-03-02', 280.0, 2344))
        c.execute("INSERT INTO cotations (symbol_id, time_exchange, price, size) VALUES (?, ?, ?, ?)", ('AAPL', '2024-03-03', 284.0, 4000))

        c.execute("select id, symbol_id, time_exchange, price, size from cotations order by time_exchange")
        rows = c.fetchall()

        for row in rows:
            id, symbol_id, time_exchange, price, size = row

            print(f"{id} {symbol_id} {time_exchange} {price} {size} ")
        
        c.close()
        conn.commit()

        conn.close()

class DBHelper(object):
    def read_data(self):
        conn = sqlite3.connect('mabase.db')
        c = conn.cursor()

        c.execute("select id, symbol_id, time_exchange, price, size from cotations order by time_exchange")
        rows = c.fetchall()

        for row in rows:
            id, symbol_id, time_exchange, price, size = row

            print(f"{id} {symbol_id} {time_exchange} {price} {size} ")
        
        c.close()

        conn.close()

if __name__ == '__main__':
    #objet1 = Initializer()
    #objet1.execute()

    reader = DBHelper()
    reader.read_data()
