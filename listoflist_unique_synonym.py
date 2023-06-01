Task- create 2 tables insert the values for the given input get the listoflist without duplicate values.

import mysql.connector


def connection(user):
  khost,kname,kpass,kdb=user.split(#)
   my_conn=mysql.connector.connect(Host=khost,user=kname,paswd=kpass,databse=kdb)
   cur=my_conn.cursor()
   cur.close()
   my_conn.close()
    return con,my_conn
  
 def task(db_connection):
    connection(db_connection)
    sql="select drug_id from drugtable"
    cur.excute(sql)
    res=cur.fetchone()
    print(res) # 54
    sql="select sysnoms from the synonym where drug_id=%s"
    cur.execute(sql,%res)
    cur.fetchall()
     
  
  if ___name__=='__main__':
    db_connection=localhost#root#kavya8787@#info
    task()
