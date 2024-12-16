print(50*"=")
print("Welcome to my skincare shop".center(40))
print(50*"=")

item_dict={"Facial Mist":[40,1200],
           "Face Cleanser":[50,1200],
           "Toner":[40,1000],
           "Moisturizer":[30,1000],
           "Sunscreen SPF 50":[60,1800],
           "Serum - Vitamin C":[25,2400],
           "Eye Cream":[20,2000],
           "Night Cream":[35,2000],
           "Sheet Mask":[100,300],
           "Exfoliating Scrub":[45,1400],
           "Lip Balm":[70,500],
           "Clay Mask":[40,1200],
           "Makeup Remover Wipes":[90,200],
           "Micellar Water":[50,300],
           "Face Oil":[25,500],
           "Anti-Acne Gel":[30,1200],
           "Brightening Cream":[35,2000],
           "Aloe Vera Gel":[60,600],
           "Hand Cream":[50,800],
           "Foot Cream":[30,1000],
           "Body Lotion":[40,1800],
           "Charcoal Mask":[45,300],
           "Rose Water Mist":[50,900],
           "Retinol Cream":[30,1200],
           "Anti-Wrinkle Serum":[20,3000],
           "Body Scrub":[35,1800],
           "Hair Removal Cream":[50,700],
           "Nail Cuticle Oil":[40,800],
           "Lip Scrub":[55,600],
           "Collagen Face Mask":[120,400],
           "Whitening Cream":[30,1200],
           "Spot Corrector":[20,1800],
           "Cleansing Oil":[40,2000],
           "Hydrating Mist":[50,1400],
           "Body Butter":[25,2200],
           "Tinted Moisturizer":[30,1800],
           "After-Sun Lotion":[40,1200],
           "Pore Minimizer":[20,2000],
           "Skin Brightening Serum":[25,800],
           "Face Mask - Tea Tree":[100,200],
           "Blackhead Remover":[30,180.50],
           "Hydrating Gel":[35,320.75],
           "Anti-Aging Mask":[90,500],
           "Blemish Balm (BB Cream)":[25,2200],
           "CC Cream":[30,2500],
           "Whitening Body Wash":[40,1400],
           "Face Wash Neem":[50,600],
           "Anti-Dandruff Lotion":[30,1500],
           "Hydrating Face Gel":[25,1000],
           "Spot Lightening Gel":[20,1300]}



         
def show_dict():
    print(50*"=")
    print("Available items and quantity")
    print(50*"=")
    for x in item_dict:
        print(x,(23-len(x))*" ",
              (14-len(str(item_dict[x][0])))*" ",
                     item_dict[x][0])
    print(50*"-")
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

    print(50*"=")
    
    print ("**payment receipt**".center(40))
    print (50*"=")
    print ("item",12*" ","quant."," ","u.price",6*" ","s.total")
    tprice=0
    for x in demand_list:
          tprice+=x[3]
          print (x[0].title(),(15-len(x[0]))*" ",
                 (5-len(str(x[1])))*" ",x[1],
                 (9-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
                 (13-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
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

f=open("D:/New folder/data01.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.close()
