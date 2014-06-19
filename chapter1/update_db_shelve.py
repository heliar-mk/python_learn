from initdate import tom
import shelve
db=shelve.open('people-shelve')
sue=db['sue']
sue['pay']*=1.50
db['tom']=tom
db['sue']=sue
db.close()