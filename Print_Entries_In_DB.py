# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 20:53:48 2018

@author: kevin
"""

import sqlite3

db = sqlite3.connect("Users.sqlite")

# Printing the values in database so far
for name, phone, email in db.execute("SELECT * FROM registerUsers"):
    print(name)
    print(phone)
    print(email)
    print("-" *20)

db.close()    