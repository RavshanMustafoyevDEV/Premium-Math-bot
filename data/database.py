import sqlite3
import datetime



class Database:

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
    


    def buy_order(self, type, id_type):
        with self.con:
            def generate_redeem():
                import uuid
                return uuid.uuid1()

            if type == 'mavzu':
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
            
            elif type == 'test':
                reedem_code = generate_redeem()
                self.con.execute(f"INSERT INTO reedem VALUES('{reedem_code}', '{type}', '{id_type}',False)")
                self.con.commit()
                return reedem_code


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


    def get_reedem(self, code):
        with self.con:
            r = self.con.execute(f'SELECT * FROM reedem WHERE code = "{code}"').fetchone()

            if r:
                return r
            else:
                pass


    def set_saled_mavzu(self, idMavzu, user_id):
        with self.con:
            t = self.con.execute(f"SELECT * FROM mavzular WHERE id = '{idMavzu}'").fetchone()
            if t:
                price = t[2]
                date_full = datetime.datetime.now().strftime("%d-%b-%Y")
                self.con.execute(f"INSERT INTO saled_mavzu VALUES('{idMavzu}', '{t[1]}','{price}', '{date_full}', '{user_id}')")
                self.con.commit()
                return True
            else:
                pass


    def get_my_mavzu(self, user_id):
        with self.con:
            my_mavzu = self.cursor.execute(f"SELECT * FROM saled_mavzu WHERE userID = {user_id}").fetchall()

            if my_mavzu:
                return my_mavzu

            else:
                pass

    def get_saled_mavzu(self):
        with self.con:
            t = self.con.execute("SELECT * FROM saled_mavzu").fetchall()
            q = []

            for r in t:
                j = r[2]
                q.append(j)


            return q

    





                




    #-----------------------------------------------------------TESTS

    def set_new_test(self, unit, answers, price, file_id): # Yangi test yaratish
        with self.con:
            self.cursor.execute(f"INSERT INTO testlar(unit, answers, price, file_id) VALUES('{unit}','{answers}','{price}', '{file_id}')")
            self.con.commit()
            return True

    def get_test(self, idTest): # Test haqida barcha ma'umotni olish
        with self.con:
            r = self.con.execute(f"SELECT * FROM testlar WHERE test_id = '{idTest}'").fetchall()
            if r:
                return r
            else:
                pass

    def get_test_by(self, unit): # Test haqida barcha ma'umotni olish
        with self.con:
            r = self.con.execute(f"SELECT * FROM testlar WHERE unit = '{unit}'").fetchall()
            if r:
                return r
            else:
                pass



    def get_random_test_by_unit(self, unit, not_test_id):
        with self.con:
            u = self.con.execute(f"SELECT * FROM units WHERE unit = '{unit}'")
            if u:
                r = self.con.execute(f"SELECT * FROM testlar WHERE unit = '{unit}' AND  price != 0 AND test_id != '{not_test_id}' ORDER BY RANDOM() LIMIT 1").fetchone()

                if r:
                    return r

                else:
                    pass
            else:
                pass

    def get_random_free_test_by_unit(self, unit, not_test_id):
        with self.con:
            u = self.con.execute(f"SELECT * FROM units WHERE unit = '{unit}'")
            if u:
                r = self.con.execute(f"SELECT * FROM testlar WHERE unit = '{unit}' AND  price == 0 AND test_id != '{not_test_id}' ORDER BY RANDOM() LIMIT 1").fetchone()

                if r:
                    return r

                else:
                    pass
            else:
                pass


    def get_all_tests(self):
        with self.con:
            r = self.con.execute("SELECT * FROM testlar").fetchall()
            return r



    def remove_test(self, idTest): # Testni o'chirish
        with self.con:
            try:
                self.con.execute(f"DELETE FROM testlar WHERE test_id = '{idTest}'")
                self.con.commit()
                return True
            except:
                return False

    
    def get_test_reedem(self, code):
        with self.con:
            r = self.con.execute(f'SELECT * FROM reedem WHERE code = "{code}"').fetchall()

            if r:
                return r
            else:
                return False


    def set_saled_test(self, idTest, user_id, test_price):
        with self.con:
            t = self.con.execute(f"SELECT * FROM testlar WHERE test_id = '{idTest}'").fetchone()
            if t:
                date_full = datetime.datetime.now().strftime("%d-%b-%Y")
                self.con.execute(f"INSERT INTO saled_tests VALUES('{t[0]}', '{date_full}','{test_price}', '{user_id}')")
                self.con.commit()
                return True
            else:
                pass


    def check_test_answers(self, test_id, test_answers):
        with self.con:
            def check_test(keys, answers, test_id):
                if len(keys) == len(answers):
                    keys = keys.upper()
                    answers = answers.upper()
                    togri = []
                    xato = []

                    for count, (savol, javob) in enumerate(zip(answers, keys), 1):
                        if savol == javob:
                            togri.append(count)
                        if savol != javob:
                            xato.append(count)
            
                    len_togri = len(togri)
                    len_savollar = len(answers)

                    foiz = (len_togri * 100) / len_savollar


                    togri_result = f"To'g'ri javoblar : {len(togri)} ta (" + ",".join(str(x) for x in togri) + ") ✅"
                    xato_result = f"Xato javoblar : {len(xato)} ta (" + ",".join(str(y) for y in xato) + ") ❓"
                    foiz_result = f"Foiz : {round(int(foiz))} % 📑" 
                    return f"{togri_result}\n{xato_result}\n{foiz_result}"
                    
                else:
                    pass

            t = self.get_test(idTest=test_id)
            if t:
                for i in t:
                    output = check_test(keys=test_answers, answers=i[2], test_id=test_id)
                    if output:
                        return output
                    else:
                        return f"Xatolik: savollar soni {len(i[2])} ta siz kiritgan javoblar soni {len(test_answers)} ta ("
            else:
                pass


    def get_my_tests(self, user_id):
        with self.con:
            my_tests = self.con.execute(f"SELECT * FROM saled_tests WHERE user_id = {user_id}").fetchall()
            if my_tests:
                return my_tests

            else:
                return False
            





    


#  UNTIS================================================================
    def new_unit(self, unit):
        with self.con:
            self.con.execute(f"INSERT INTO units(unit) VALUES('{unit}')")
            self.con.commit()

    def remove_unit(self, unit):
        with self.con:
            u = self.con.execute(f"SELECT * FROM units WHERE unit = '{unit}'").fetchall()
            if u:
                self.con.execute(f"DELETE FROM units WHERE unit = '{unit}'")
                self.con.commit()
                return True
            else:
                return False


    def list_unit(self):
        with self.con:
            u = self.con.execute("SELECT unit FROM units").fetchall()
            return u




    # bot ===================================================
    def get_users(self):
        with self.con:
            users = self.con.execute("SELECT * FROM users").fetchall()
            return users

    def get_saled_tests(self):
        with self.con:
            t = self.con.execute("SELECT * FROM saled_tests").fetchall()
            q = []

            for r in t:
                j = r[2]
                q.append(j)


            return q
        





    # ADMIN ADD REMOVE==========================================
    def get_admins(self):
        with self.con:
            list = self.cursor.execute("select user_id from admins").fetchall()
            return list



