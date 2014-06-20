#interactive queries
import shelve

fliedname=('name','age','pay','job')
maxflied=max(len(f) for f in fliedname)
dbfile=shelve.open('class-shelve')

while True:
    key=input('\nkey=>')
    if not key:
        break
    try:
        record=dbfile[key]
    except:
        print('No such key "%s"' % key)
    else:
        for flied in fliedname:
            print(flied.ljust(maxflied),'=>',getattr(record,flied))

dbfile.close()