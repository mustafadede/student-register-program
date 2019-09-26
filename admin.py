import sqlite3
# ADMİN OBJECT
class Admin():
  def __init__(self,admin_id = None,admin_namesurname = None,admin_pass = None,admin_autorization = None):
    self.admin_id = admin_id
    self.admin_namesurname = admin_namesurname
    self.admin_pass = admin_pass
    self.admin_autorization = admin_autorization
  def __str__(self):
    return f"Admin id: {self.admin_id}\nAdmin name: {self.admin_namesurname}\nAdmin Autorization: {self.admin_autorization}"
# ADMİN DATABASE OBJECT
class AdminDatabase():
  def __init__(self):
    self.connection()
  def connection(self):
    self.link = sqlite3.connect("admin_database.db")
    self.cursor = self.link.cursor()
    """Admin autorization needs to be yes or no"""
    self.cursor.execute("Create table If not exists ADMIN (admin_id integer PRIMARY_KEY,admin_namesurname text,admin_pass integer,admin_autorization text)")
    self.link.commit()
  def disconnection(self):
    self.link.close()
  #CREATE ADMİN
  def create_admin(self,Admin):
    self.cursor.execute("Insert into ADMIN VALUES (?,?,?,?)",(Admin.admin_id,Admin.admin_namesurname,Admin.admin_pass,Admin.admin_autorization))
    self.link.commit()
  def admin_nick(self,name):
    self.cursor.execute("Select admin_namesurname from ADMIN where admin_namesurname=?",(name,))
    admin = self.cursor.fetchall()
    for name in admin:
      return True
    self.link.commit()
  def admin_pass(self,passw):
    self.cursor.execute("Select admin_pass from ADMIN where admin_pass=?",(passw,))
    admin_passw = self.cursor.fetchall()
    for name in admin_passw:
      return True
    self.link.commit()
  def all_admin(self):
    self.cursor.execute("Select admin_id,admin_namesurname,admin_autorization from ADMIN") 
    admin = self.cursor.fetchall()
    if len(admin) == 0:
      print("There is no record") 
    else:
      all_admin=0
      for i in admin:
        admins = Admin(i[0],i[1],i[2])
        all_admin+=1
        print(admins)
        print("  --  ")
        print("Total Admin = "+str(all_admin))