item_dict={}
f = open("D:/Hridita/data01.txt","r")

while True:
    item = f.readline()
    if item == '':
        break 
    quantity = f.readline()
    uprice = f.readline()
    item = item[:len(item)-1]
    quantity = int(quantity[:len(str(quantity))-1])
    uprice = float(uprice[:len(str(uprice))-1])
    item_dict[item]=[quantity,uprice]
f.close()

def show_dict():
    print(30*"=")
    print("Available items and quantity")
    print(30*"=")
    for x in item_dict:
        print(x,(15-len(x))*" ",
              (6-len(str(item_dict[x][0])))*" ",
                     item_dict[x][0])
    print(30*"-")
#show_dict()  
def dec_quant(key,val):
    item_dict[key][0]-=val
def inc_quant(key,val):
    item_dict[key][0]+=val
def receive_order():
    print("order received:")
    while True:
        item = input("Items(x to stop):")
        if item =="x":
            break
        value =int (input("Quantity:"))
        if item not in item_dict:
            print("new item found!")
            uprice = float (input("unit price:"))
            item_dict[item]=[value,uprice]
            continue
        inc_quant(item,value)

    #show_dict()
def process_demand():
    print("input demand:")
    demand_list = []

    while True:
        item = input("Items(x to stop):")
        if item =="x":
            break
        if item not in item_dict:
            print(f"the item '{item}' is not available")
            continue
        value =int (input("Quantity:"))
        if value>item_dict[item][0]:
            print(f"Total of {item_dict[item][0]} quantity are available")
            continue
        dec_quant(item,value)
        demand_list+=[item,value,
                      item_dict[item][1],
                      value*item_dict[item][1]],
#printing the payment receipt

    print(40*"=")
    
    print ("**payment receipt**".center(40))
    print (40*"=")
    print ("item",7*" ","quant."," ","u.price",2*" ","s.total")
    tprice=0
    for x in demand_list:
          tprice+=x[3]
          print (x[0].title(),(11-len(x[0]))*" ",
                 (5-len(str(x[1])))*" ",x[1],
                 (8-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
                 (9-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print (40*"-")
    print ("Total Price:"," ",tprice)
    #print (demand_list)
    #show_dict()
    
#show_dict()
while True:
    show_dict()
    print ("choose an option:")
    print ("Type '1':To process demand")
    print ("type '2':To receive order")
    print ("Type '3':To exit the program")
    choice = input ("Choice:")
    if choice =='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
        break
    else:
        continue