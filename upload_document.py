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
csv_read() 
def db_read():
    db_conn=mysql.connector.connect(host='localhost',user='root',passwd='Kavya8787@',database='users')
    cur=db_conn.cursor(buffered=True)
    l=csv_read()
    l2=list(l.keys()) #[1775,1756,1758]
    for l3 in l2:    
        q1=("select search_conf_id from uploaddocuments where id=%s")
        cur.execute(q1%(l3))
        l7=cur.fetchall()
        l9=l7[0][0]
        sql="select userid,docname,doctype,upload_time,process_st_time,process_en_time,filepath from uploaddocuments where id=%s"
        valsql=l3
        cur.execute(sql%(valsql))
        rem=cur.fetchone()
        #print(rem[0],rem[1],rem[2],rem[6])
        #print(l9) #[(97,)]
        values1=list(l[l3] )#[97,98,55]
        for val in values1:
            if l9 == val:
                pass     
            else:
                q3="INSERT INTO uploaddocuments (userid,docName,docType,upload_time,process_st_time,process_en_time,filepath,search_conf_id) values(%s,'%s','%s',now(),now(),now(),'%s',%s)"
                val5=(rem[0],rem[1],rem[2],rem[6],val)
                res5=cur.execute(q3%(val5))
                db_conn.commit()
                print(res5)
                
        
     
   



db_read()          


    
