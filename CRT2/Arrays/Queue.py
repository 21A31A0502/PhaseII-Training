def enQue(Q,ele):
    Q.append(ele)
def deQue(ele):
    if len(Q)==0:
        return 0
    Q.pop(0)
    
    




Q=[]
enQue(Q,10)
enQue(Q,20)
enQue(Q,30)
enQue(Q,40)
enQue(Q,50)
enQue(Q,60)
print(Q)
deQue(Q)
deQue(Q)
deQue(Q)
deQue(Q)
print(Q)