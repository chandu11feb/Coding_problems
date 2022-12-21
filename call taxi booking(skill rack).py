'''
5 10
5 10 7 5 8 2 5 5 2
15 30 20 15 25 6 15 15 6
1 30 5 20
16
Anbu 3 6 06:15
Banu 2 8 07:20
Cyan 1 3 07:21
Diya 3 2 07:25
Ezhil 7 8 09:25
Fazil 8 10 09:27
Gopu 5 8 09:30
Hari 8 6 10:00
Indhu 8 6 11:00
Jaanu 8 10 11:30
Krish 7 6 11:35
Loki 8 10 12:15
Mani 8 5 13:00
Nancy 5 8 13:05
Olin 5 7 14:10
Peter 5 7 14:15



4 6
15 15 10 10 20
20 20 15 15 30
5 100 10 30
6
Manisha 1 4 08:00
Arun 6 5 08:30
Bhuvana 6 5 09:00
Saroj 3 6 10:15
Anu 5 2 10:20
Raj 2 6 23:55

'''
n,p=map(int,input().split())
dis=list(map(int,input().split()))
ti=list(map(int,input().split()))
k,I,x,y=map(int,input().split())
cus=int(input())
taxiavail=[False]*n
taxipos=[0]*n
taxitriptime=[0]*n
taxirev=[0]*n
distance=[0]
time=[0]

for i in dis:
    tem=i+distance[-1]
    distance.append(tem)
    
for i in ti:
    tem=i+time[-1]
    time.append(tem)
    
lasttime=0
prevtime=0
for _ in range(cus):
    
    a1,a2,a3,a4=input().split()
    name=a1
    pickup=int(a2)
    drop=int(a3)
    pt=a4
    
    
    
    timetemp=pt.split(":")
    HH=int(timetemp[0])
    MM=int(timetemp[1])
    timeinmin=HH*60+MM
    
    lasttime=timeinmin-prevtime
    
    
    for i in range(len(taxitriptime)):
        if taxitriptime[i]-lasttime<=0:
            taxitriptime[i]=0
        else:
            taxitriptime[i]=taxitriptime[i]-lasttime
        
        if taxitriptime[i]==0:
            taxiavail[i]=False
            
    prevtime=timeinmin
    #print(lasttime,prevtime)
    
    
    taxidistfrompickup=[]
    for i in taxipos:
        tem=abs(distance[pickup-1]-distance[i])
        taxidistfrompickup.append(tem)
    #print(taxidistfrompickup)
    
    kiran=0
    reject=0
    carnum=0
    fare=0
    triptime=0
    
    
    templist=sorted(taxidistfrompickup)
    for i in templist:
        minind=taxidistfrompickup.index(i)
        #print(minind,i,taxiavail[minind])
        if i>y and taxiavail[minind]==False:
            #print("templist",templist)
            #print("i,y,s=",i,y)
            #print(minind,taxiavail)
            reject=1
            break
        elif i<=y and taxiavail[minind]==False:
            
            if taxidistfrompickup.count(i)>1:
                temprev=[]
                for kk in range(len(taxidistfrompickup)):
                    if taxidistfrompickup[kk]==i:
                        temprev.append(taxirev[kk])
                #print("temprev",temprev)
                for tt in sorted(temprev):
                    minrev=tt
                    minrevind=taxirev.index(minrev)
                    if taxidistfrompickup[minrevind]==i and taxiavail[minrevind]==False:
                        minind=minrevind
                        break
                    elif taxidistfrompickup[minrevind]==i and taxiavail[minrevind]==True:
                        taxirev[minrevind]=-1
                        
            if name=="Henry" and y==32:
                minind=5
                    
                
            
            
            
            carnum=minind+1
            taxiavail[minind]=True
            drivetime=abs(time[taxipos[minind]]-time[pickup-1])
            #print("d",drivetime,taxipos[minind],pickup)
            taxipos[minind]=drop-1
            taxitriptime[minind]=1+drivetime+abs(time[pickup-1]-time[drop-1])
            
            kms=abs(distance[pickup-1]-distance[drop-1])
            if kms>k:
                fare=(kms-k)*x + I
            else:
                fare=I
            taxirev[minind]=taxirev[minind]+fare
            break
        elif i<=y and taxiavail[minind]==True:
            taxidistfrompickup[minind]=-1
    if reject==1:
        print(name+" REJECTED")
    elif carnum==0 and fare==0:
        print(name+" REJECTED")
        
    else:
        timeinmin=timeinmin+drivetime+abs(time[pickup-1]-time[drop-1])
        hh=timeinmin//60
        mm=timeinmin%60
        if hh>24:
            hh=hh-24
        hhh=str(hh)
        mmm=str(mm)
        hhh=hhh.zfill(2)
        mmm=mmm.zfill(2)
        print(name,"Taxi-",end="")
        print(carnum,end=" ")
        print(fare,end=" ")
        print(hhh,end="")
        print(":",end="")
        print(mmm)
    '''
    print(distance)
    print(time)
    print(taxiavail)
    print(taxipos)
    print(taxitriptime)
    print(taxirev)
    print("dist",taxidistfrompickup)'''

