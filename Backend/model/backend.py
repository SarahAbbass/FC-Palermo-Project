from datetime import datetime
import string


def login(cursor, username, password):
    # check if user already exists
    query = 'select username from users'
    cursor.execute(query)
    usernames = cursor.fetchall()
    isFound = False
    for row in usernames:
        if username in row:
            isFound = True
            cursor.execute('select pass from users where username = \'' + username + '\';')
            conf = cursor.fetchall()[0]
            if password in conf:
                return isFound
            
    return isFound
  
    
def dateFormat(date):
#     'DD/MM/YYYY'
    DD = date[0:2]
    MM = date[3:5]
    YYYY = date[6:10]
    test = YYYY + '-' + MM + '-' + DD
#        
    try:
        if test != datetime.strptime(test, "%Y-%m-%d").strftime('%Y-%m-%d'):
            #raise ValueError
            return False
        return True
    except ValueError as e:
        print(e)
        return False
    
def register(conn, cursor, email, username, password, country, dob):
    # check in app.py if dob format is correct: set Boolean variable and check for empties
    
    # check if user already exists:
    query = 'select username from users'
    cursor.execute(query)
    usernames = cursor.fetchall()
    for row in usernames:
        if username in row:
            return False        # i.e. user already exists
        
    query = 'select email from users'
    cursor.execute(query)
    emails = cursor.fetchall()
    for row in emails:
        if email in row:
            return False
    # new user, insert into database
    try:
        query1 = "insert into users "
        query2 = f"values('{email}', '{username}', '{password}', '{country}', '{dob}');"
        cursor.execute(query1+query2)
        conn.commit()
        print('User successfully added!')
        return True
    except Exception as e:
        print(e)
        print('\nData already inserted into users relation.')
        
def usernameFormat(username):
    if len(username) > 8:
        return False
    
def emailFormat(email):
    if len(email) > 35:
        return False
    sign = email[-12:] 
    if '@yahoo.com' not in sign and '@gmail.com' not in sign and '@hotmail.com' not in sign:
        return False
    return True

def passwordFormat(password):
    if len(password) > 12 or len(password) < 8:
        return 'wrong length'
    alphabet_string = string.ascii_uppercase
    caps = list(alphabet_string)
    signs = ['@', '-', '_', '$', '#']
    caps_count = 0
    signs_count = 0
    for i in range(len(password)):
        if password[i] in caps:
            caps_count += 1
        if password[i] in signs:
            signs_count += 1
    if caps_count < 1 or signs_count < 1:
        return 'missing conds'
    
    return 'correct'

        
def updatePass(conn, cursor, username, newPass):
        try:
            query = 'update users set pass = \'' + newPass + '\'' + 'where username = \'' + username + '\';'
            cursor.execute(query)
            conn.commit()
            print('Password updated!')
            return True
        except Exception  as e:
            print(e)
            return False
    
    
def belongs(conn, cursor, instance, relation):
    query = 'select * from ' + relation
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        if instance in row:
            return True
    return False

def updateEmail(conn, cursor, username, newEmail):
        try:
            query = 'update users set email = \'' + newEmail + '\'' + 'where username = \'' + username + '\';'
            cursor.execute(query)
            conn.commit()
            print('Email updated!')
            return True
        except Exception  as e:
            print(e)
            return False    
        
def deleteAcc(conn, cursor, username, password):
    try:
        query = 'delete from users where username = \'' + username + '\';'
        cursor.execute(query)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False