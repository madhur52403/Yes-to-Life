# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 20:06:01 2018

@author: kevin
"""
import sqlite3
db = sqlite3.connect("Users.sqlite")

# Creating a table
db.execute("CREATE TABLE IF NOT EXISTS registerUsers(id integer primary key autoincrement,username text not null,password text not null)")

db.commit()   
db.close() 
