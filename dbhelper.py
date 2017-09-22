import pymysql
import dbconfig

class DBHelper:


    def connect(self, database='business_map'):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)


    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description from business_list;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()


    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO business_list(description) VALUES('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()



    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM business_list;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()