import pickle
import datetime
f1=open("E://dates.bin","rb")
#dt=[]
#dt=pickle.load(f1)

f=open("E://parsed1.bin","rb")
wrd=pickle.load(f)
f.close()
i=0
while True:
    dt=pickle.load(f1)
    if datetime.datetime.date(datetime.datetime.now())==dt:
        break
    else:
        i+=1
print("Word for Today is : " ,wrd[i])
f1.close()

input("Press Any Key to Close")
