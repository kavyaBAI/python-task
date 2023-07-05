from flask import Flask, render_template,request,redirect, url_for, session
from flask import Flask, request, \
        render_template, redirect, url_for, \
        session, send_file

app = Flask(__name__)

def read_txt(filename):
    res_list = []
    with open(r"C:\Users\kavya\OneDrive\Documents\form\custsubcost.txt") as file:
        for data in file:
            res = data.split()
            if res:
                if res not in res_list:
                    value = (res[1], res[2])
                    res_list.append(value)
                else:
                    res_list
    return res_list

@app.route('/',methods=["GET","POST"])
def out_values():
    res_list =[]
    if request.method== "POST":
        Customer_name = request.form['Customer']
        date_range  =request.form['AppId']
        Customer_name1 = eval(Customer_name)
        date_range1 = eval(date_range)
        # print(type(Customer_name1))
        # print(date_range1)

    # comapny_names = ['DR_Dev/QA/Demo', 'DRTrial', 'Anunta BLR']
    # date_range = ['2023-07-03', '2023-07-02', '2023-07-01']
        sanath_data = {
        ('DR_Dev/QA/Demo', 'd4315828-9f12-44a4-b1b0-7681c3f39623'): ['2023-07-03', 34, 0],
        ('DRTrial', 'a24d81d4-940f-4503-95d7-46748219b4d8'): ['2023-07-02', 45, 1],
        ('Anunta BLR', 'f8cc1812-93a2-4b37-9dd6-12176eae5028'): ['2023-07-02', 88, 0]
        }
    
        for c1 in zip(Customer_name1, date_range1):
            c2 = c1[0]
            c3 = c1[1]
            res = c3.split("-")
            filename = "%s_%s_%s.txt" % (c2, res[1], res[0])
            res1 = read_txt(filename)
            
            for (sub, cost) in res1:
                key = (c2, sub)
                data = sanath_data.get(key)
                
                if data is not None:
                    temp_list = [c2, sub, data[0], cost, data[1], data[2]]
                    res_list.append(temp_list)
        return render_template('table.html',dea = res_list)
        
    return render_template('base1.html')



if __name__ == '__main__':
    app.run(debug=True)
