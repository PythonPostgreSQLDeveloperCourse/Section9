'''
'''
from database import Database
import user

'''
u = user.User('jonas@cghijinks.com', 'Jonas', 'Avrin', None)

print(u)
# <User jonas@cghijinks.com>

# add user to postgresql
u.save_to_db()
'''

uname, pwd = 'postgres', '#N1#Gkq7yWkjnE#H'
# we choose when we want to initialize the database
Database.initialise(minconn=1, maxconn=10, user=uname, password=pwd,
					database='udemy-learning', host='localhost')

# retrieve user info from database and create a User instance
u = user.User.load_from_db_by_email('jonas@cghijinks.com')
print(u)
# <User jonas@cghijinks.com>
