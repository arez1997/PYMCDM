#!/usr/bin/env python
# coding: utf-8

# **welcome**

# In[1]:


#arez
print('please wait')
import pandas as pd
import numpy as np
import statistics as st
from scipy.stats import rankdata
#####@=address/file name.xlsx


file_location=input('filelocation:')
df=pd.read_excel(file_location)
x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
b=list(map(int,input('cost criteria("Ex:1 2 4 11"): ').split()))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr
print("....................weighting method....................")
arez=int(input('MIX=0,DM:1,CRITIC:2   :'))


#############################MIX##################
dmm=0
if arez==0:
    dm=np.array(list(map(float,input('DM weight  :').split())))
    dmm=float(input('DM%   :'))
    arez=int(input('another wightied method   :')) 
    dm=(dm/sum(dm))
else:
    6+6+6
     
    
######################################DM################  

if arez==1:
    arezDM=list(map(float,input('weight cr  :').split()))
    w=arezDM
    
######################CRITIC#####################    
if arez==2:
    for i in range(0,len(a)):
        maxx=max(a[i])
        minn=min(a[i])
        for j in range(0,al):
            a[i][j]=(maxx-a[i][j])/(maxx-minn)
    v=0
    n=[]
    for i in range(0,len(c)):
        maxx=max(c[i])
        minn=min(c[i])
        for j in range(0,al):
            v=c[i][j]
            n.append((v-minn)/(maxx-minn))
    c=np.array(n).reshape(cr-len(b),al)
    for i in range(0,len(a)):
        c=np.insert(c,b[i]-1,a[i],axis=0)
    #c=matrix bi bood
    std=[]
    for i in range(0,len(c)):
        std.append(st.pstdev(c[i]))
    #std=standar deviation
    rank=[]
    for i in range(0,cr):
        rank.append((rankdata(c[i], method='max')))
    rank=np.array(rank)  
    rank=int(al)-rank+1
    rank=1-abs(np.corrcoef(rank))
    m=[]
    for i in range(0,cr):
        m.append(sum(rank[i])) 
    w=np.multiply(np.array(m),std)
    w=w/sum(w)
    if dmm==0:
        print('CRITIC')
        for i in range(0,cr):
            print('W',i+1,w[i])
    elif dmm!=0:
        w=(1-dmm)*w+dmm*dm
        print('DM and CRITIC')
        for i in range(0,cr):
            print('W cr',i+1,w[i])
        for i in range(0,cr):
               print('W cr',i+1,w[i])    

    

print("........................ranking methods...................")   
#################################################################        
arez=int(input('TOPSIS:1,EDAS:2,CODAS:3,SAW:4,MOORA:5,COPRAS:6,ARAS:7,WASPAS:8,ALL:99  : '))
###############################################################
x=df.values
#########################################topsis####################    
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr


if arez==1 or arez==99:
    cc=np.zeros((cr,al))
    for i in range(0,cr):
        q=sum(x[i]**2)**.5
        cc[i]=x[i]/q
    #cc=matrix bi bood
    for i in range(0,cr):
        cc[i]=w[i]*cc[i]
    #cc=matrix bi bood mozoon
    A=[]
    AA=[]
    for i in range(0,cr):
        if i+1 in b:
            A.append(min(cc[i]))
            AA.append(max(cc[i]))
        else:
            A.append(max(cc[i]))
            AA.append(min(cc[i]))    
        #A,AA best and worst solution
 
    cc=cc.T
    Di=[]
    Dii=[]
    for i in range(0,al):
        Di.append(np.linalg.norm(cc[i]-A))
        Dii.append(np.linalg.norm(cc[i]-AA))
    #Di , Dii
  
    CCi=[]
    for i in range(0,al):
        CCi.append(Dii[i]/(Dii[i]+Di[i]))
    #CCi
   
    CCii=CCi.copy()
    print("TOPSIS")
    for i in range(0,al):
        a=max(CCi)
        o=CCii.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        CCi.remove(a)
    #ranking
    
######################################EDAS###################
x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr

