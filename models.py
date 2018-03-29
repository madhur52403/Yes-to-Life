# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 22:40:59 2018

@author: kevin
"""

import sqlite3 as sql

# Function to add new users to the database
def insertUser(username,password):
    con = sql.connect("Users.sqlite")
    cur = con.cursor()
    cur.execute("INSERT INTO registerUsers (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

    
