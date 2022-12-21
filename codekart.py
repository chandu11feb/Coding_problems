t=int(input())
for i in range(t):
    smcost=[0,0]
    smquan=[0,0]
    cquan=[0,0]
    avail=[False,False]
    cavial=[False,False]
    e="END"
    sm="SM"
    while(1):
        x=input().split()
        print(x)
        if x[0]=="END":
            break
        elif x[1]==sm:
            if x[2]=='ADD':
                itemnm=x[3]
                itemq=int(x[4])
                if itemq > 0 :
                    if itemnm=="SHIRT" and avail[0]==False:
                        avail[0]=True
                        smquan[0]+=itemq
                        print(itemq)
                    elif itemnm=="SHOE" and avail[1]==False:
                        avail[1]=True
                        smquan[1]+=itemq
                        print(itemq)
                    else:
                        print("-1")
                else:
                    print("-1")
            elif x[2]=="REMOVE":
                itemnm=x[3]
                if itemnm=="SHIRT":
                    avail[0]=False
                    if smquan[0]>0:
                        smquan[0]=0
                        print('1')
                    else:
                        print("-1")
                elif itemnm=="SHOE":
                    avail[1]=False
                    if smquan[1]>0:
                        smquan[1]=0
                        print('1')
                    else:
                        print("-1")
                else:
                    print("-1")
            elif x[2]=="GET_QTY":
                itemnm=x[3]
                if itemnm=="SHIRT":
                    print(smquan[0])
                elif itemnm=="SHOE":
                    print(smquan[1])
            elif x[2]=="INCR":
                itemnm=x[3]
                itemq=int(x[4])
                if itemnm=="SHIRT":
                    if avail[0]==True:
                        if itemq>0:
                            smquan[0]+=itemq
                        print(itemq)
                    else:
                        print("-1")
                elif itemnm=="SHOE":
                    if avail[1]==True:
                        if itemq>0:
                            smquan[1]+=itemq
                        print(itemq)
                    else:
                        print("-1")
                else:
                    print("-1")
            elif x[2]=="DCR":
                itemnm=x[3]
                itemq=int(x[4])
                if itemnm=="SHIRT" and avail[0]==True:
                    dec=smquan[0]-itemq
                    if dec>0:
                        smquan[0]=dec
                        print(itemq)
                    else:
                        print("-1")
                elif itemnm=="SHOE" and avail[1]==True:
                    dec=smquan[1]-itemq
                    if dec>0:
                        smquan[1]=dec
                        print(itemq)
                    else:
                        print("-1")
                else:
                    print("-1")
            elif x[2]=="SET_COST":
                itemnm=x[3]
                cost=int(x[4])
                if itemnm=="SHIRT":
                    smcost[0]=cost
                    print(float(cost))
                elif itemnm=="SHOE":
                    smcost[1]=cost
                    print(float(cost))
                else:
                    print("-1")
            else:
                print("-1")
        elif x[1]=="S":
            if x[2]=="ADD":
                itemnm=x[3]
                itemq=int(x[4])
                if itemnm=="SHIRT" and avail[0]==True:
                    cquan[0]+=itemq
                    cavial[0]=True
                    print(itemq)
                elif itemnm=="SHOE" and avail[1]==True:
                    cquan[1]+=itemq
                    cavial[1]=True
                    print(itemq)
                else:
                    print("-1")
            elif x[2]=="REMOVE":
                itemnm=x[3]
                if itemnm=="SHIRT" and cavial[0]==True:
                    cquan[0]=0
                    print("1")
                    cavial[0]=False
                elif itemnm=="SHOE" and avail[0]==True:
                    cquan[1]=0
                    print("1")
                    cavial[1]=False
                else:
                    print("-1")
            elif x[2]=="INCR":
                itemnm=x[3]
                itemq=int(x[4])
                famt1=cquan[0]+itemq
                famt2=cquan[1]+itemq
                if itemnm=="SHIRT" and cavial[0]==True:
                    if itemq>0 and famt1 <= smquan[0]:
                        cquan[0]+=itemq
                        print(itemq)
                    else:
                        print("-1")
                elif itemnm=="SHOE" and cavial[1]==True:
                    if itemq>0 and famt2 <= smquan[1]:
                        cquan[1]+=itemq
                        print(itemq)
                    else:
                        print("-1")
                else:
                    print("-1")
            elif x[2]=="DCR":
                itemnm=x[3]
                itemq=int(x[4])
                dec1=cquan[0]-itemq
                dec2=cquan[1]-itemq
                if itemnm=="SHIRT" and cavial[0]==True:
                    if itemq>0 and dec1>0:
                        cquan[0]=dec1
                        print(itemq)
                    else:
                        print("-1")
                elif itemnm=="SHOE" and cavial[1]==True:
                    if itemq>0 and dec2>0:
                        cquan[1]=dec2
                        print(itemq)
                    else:
                        print("-1")
                else:
                    print("-1")
            elif x[2]=="GET_ORDER_AMOUNT":
                total=0
                if cavial[0]==True and cavial[1]==True:
                    total+=cquan[0]*smcost[0]
                    total+=cquan[1]*smcost[1]
                    print('%.2f'%total)
                elif cavial[0]==True:
                    total+=cquan[0]*smcost[0]
                    print('%.2f'%total)
                elif cavial[1]==True:
                    total+=cquan[1]*smcost[1]
                    print('%.2f'%total)
                else:
                    print("-1")
            else:
                print("-1")
        else:
            print("-1")