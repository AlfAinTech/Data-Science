
import pandas as pd
import enchant
import sqlite3

d=enchant.Dict("en_US")

conn = sqlite3.connect('Z:\Data Science Internship\Data Sciences\SQLite Files\items.sqlite')
c = conn.cursor()

c.execute('Select * from items')

print(pd.read_sql_query('Select * from items',conn))
print ('/////////////////////Above is the database taken////////////////////')
x=0
id=1
for col in c.fetchall():

    id=col[1]
    if(col[0]==''):

        #print('this is the id :'+ str(id))
        x=x+1
        if(x>0):
         #print('user entered : '+str(input('Database has empty cell at id '+str(id)+' please enter a value: ')))
         y=str(input('Database has empty cell at id '+str(id)+' please enter a value: '))
         c.execute("UPDATE items SET items_name ='"+y+"' where id="+str(id))
    else:
         if(d.check(col[0])):
             print(str(id)+':'+col[0]+' is a correct word')
         else:
            print(str(id)+':'+col[0] + ' is a mispelled following are the correct sugesstion :')
            print(d.suggest(col[0]))
            c.execute("UPDATE items SET items_name ='" + d.suggest(col[0])[0] + "' where id=" + str(id))
            print('Program changed '+col[0]+' to '+d.suggest(col[0])[0]+' at id'+str(id))


conn.commit()
  