if arez==2 or arez==99:
    PDA=np.zeros((cr,al))
    NDA=np.zeros((cr,al))
    ave=[]
    for i in range(0,cr):
        ave.append(np.average(x[i])) 
    
    for i in range(0,cr):
        if i+1 in b:
            for j in range(0,al):
                PDA[i][j]=max(0,ave[i]-x[i][j])/ave[i] 
        else:
            for j in range(0,al):
                PDA[i][j]=max(0,(x[i][j]-ave[i]))/ave[i]   

    for i in range(0,cr):
        if i+1 in b:
            for j in range(0,al):
                NDA[i][j]=max(0,(x[i][j]-ave[i]))/ave[i]  
        else:
            for j in range(0,al):
                NDA[i][j]=max(0,ave[i]-x[i][j])/ave[i]
    #NDA , PDA
    SP=np.zeros((cr,al))
    SN=np.zeros((cr,al))
    for i in range(0,cr):
        SP[i]=PDA[i]*w[i]
        SN[i]=NDA[i]*w[i]
    #SP , SN
    SP=SP.T
    SN=SN.T
    LSP=[]
    LSN=[]
    for i in range(0,al):
        LSP.append(sum(SP[i]))
        LSN.append(sum(SN[i]))
    #LSP , LSN
    NSP=[]
    NSN=[]

    for i in range(0,al):
        NSP.append(LSP[i]/max(LSP))
        NSN.append(1-(LSN[i]/max(LSN)))
    #NSP , NSN
    AS=[]
    for i in range(0,al):
        AS.append(0.5*(NSP[i]+NSN[i]))
    #AS
    print("EDAS")
    ASS=AS.copy()
    for i in range(0,al):
        a=max(AS)
        o=ASS.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        AS.remove(a)
    #ranking
    
    
###################################CODAS#############################
x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr

if arez==3 or arez==99:
    u=np.zeros((cr,al))
    for i in range(0,cr):
        if i+1 in b:
            for j in range(0,al):
                u[i][j]=min(x[i])/x[i][j]
        else:
            for j in range(0,al):
                u[i][j]=x[i][j]/max(x[i])

    for i in range(0,cr):
        u[i]=u[i]*w[i]
    #u=matrix bi bood mozoon
    Au=[]
    for i in range (0,cr):
        Au.append(min(u[i]))
    #Au= worst solution
    
    T=np.zeros((al,cr))
    u=u.T
    for i in range(0,al):
         T[i]=abs(u[i]-Au)
    TD=[]
    for i in range(0,al):
        TD.append(sum(T[i]))
    #TD=manhatan distance
    OD=[]
    for i in range(0,al):
        OD.append(np.linalg.norm(u[i]-Au))
    #OD=oghlidoosi distance
    M=np.zeros((al,al))

    for i in range(0,al):
        for j in range(0,al):
            if  abs(OD[i]-OD[j])< 0.02 :
                M[i][j]=OD[i]-OD[j]
            else:
                M[i][j]=(OD[i]-OD[j])+(TD[i]-TD[j])
    Hi=[]
    for i in range(0,al):
        Hi.append(sum(M[i]))
    #Hi=point of alternative
    Hii=Hi.copy()
    print('CODAS')
    for i in range(0,al):
        a=max(Hi)
        o=Hii.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        Hi.remove(a)
########################################SAW################################
x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr

if arez==4 or arez==99:
    u=np.zeros((cr,al))
    for i in range(0,cr):
        if i+1 in b:
            for j in range(0,al):
                u[i][j]=min(x[i])/x[i][j]
        else:
            for j in range(0,al):
                u[i][j]=x[i][j]/max(x[i])
    
    for i in range(0,cr):
        u[i]=u[i]*w[i]
    u=u.T
    uu=[]
    for i in range(al):
        uu.append(sum(u[i]))
    uuu=uu.copy()
    print("SAW")
    for i in range(0,al):
        a=max(uu)
        o=uuu.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        uu.remove(a)
###########################MOORA##########################
x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr

if arez==5 or arez==99:
   
    cc=np.zeros((cr-len(b),al))
    for i in range(len(c)):
        cc[i]=c[i]/sum(c[i]**2)**.5
    for i in range(len(a)):
        a[i]=-a[i]/sum(a[i]**2)**.5
    j=0
    k=0
    s=np.zeros((cr,al))
    for i in range(cr):
        if i+1 in b:
            s[i]=a[k]
            k+=1
        else:
            s[i]=cc[j]
            j+=1
       
    s=s.T
    s=s*w
    uu=[]
    for i in range(al):
        uu.append(sum(s[i]))
    uuu=uu.copy()
    print("MOORA")
    for i in range(0,al):
        a=max(uu)
        o=uuu.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        uu.remove(a)
###############################COPRAS######################

