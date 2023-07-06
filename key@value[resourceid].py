import pandas as pd 


def tags_resourceid():
    file_path = r"C:\Users\kavya\OneDrive\Documents\currency convertor\Firstsource_Solutions_Ltd_april.csv"
    df = pd.read_csv(file_path,usecols=["ResourceId","tags"])
    res = len(df.index)
    res_dict = {}
    for i in range(res):
        res_dict = {}
        value = df.iloc[i]
        resource_id = value[0]
        tag_id = str(value[1])
        if 'nan' not in tag_id:
            val = eval(tag_id)
            for key,value in val.items():
                val =value.replace(" ","_")
                x = "@".join([key,val])
                if x not in res_dict:
                    res_dict[x] = [resource_id]
                else:
                    res_dict[x].append(resource_id)
        print(res_dict)   
    
    #print(res_dict) 
    # print(len(res_dict))
    # for key, val in res_dict.items():
    #     print(f"{key}: {val}")
    #     print()        

tags_resourceid()