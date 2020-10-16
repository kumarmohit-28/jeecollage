from flask import Flask,render_template,request,flash,redirect,url_for,session
import xlrd
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'JEE'
mysql=MySQL(app)
app.secret_key='qwertyuiopasdfgghh'
def Sort1(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            try:
                if (int(sub_li[j][7]) > int(sub_li[j + 1][7])):
                    tempo = sub_li[j]
                    sub_li[j] = sub_li[j + 1]
                    sub_li[j + 1] = tempo
            except:
                pass
    return sub_li



@app.route('/rank2019',methods=['GET','POST'])
def rank2019():
    session['len'] = False
    if(request.method=='POST'):
        rank=request.form.get('RANK')
        cat=request.form.get('Category')
        gen=request.form.get('GENDER')
        ins=request.form.get('INSTITUTE')
        rou=request.form.get('ROUND')
        #print(rou)
        if(ins=='IIT'):
            loc = ("templates/round"+str(rou)+"iit.xlsx")
        else:
            loc = ("templates/round"+str(rou)+"nit.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        l1=[]
        for row in range(3, sheet.nrows):
            try:
                if(int(sheet.cell_value(row, 7)) >= int(rank) and str(sheet.cell_value(row, 4)) == cat and str(sheet.cell_value(row, 5)) == gen):
                    l1.append(sheet.row_values(row))
                    print(sheet.row_values(row))
            except:
                continue
        l1=Sort1(l1)
        print(l1)
        if(len(l1)==0):
            session['len']=True
        return render_template('index.html',items=l1)
    return render_template('enter.html')

@app.route('/ins2019',methods=['GET','POST'])
def ins2019():
    session['len'] = False
    if(request.method=='POST'):
        ins1=request.form.get('suggestions')
        cat=request.form.get('Category')
        gen=request.form.get('GENDER')
        #ins=request.form.get('INSTITUTE')
        rou=request.form.get('ROUND')
        #print(ins1)
        if('Indian Institute of Technology' in str(ins1) or 'Indian Institute  of Technology' in str(ins1)):
            loc = ("templates/round"+str(rou)+"iit.xlsx")
        else:
            loc = ("templates/round"+str(rou)+"nit.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        l1=[]
        #print(ins1)

        for row in range(3, sheet.nrows):
            s = str(sheet.cell_value(row, 1))
            #print(s)
            if (s==ins1 and str(sheet.cell_value(row, 4)) == cat and str(sheet.cell_value(row, 5)) == gen):
                l1.append(sheet.row_values(row))
                #print(sheet.row_values(row))
        l1=Sort1(l1)
        #print(l1)
        return render_template('index.html',items=l1)
    loc = ("templates/round" + str(1) + "iit.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    l=[]
    for row in range(3, sheet.nrows):
        l.append(sheet.cell_value(row,1))
    loc = ("templates/round" + str(1) + "nit.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for row in range(3, sheet.nrows):
        l.append(sheet.cell_value(row,1))
    #print(l)
    try:
        l.remove("Institute")
    except:
        l=l
    l=set(l)
    return render_template('ins2019.html',items=l)

@app.route('/2020rank',methods=['GET','POST'])
def rank2020():
    l1=[['2020 round 1','results','will','be','out on','17th' ,'of','october']]
    if (len(l1) == 0):
        session['len'] = True
    return render_template('index.html', items=l1)
@app.route('/2020ins',methods=['GET','POST'])
def rankins():
    l1=[['2020 round 1','results','will','be','out on','17th' ,'of','october']]
    if (len(l1) == 0):
        session['len'] = True
    return render_template('index.html', items=l1)

@app.route('/',methods=['GET','POST'])
def home1():
    return render_template('home.html')
@app.route('/link')
def link():
    a='1'
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(number) VALUES(%s)",(a))
    mysql.connection.commit()
    cur.close()
    return render_template('link.html')
if __name__ == '__main__':
    app.run(debug=True)