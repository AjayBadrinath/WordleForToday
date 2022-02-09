import pickle
##f=open("E://parsed.bin","rb")
##list1=pickle.load(f)
from datetime import date,timedelta
start=date(2021, 6, 19)
f=open("parsed1.bin","rb")
x=pickle.load(f)
f.close()

end=start+timedelta(len(x))
l=[]
f=open("dates.bin","wb")
def tim(s,end):
    for i in range(int((end-s).days)):
                   pickle.dump(s+timedelta(i),f)
                   
tim(start,end)
f.close()
