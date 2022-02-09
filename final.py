import pickle
import datetime

f1=open("E://dates.bin","rb")
#dt=[]
#dt=pickle.load(f1)
x=input("Enter date in order (dd/mm/yy)")
d_conv=datetime.datetime.strptime(x,"%d/%m/%y")
f=open("E://parsed1.bin","rb")
wrd=pickle.load(f)
f.close()
i=0
while True:
    dt=pickle.load(f1)
##    if datetime.datetime.date(datetime.datetime.now())==dt:
##        break
    if datetime.datetime.date(d_conv)==dt:
        break
    else:
        i+=1
print("Word for",x, "is : " ,wrd[i])
f1.close()
##x=eval(input("Enter date in order (yyyy-mm-dd)"))

input("Press Any Key to Close")
