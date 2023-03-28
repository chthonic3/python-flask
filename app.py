from flask import Flask, render_template, request
import db
import datetime
import pandas as pd
import pymysql
import time

app = Flask(__name__)

#
@app.route('/')
def main():
    #展示廠的資料
    sql = 'select id,machineTyp1,machineNo1,loc1,place1 from mac_loc where enable1="1" ORDER BY machineTyp1 ASC, machineNo1 ASC'
    datas = db.query_data(sql)
    return render_template('index.html', datas=datas)

@app.route('/<machineTyp>/<machineNo>')
def index(machineTyp,machineNo):
    date = datetime.date.today()
    #搜尋資料庫是否有此機型或機號，limit就是只要有就停止搜尋
    sql = 'select machineTyp,machineNo from user where machineTyp="'+ machineTyp +'"' +'and machineNo="'+machineNo+'" limit 1'
    #將搜尋到的資料存放在datas下備用
    datas = db.query_data(sql)
    #查詢有資料就放在exit_datas為1，沒有就為0
    exit_datas=len(datas)
    if exit_datas==1:#如果有資料
        #用來html顯示順序備用
        sql1 = 'select * from user where machineTyp="'+ machineTyp +'"' +'and machineNo="'+machineNo+'" ORDER BY date DESC'
        datas1 = db.query_data(sql1)

        #抓取此機台最後一筆日期，與今日比較用
        sql2 = 'SELECT date FROM user where machineTyp="'+ machineTyp +'"' +'and machineNo="'+machineNo+'" ORDER BY date DESC LIMIT 1'
        datas2 = db.query_data(sql2)     
        #   
        for item in datas2:
            for key in item:
                data_date=item[key]

        if data_date !=date:
            update_date='今日無更新'
        else:
            update_date='已更新'
        
        return render_template('show_add_user.html', machineTyp=machineTyp,machineNo=machineNo,date=date,datas1=datas1,update_date=update_date)
    else:
        return render_template('show_add_user.html', machineTyp=machineTyp,machineNo=machineNo,date=date)



@app.route("/do_add_user",methods=['POST'])
def do_add_user():
    machineTyp = request.form.get("machineTyp")
    machineNo = request.form.get("machineNo")
    backlog = request.form.get("backlog")
    user = request.form.get("user")
    date = request.form.get("date")
    # print(user)
    if machineTyp and machineNo and backlog and user and date !="":
        sql = f"""
            insert into user (machineTyp , machineNo , backlog , user , date)
            values('{machineTyp}' , '{machineNo}' , '{backlog}' , '{user}' , '{date}')
        """
        print(sql)
        db.insert_or_update_data(sql)
        return render_template("success.html",machineTyp=machineTyp,machineNo=machineNo)
    else:
        return render_template("err.html")

@app.route("/do_update_user/<machineTyp>/<machineNo>/<user_id>/<date>",methods=['POST','GET'])
def do_update_user(machineTyp,machineNo,user_id,date):
    machineTyp = machineTyp
    machineNo = machineNo
    date = request.form.get("date")
    print(date)
    sql = f"""
            UPDATE user SET enddate = '{date}' WHERE id = '{user_id}'
        """ 
    db.insert_or_update_data(sql)
    return render_template("success_update.html",machineTyp=machineTyp,machineNo=machineNo)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0")
    
    # #先將電腦的IP4改為IP，然後在下方host改為此電腦的ip，就可以連線
    # app.run(debug=True,host='192.168.185.16',port=5000)
