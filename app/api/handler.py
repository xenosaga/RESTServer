from .user import user
from .admin import admin

usr = user('bbl')
adm = admin()

def query():
    pass

def delete():
    pass

def modify():
    pass

def add():
    pass

def process(post_data):
    if(post_data['usr_id'] == 'admin'):
        print('admin mode')
    else:
        print('user mode')
        print(post_data)
        res = usr.process(post_data)
        print('----------result-----------')
        print(res)
        print('---------------------------')
    pass

