
# coding: utf-8

# In[107]:


import sys
import numpy as np
f = open(sys.argv[1],"r")
valx=open(sys.argv[2],"w")
polx=open(sys.argv[4],"w")
qlx=open(sys.argv[3],"w")
epoch=5
gamma=float(sys.argv[8])
lrate=float(sys.argv[7])
maxeps=int(sys.argv[6])
epsilon=float(sys.argv[9])
nepisodes=int(sys.argv[5])
alnew=0
benew=0
al=0
be=0
next ='a'
axel=0
nl=0
eps=0
cl=0
clmax=0
dirs=np.zeros((4))
op=-1
while next != (""):
    next = f.read(1)
    if next=="G" or next=="S" or next==".":
        axel=axel+1
    if(next=="\n"):
        nl=nl+1
        if(cl>clmax):
            clmax=cl
        cl=0
    else:
        cl=cl+1
# fol=np.genfromtxt(sys.argv[1],skip_header=0,delimiter="\n",dtype=None,unpack=True)
# clmax=len(fol[0])
# nl=len(fol)
f.close()
# print("number of elements in each row in maze: {}".format(clmax))
# print("number of lines in maze: {}".format(nl))
# print("number of non obstable elements: {}".format(axel))
vs=np.zeros((nl,clmax))
vsact=np.zeros((nl*clmax))
vs=np.matrix(vs)
maze1=np.chararray([nl,clmax])
vsdummy=vs
f = open(sys.argv[1],"r")
next=f.read(1)
j=0
k=0
while next != (""):
    if(next!="\n"):
        maze1[k,j]=next
        j=j+1
    if(next=="\n"):
        k=k+1
        j=0
    next=f.read(1)
qs=np.zeros((axel*4))
# print(maze1)
xn=0
yn=0
for tg in range(nl):
    for qd in range(clmax):
        if(maze1[tg,qd]=="S"):
            xn=tg
            yn=qd
def step(x,y,act):
    ist=0
    reward=-1
    xnew=0
    ynew=0
    if(act==0):
        if(y==0 or maze1[x,y-1]=="*"):
            xnew=x
            ynew=y
        else:
            xnew=x
            ynew=y-1
    if(act==1):
        if(x==0 or maze1[x-1,y]=="*"):
            xnew=x
            ynew=y
        else:
            xnew=x-1
            ynew=y
    if(act==2):
        if(y+1==clmax or maze1[x,y+1]=="*"):
            xnew=x
            ynew=y
        else:
            xnew=x
            ynew=y+1
    if(act==3):
        if(x+1==nl or maze1[x+1,y]=="*"):
            xnew=x
            ynew=y
        else:
            xnew=x+1
            ynew=y
    if(maze1[xnew,ynew]=="G"):
        ist=1
        reward=0
    return xnew,ynew,reward,ist
meps=0   
jamma=0
f.close()
al=xn
be=yn
jack=0.0
ekson=0
qlearn=np.zeros((4,nl,clmax))
for neps in range(nepisodes):
    while meps<maxeps:
#         print("hi")
#         print(al,be)
#         print("options")
#         print(qlearn[:,al,be])
        jack=np.random.uniform(0,1)
        if(jack<epsilon):
            ekson=np.random.choice([1,2,0,3])
        else:
            ekson=np.argmax(qlearn[:,al,be])
#         print(ekson)
        alnew,benew,rev,term=step(al,be,ekson)
        if(term==1):
            qlearn[ekson,al,be]=(1-lrate)*float(qlearn[ekson,al,be])+(lrate*(-1))
#             print("addon")
            meps=maxeps+1
            al=xn
            be=yn
        
        elif(term==0):
            qlearn[ekson,al,be]=(1-lrate)*qlearn[ekson,al,be]+(lrate*(-1+(gamma*np.max(qlearn[:,alnew,benew]))))
            al=alnew
            be=benew
            meps=meps+1
#         print("probo")
    meps=0
    al=xn
    be=yn     
# print(qlearn)
for joo in range(nl):
    for goo in range(clmax):
        if(maze1[joo,goo]!="*"):
            for dfl in range(4):
                qlx.write("{} {} {} {}\n".format(joo,goo,dfl,qlearn[dfl,joo,goo]))

            polx.write("{} {} {}\n".format(joo,goo,np.argmax((qlearn[:,joo,goo]))))
            valx.write("{} {} {}\n".format(joo,goo,np.max((qlearn[:,joo,goo]))))
valx.close()
polx.close()
qlx.close()

