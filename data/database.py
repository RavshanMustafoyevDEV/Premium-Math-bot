import sqlite3



class Database:
    import sys
    sys.setrecursionlimit(2000)

    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cursor = self.con.cursor()

    def get_mavzu(self, idMavzu):
        with self.con:
            m = self.cursor.execute(f'SELECT * FROM mavzular WHERE id = "{int(idMavzu)}"').fetchall()

            if m is not None:
                return m
            else:
                return False


    #Your database
    def regUser(self, id, name, number):
        with self.con:
            user = self.cursor.execute(f'SELECT id FROM users WHERE id = {id}').fetchone()
            if user:
                return False
            
            else:
                self.cursor.execute(f"INSERT INTO users VALUES('{id}', '{name}', '{number}')")
                self.con.commit()
                return True

    def checkUser(self, id):
        with self.con:
            user = self.cursor.execute(f"SELECT id FROM users WHERE id = {id}").fetchone()
            if user:
                return True
            else:
                return False


    def get_mavzular(self):
        with self.con:
            mavzular = self.cursor.execute(f"SELECT * FROM mavzular").fetchall()
            return mavzular

    def get_premium_mavzular(self):
        with self.con:
            mavzular = self.cursor.execute(f"SELECT * FROM mavzular WHERE price != 0").fetchall()
            return mavzular


    def get_free_mavzular(self):
        with self.con:
            mavzular = self.cursor.execute(f"SELECT * FROM mavzular WHERE price = 0").fetchall()
            return mavzular




    def set_newMavzu(self, name, price, about, file_id):
        with self.con:
            mavzu = self.con.execute(f'SELECT * FROM mavzular WHERE nomi = "{name}"').fetchone()

            if mavzu:
                return False
            else:
                self.con.execute(f"INSERT INTO mavzular(nomi, price, about, file_id) VALUES('{name}', '{price}', '{about}', '{file_id}')")
                self.con.commit()

                return True

    def remove_Mavzu(self, id):
        with self.con:
            mavzu = self.con.execute(f"SELECT * FROM mavzular WHERE id = '{id}'")
            if mavzu:
                self.con.execute(f"DELETE FROM mavzular WHERE id = '{id}'")
                self.con.commit()
                return True
            else:
                return False
    


    def buy_mavzu(self, type, id_type):
        with self.con:
            def generate_redeem():
                import uuid
                return uuid.uuid1()


            mv = self.get_mavzu(idMavzu=id_type)
            for m in mv:
                if m:
                    if m[2] != 0:
                        reedem_code = generate_redeem()
                        self.con.execute(f"INSERT INTO reedem VALUES('{reedem_code}', '{type}', '{id_type}',False)")
                        self.con.commit()
                        return reedem_code
                    else:
                        return 'free'
                else:
                        return False


    def activate_reedem(self, reedem_code):
        with self.con:
            r = self.con.execute(f'SELECT * FROM reedem WHERE code = "{reedem_code}"').fetchall()

            if r:
                self.con.execute(f"UPDATE reedem SET activated = True WHERE code = '{reedem_code}'")
                self.con.commit()
                return True
            else:
                return False



    def delete_reedem(self, reedem_code):
        with self.con:
            r = self.con.execute(f"SELECT * FROM reedem WHERE code = '{reedem_code}'").fetchall()

            if r:
                self.con.execute(f"DELETE FROM reedem WHERE code = '{reedem_code}'")
                self.con.commit()
                return True
            else:
                return False


    def get_mavzu_reedem(self, code):
        with self.con:
            r = self.con.execute(f'SELECT * FROM reedem WHERE code = "{code}"').fetchall()

            if r:
                return r
            else:
                return False




                








