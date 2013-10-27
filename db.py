import psycopg2
import sys


con = None
'''con = psycopg2.connect(database='a') 
cur = con.cursor()
cur.execute("create table posts(title TEXT,text INT)")
con.commit()
con.close()
'''

con = psycopg2.connect(database='a') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS posts")
cur.execute("CREATE TABLE posts(id  serial,title TEXT,text TEXT)")
#	cur.execute("insert into posts (title, text) values ('sdfsff','fhjfjjj')")
con.commit()
con.close()
#	cur.execute("create table posts(title TEXT,text INT)")
#except psycopg2.DatabaseError, e:
#    	print 'Error %s' % e    
#    	sys.exit(1)
    
    
#finally:
#    
#    	if con:
#       	con.close()
#	cur.executemany("INSERT INTO sale VALUES(?,?)",[a['title'],a['text']])

