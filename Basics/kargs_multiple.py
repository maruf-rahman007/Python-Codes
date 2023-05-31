# def making_kargs(first , last , title , **additional):
#     for key,value in additional.items():
#         print(key , value)
# making_kargs('Rafim','Rabby','Coder boy','Magibaz','Magi')

balance = 3000
def buying(item,price):
    global balance 
    balance = balance - price
    print(balance)

buying('iPhone',999)