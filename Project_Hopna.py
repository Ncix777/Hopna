strt=1
Dict={}
credit={}
list_cus=[]
temp_lis=[]
p_bought={}
amount=0
print("!Only to maintain Customer Data: ")
while strt==1:
    tot_bill=0
    nam=input("Enter Customer Name: ")
    shop=int(input("Enter No. Product Purchased: "))
    list_cus.append(nam)
    temp={}
    for i in range(shop):
        item=input("Enter Product Name: ")
        quan=int(input("Enter Quantity: "))
        price=int(input("Enter Price: "))
        temp[item]=[quan,price]
        temp_lis.append(temp)
        tot_bill+=price
    else:
        print(nam,"Total Bill Is",tot_bill)
        if tot_bill>0:
            amount=int(input("Enter The Amount Paid By Customer: "))
        bal=tot_bill-amount
        if bal>0:
            print("Customer",nam," Have To Pay Rs: ",bal)
            credit[nam]=[bal]
        else:
            print("Fully Paid")
    strt=int(input("\nEnter Choice\n1.Another Customer\n2.Exit\n"))
for i in range(len(list_cus)):
    p_bought[list_cus[i]]=[temp_lis[i]]
q=int(input("Do You Have Another Query\n1.Yes\n2.No Exit\n"))
while q==1:
    qes=int(input("1.List Of People Who Have Credited\n2.All Customer List\n3.Customer List With Product\n"))
    if qes==1:
        if len(credit)>=1:
            for i in credit.items():
                print(i)
            choice=int(input("1.To Pay\n2.Continue\n"))
            if choice==1:
                nam=input("Enter Name Of Customer: ")
                if nam in credit:
                    amount=int(input("Enter Amount Paid: "))
                    for i in credit[nam]:
                        cre=i-amount
                    if cre<=0:
                        del credit[nam]
                    else:
                        credit[nam]=[cre]
                else:
                    print("Customer Not in Credit")
            else:
                pass
        else:
            print("No Customer Has Credited")
    elif qes==2:
        print(list_cus)
    elif qes==3:
        for i in p_bought.items():
            print(i)
    q=int(input("Do You Have Another Query\n1.Yes\n2.No Exit\n"))

