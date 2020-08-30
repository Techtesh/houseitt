# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 00:36:07 2020

@author: Hitesh
"""
import sqlite3
#from structs import values


    
def column(table):
    conn = sqlite3.connect(r'C:\Users\Hitesh\Desktop\data\project 11b\houseiit\db.sqlite3')
    c = conn.cursor()
    #print("connection established")
    
    a=c.execute (f"select * from {table}")
    for row in a :
        print(row)
        
    names = [description[0] for description in c.description]
    #print(names)
    return names[1:]
    conn.close()
    
def updateDB(table,data):
    print(data)
    column_name=tuple(column(table))
    #print(column_name)
    
    conn = sqlite3.connect(r'C:\Users\Hitesh\Desktop\data\project 11b\houseiit\db.sqlite3')
    c = conn.cursor()
    if column_name[-1]=="main_id_id":
        print("@@@@@@@@@@@@@@@@@@@ as planned")
        updates=c.execute("select id from calc_primaryform where id >25")
        for val in updates:
               latest=val[0]
               print(latest,type(latest))
    if column_name[-1]=="main_id_id":
            print("################## i am in a subform addn data:",latest)
            data.append(latest)
    
    print("connection established")
    print(data)
    for index,val in enumerate(data):
        try:
            temp=eval(val)
            data[index]=temp
        except:
            pass
    #print(column_name)
    
           
    
    for x,y in zip(column_name,data):
        print(f"{x}:{y}")
    try:   
        
        data=data[:len(column_name)]
        
        temp="?,"*len(column_name)
        temp=temp[:-1]
        print(f"insert into {table} {column_name}values({data})")
        
        c.execute(f"insert into {table} {column_name}values({temp})",data)
        
    except Exception as e:
        print("error happened",e)
    else:
        print("data updated succesfully")
    conn.commit()
    conn.close()
#data=["a113","sharing","12000","False","250000","True","anyone","False"]
#updateDB("calc_primaryform",data)



    