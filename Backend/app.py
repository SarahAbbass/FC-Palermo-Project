import psycopg2
from flask import Flask
from flask import render_template, request
from datetime import datetime
from model.backend import login, register, dateFormat, emailFormat, passwordFormat, usernameFormat, updatePass, belongs, updateEmail, deleteAcc

conn = psycopg2.connect(database = 'Palermo', user = 'postgres', password = 'Anar19672001', host = 'localhost', port = '5432')
cursor = conn.cursor()




app = Flask(__name__)
@app.route("/", methods = ['GET','POST'])
def main():
    return render_template('homepage.html')

@app.route("/login", methods = ['GET','POST'])
def login_main():
    
        cursor = conn.cursor()
        if request.method=='GET':
            return render_template('login.html')
        else:
            username = request.form['username']
            password = request.form['pass']
            if username == "" or password == "":
                empty_log = True
                return render_template('login.html', empty_log=empty_log)
            
            if belongs(conn, cursor, username, 'users') == False:
                user_belong = False
                return render_template('delete.html', user_belong=user_belong)
            
            cursor.execute('select pass from users where username = \'' + username + '\';')
            result = cursor.fetchall()
            match = False
            for row in result:
                if password in row:
                    match = True
            if match == False:
                return render_template('login.html', match=match)
            log = login(cursor, username, password)
            if log == True:
                success = True
                return render_template('login.html', success = success)
            # render next page where user has profile instead of login above
            else:
                success=False
                return render_template('login.html', success = success)
                
@app.route("/register", methods = ['GET','POST'])
def register_main():
    
        cursor = conn.cursor()
        if request.method=='GET':
            return render_template('register.html')
        else:
            email = request.form['email']
            username = request.form['username']
            password = request.form['pass']
            country = request.form['country']
            dob = request.form['dob']
            # check lengths and formats of inputs
            if email == "" or username == "" or password == "" or country == "" or dob == "":
                empty = True
                return render_template('register.html', empty=empty)
            if emailFormat(email) == False:
                emailF = False
                return render_template('register.html', emailF = emailF)
            if usernameFormat(username) == False:
                userF = False
                return render_template('register.html', userF = userF)
            if passwordFormat(password) == 'wrong length':
                length = False
                return render_template('register.html', length=length)
            if passwordFormat(password) == 'missing conds':
                conds = False
                return render_template('register.html', conds=conds)
            if dateFormat(dob) == False:
                bad_date = True
                return render_template('register.html', bad_date=bad_date)
            try_reg = register(conn, cursor, email, username, password, country, dob)
            if try_reg == True:
                success2 = True
                return render_template('register.html', success2 = success2)
            else:
                success2 = False
                return render_template('register.html', success2 = success2)
            
@app.route("/update_pass", methods = ['GET', 'POST'])
def updatePass_main():
    if request.method == 'GET':
        return render_template('updatePass.html')
    username = request.form['username']
    newPass = request.form['newPass']
    if username == "" or newPass == "":
        empty_u = True
        return render_template('updatePass.html', empty_u=empty_u)
    if belongs(conn, cursor, username, 'users') == False:
        user_belong = False
        return render_template('updatePass.html', user_belong=user_belong)
    if passwordFormat(newPass) == 'wrong length':
        lengthN = False
        return render_template('updatePass.html', lengthN=lengthN)
    if passwordFormat(newPass) == 'missing conds':
        condsN = False
        return render_template('updatePass.html', condsN=condsN)
    if updatePass(conn, cursor, username, newPass) == True:
        successN = True
        return render_template('updatePass.html', successN=successN)
    else:
        successN = False
        return render_template('updatePass.html', successN=successN)
        
@app.route("/update_email", methods = ['GET', 'POST'])
def updateEmail_main():
    if request.method == 'GET':
        return render_template('updateEmail.html')
    username = request.form['username']
    newEmail = request.form['newEmail']
    if username == "" or newEmail == "":
        empty_e = True
        return render_template('updateEmail.html', empty_e=empty_e)
    if belongs(conn, cursor, username, 'users') == False:
        user_belong = False
        return render_template('updateEmail.html', user_belong=user_belong)
    if emailFormat(newEmail) == False:
        emailF = False
        return render_template('updateEmail.html', emailF=emailF)
    if belongs(conn, cursor, newEmail, 'users') == True:
        email_belong = True
        return render_template('updateEmail.html', email_belong=email_belong)
    if updateEmail(conn, cursor, username, newEmail) == True:
        successE = True
        return render_template('updateEmail.html', successE=successE)
    else:
        successE = False
        return render_template('updateEmail.html', successE=successE)   

@app.route("/delete_acc", methods = ['GET', 'POST'])
def delete():
    if request.method == 'GET':
        return render_template('delete.html')
    username = request.form['username']
    password = request.form['pass']
    if username == "" or password == "":
        empty_u = True
        return render_template('delete.html', empty_u=empty_u)
    if belongs(conn, cursor, username, 'users') == False:
        user_belong = False
        return render_template('delete.html', user_belong=user_belong)
    cursor.execute('select pass from users where username = \'' + username + '\';')
    
    # check if tuple (username, pass) belongs
    result = cursor.fetchall()
    print(result)
    match = False
    for row in result:
        if password in row:
            print(row)
            match = True
    if match == False:
        return render_template('delete.html', match=match)
    if deleteAcc(conn, cursor, username, password) == True:
        success = True
        return render_template('delete.html', success=success)
    else:
        success = False
        return render_template('deete.html', success=success)
    
############################# ACCOUNT MANAGEMENT ################################


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)