import datetime
from tinydb import TinyDB, where
db = TinyDB('./todo.db.json')
#db.insert({'id': 1, 'task': 'Read A-byte-of-python to get a good introduction into Python', 'status': '0'})
#db.insert({'id': 1, 'task': 'Read A-byte-of-python to get a good introduction into Python', 'status': '0', 'priority': 10})
#db.update({'task': 'Its working now'}, eids=[3])
#db.remove({eids=[1, 2])
#rows = db.get(where('priority') == 10)
#rows = db.get(('task'), where('priority') == 10)
#rows = db.search(where('id'))
start = datetime.datetime.now()
for x in range(0, 1000):
	db.insert({'id': 1, 'task': 'Read A-byte-of-python to get a good introduction into Python', 'status': '0'})
	db.insert({'id': 1, 'task': 'Read A-byte-of-python to get a good introduction into Python', 'status': '0', 'priority': 10})
end = datetime.datetime.now()
exc_time = end - start
print ("Execution time : ", exc_time)

stime = datetime.datetime.now()
rows = db.search(where('id'))
etime = datetime.datetime.now()
total_time = etime - stime
print ("Fecthing time : ",  total_time)
count = db.count(where('id'))
print (count)

#import sqlite3
#import datetime
#con = sqlite3.connect('homework_sqlite.db')
#cursor = con.cursor()

#start = datetime.datetime.now()
#for x in range(0, 10000):
#con.execute("CREATE TABLE Homework (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
#	con.execute("INSERT INTO Homework (task,status) VALUES ('Finish software testing Homework',0)")
#	con.execute("INSERT INTO Homework (task,status) VALUES ('Finished SQlite part',1)")
#con.commit()
#end = datetime.datetime.now()
#exc_time = end - start
#print ("Execution time : ", exc_time)

#stime = datetime.datetime.now()
#cursor.execute("select * from Homework")
#rows = cursor.fetchall()
#etime = datetime.datetime.now()
#total_time = etime - stime
#print ("Fecthing time : ",  total_time)
#cursor.execute("select COUNT(*) from Homework")
#count = cursor.fetchall()
#print (count)
	
#con.execute("INSERT INTO Homework (task,status) VALUES ('Finish software testing Homework',1)")
#con.execute("ALTER TABLE Homework ADD priority INTEGER")
#con.execute("DELETE FROM Homework")
# Show the results before update
#print ('\nBefore update:')
#cursor.execute("select * from Homework where id = 1")
#rows = cursor.fetchall()
#print (rows)
#try:
#	con.execute("UPDATE Homework set status = 0 where id = 1")
#	cursor.execute("select * from Homework where id = 1")
#	print ('\nAfter update:')
#	rows = cursor.fetchall()
#	print (rows)
	# Pretend the processing caused an error
#	raise RuntimeError('simulated error')
#except Exception :
#	print ('ERROR: simulated error' )
#	con.rollback()
#else:
#	con.commit()
	
# Show the results after rollback
#print ('\nAfter rollback:')
#cursor.execute("select * from Homework where id = 1")
#rows = cursor.fetchall()
#print (rows)