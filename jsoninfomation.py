task: given 2 excel files 1 had all the detailes and 2 nd one they have chosen specific columns for that u should add the details.it had multiple sheets in excel.
  
  so reading multiple sheets from python the code looks like below :
     import pandas as pd 
      worksheets=["sheet1","sheet2"]
      col=['A,B,C' ,'B,C']
      path=r"path of the file"
      
      for wc,cl  zip in (worksheeets,col):
        df=pd.read_excel(path,sheetname=worksheets,usecols=col,header=0)
         print(df) // it will print dfframes for 2 differnt sheets 
          
          part2- in this after reading multiple sheets append on the json file
          
          lets us undertsnd little bit about the json
          JSON-java script object notation 
          1.json which is like{} have 2 methods dump/dumps,load/loads
          2.python dict --------dump/dumps--------------->json dict
                             (serialized)
                       <--------load/loads----------------
                          (unserialized)
          3.but in the above code its in dataframe convert into dict
          for that use to_dict() method-->this method will convert pandas dataframe to dict.python
            to_dict(orient="dict") it can be anything dict ,records many options are there
            
           .
          .  . res=df.to_dict(orient='records')
          with open ('filename','a') as fs:
            json.dump(res,fs)
         Difference between dump and dumps :
         ______________________________________
        
        Dumps->
        if input is in the form of list or any other format then it will terun in "string"
        if ip in the {} it will return same
        
      Dump->
      if input in the {} the output will will be {}
      
      thew loads and load
      json.load(filename)
        
        
        
        
        
        
        
        
        
        
        
      
