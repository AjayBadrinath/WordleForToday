import pickle

f=open("E://wordle.txt","r")
def val():
    global maxval
    maxval=int(f.seek(0,2)/8)
    maxvaldup=maxval
val()
f.seek(1)
l=[]
l.append(f.read(5))
f.seek(9)
l.append(f.read(5))
i=0
while True:
    if i<=maxval:
        f.seek(f.tell()+3)
        l.append(f.read(5))
        print(l[i])
        i+=1
        #print(i,"Words have been updated")
    else:
        f.close()
        break
l.pop()
l.pop()
f=open("parsed1.bin","wb")
pickle.dump(l,f)
f.close()
print(l[0],l[1])
import date