x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr

if arez==6 or arez==99:
    v=np.zeros((cr,al))
    for i in range(cr):
            if i+1 in b:
                v[i]=(-x[i]/sum(x[i]))*w[i]
            else:
                v[i]=(x[i]/sum(x[i]))*w[i]
    v=v.T
    p=[]
    n=[]
    for i in range(al):
        nn=0
        pp=0
        for j in range(cr):
            if v[i][j]>0:
                pp=v[i][j]+pp
            else:
                nn=v[i][j]+nn
        p.append(pp)
        n.append(nn)
    nnn=[]
    for i in range(al):
        nnn.append(1/n[i])
    u=[]
    for i in range(al):
        u.append(p[i]+(-sum(n)/(n[i]*sum(nnn))))
    uu=[]
    uu=u.copy()
    print("COPRAS")
    for i in range(0,al):
        a=max(u)
        o=uu.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        u.remove(a)
##############################ARAS###########################

        
x=df.values
cr=int(len(x[0]))
x=x.T
al=int(len(x[0]))
x=x.T
if arez==7 or arez==99:

    q=int(input(' for ARAS method please choose ->DM best solution:0 , auto best solution:1 '))
    
    if q==0:
        dm=list(map(float,input('best solution: ').split()))
    elif q==1:
        x=x.T
        dm=[]
        for i in range(0,cr):
            if i+1 in b:
                dm.append(min(x[i]))
            else:
                dm.append(max(x[i]))
        x=x.T
    
    
    
    p=np.zeros((al+1,cr))
    for i in range(al+1):
        if i<al:
            p[i]=x[i]
        else:
            p[i]=dm
    x=p.T
    c=x.copy()
    a=np.zeros((len(b),al+1))
    for i in range(0,len(b)):
        y=x[[b[i]-1]]
        a[i]=y
    #a= non benefit cr    
    for i in range(0,len(b)):
        c=np.delete(c,b[i]-i-1,axis=0)
    #c=benefit cr

    for i in range(cr-len(b)):
        c[i]=c[i]/sum(c[i])
    aa=np.zeros((len(b),al+1))
    for i in range(len(b)):
        for j in range(al+1):
            aa[i][j]=1/a[i][j]
    for i in range(len(b)):
        aa[i]=aa[i]/sum(aa[i])

    j=0
    k=0
    s=np.zeros((cr,al+1))
    for i in range(cr):
        if i+1 in b:
            s[i]=aa[k]
            k+=1
        else:
            s[i]=c[j]
            j+=1
        
    s=(s.T)*w
    Ui=[]
    for i in range(al+1):
        Ui.append(sum(s[i]))
    UI=[]
    for i in range(al):
        UI.append(Ui[i]/Ui[-1])
    

    B=UI.copy()
    print("ARAS")
    for i in range(0,al):
        a=max(UI)
        o=B.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        UI.remove(a)
#############################waspas########################################

x=df.values
cr=int(len(x[0]))
x=x.T
c=x.copy()
al=int(len(x[0]))
a=np.zeros((len(b),al))
for i in range(0,len(b)):
    y=x[[b[i]-1]]
    a[i]=y
#a= non benefit cr    
for i in range(0,len(b)):
    c=np.delete(c,b[i]-i-1,axis=0)
#c=benefit cr

if arez==8 or arez==99:
    u=np.zeros((cr,al))
    for i in range(0,cr):
        if i+1 in b:
            for j in range(0,al):
                u[i][j]=min(x[i])/x[i][j]
        else:           
            for j in range(0,al):
                   u[i][j]=x[i][j]/max(x[i])
    p=u.copy()
    for i in range(0,cr):
        u[i]=u[i]*w[i]
    u=u.T

    Ui1=[]
    for i in range(al):
        Ui1.append(sum(u[i]))

    for i in range(cr):
        p[i]=p[i]**w[i]
    p=p.T
    Ui2=[]
    for i in range(al):
        Ui2.append(np.prod(p[i]))
    
    UI=[]
    for i in range(al):
        UI.append(.5*(Ui1[i]+Ui2[i]))
        
    B=UI.copy()

    print("WASPAS")
    for i in range(0,al):
        a=max(UI)
        o=B.index(a)
        print(i+1,'   ','Alternativ',o+1,"      ", a)
        UI.remove(a)    
    
    
    
    
a=int(input('exit:0  '))
print('good luck')


# In[ ]:




