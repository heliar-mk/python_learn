#interactive updates

import shelve
from person import Person

fliedname=('name','age','pay','job')
dbfile=shelve.open('class-shelve')

while True:
    key=input('\nkey=>')
    if not key:
        break
    if key in dbfile:
        record=dbfile[key]
    else:
        record=Person(name="?",age='?',pay="?")
    print("Notice!\nThe added name and job values must be string!")
    for flied in fliedname:
        currattr=getattr(record,flied)
        new_value=input("[%s]=%s\n\tnew=>? " %(flied,currattr))
        if new_value:
            setattr(record,flied,eval(new_value))               #用这个函数设置属性值比较方便
            dbfile[key]=record
dbfile.close()