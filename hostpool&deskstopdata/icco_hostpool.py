import pandas as pd
import MySQLdb    #pip install mysqlclient

def get_connection(data):
    khost, kuser , kpasswd , kdb = data.split('#')
    conn = MySQLdb.connect(host= khost, user= kuser,passwd= kpasswd,db=kdb, charset="utf8")  
    cur = conn.cursor() 
    return conn, cur

def read_csv(DB_CONNECTION_STR):
    conn, cur = get_connection(DB_CONNECTION_STR) 
    df = pd.read_csv(r'C:\Users\kavya\OneDrive\Documents\form\DR_Zenworx-hostpool.csv')
    dict_res ={}
    for index, row in df.iterrows():   
        host_pool = row['HOST POOL']
        if host_pool == 'Total':
            pass
        else:
            for col in df.columns[1:]:  
                date = col
                value = row[date]
                if date not in dict_res:
                    dict_res[(host_pool,date)] = value
    for key,value in dict_res.items():
        sql = "insert into hostpool_cost(date,cust_name,subscription,hostpool_name,cost)values('%s','Dr_Zenworx','8ccf20a5-83d7-45a9-ba84-d3f0a0cf93d0','%s',%s)" 
        val = ((key[1]),key[0],value)
        print(sql%(val))
        cur.execute(sql%(val))  
           
    conn.commit()
    cur.close()
    conn.close()
 

if __name__=='__main__':
   DB_CONNECTION_STR="localhost#root#Kavya8787@#durga_task" 
   read_csv (DB_CONNECTION_STR)

