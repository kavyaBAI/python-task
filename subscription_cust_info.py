import mysql.connector



def get_connection(data):
    khost, kuser , kpasswd , kdb = data.split('#')
    conn = mysql.connector.connect(host= khost, user= kuser,passwd= kpasswd,db=kdb, charset="utf8")  
    cur = conn.cursor() 
    return conn, cur

def getProfile(DB_CONNECTION_STR, ln):
    res_dict ={}
    conn, cur = get_connection(DB_CONNECTION_STR) 
    sql = "select cust_name from cust_info WHERE cust_id=%s;"
    val=(ln)
    cur.execute(sql %(val))
    res = cur.fetchone()
    res_name = res[0]
    sql1 = "select sub_id,tenant_id,app_id,secret_key  from subscription_table WHERE cust_id=%s;" 
    q1= (ln)
    cur.execute(sql1%(q1))
    res1 = cur.fetchall()
    for i in res1:
        res_info=list(i)
       
        if res_name not in res_dict:
                res_dict[res_name] = res_info
        else:
                res_dict[res_name].append(res_info)
    print(res_dict)        

    cur.close() 
    conn.close() 


if __name__=='__main__':
   DB_CONNECTION_STR="localhost#root#Kavya8787@#prajina_task"
   id = 17 
   getProfile(DB_CONNECTION_STR,id)