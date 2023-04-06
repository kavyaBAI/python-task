import pandas as pd
import mysql.connector

def csv_read():
    res2={}
    df=pd.read_csv(r'C:\Users\kavya\OneDrive\Documents\readfilewget\listofdocid.csv')
    length=len(df.index)
    for i in range(length):
        value=df.iloc[i]

        val1=value[0]
        val2=value[1]
        res=eval(val2)
        res1=[]
        for i in res:
            val3=i[1]
            res1.append(val3)
        res2[val1]=res1
    return res2       

def db_read():
    db_conn=mysql.connector.connect(host='localhost',user='root',passwd='Kavya8787@',database='users')
    cur=db_conn.cursor(buffered=True)
    data = csv_read()
    for key, values in data.items():
        q1=("select search_conf_id from uploaddocuments where id=%s")
        cur.execute(q1, (key,))
        existing_values = [row[0] for row in cur.fetchall()]
        for val in values:
            if val in existing_values:
                continue     
            q3="insert into uploaddocuments(search_conf_id)values(%s)"
            cur.execute(q3, (val,))
            db_conn.commit()
            print(f"Inserted value {val} for key {key}")

db_read()          
