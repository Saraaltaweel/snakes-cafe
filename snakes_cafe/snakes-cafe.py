
print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')

print('''Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears''')

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

orders=[]
order= ""
count=0
while order != "quit":
     response = input("> ")
     orders.append(response)
     count+=1
     if response == "quit":
         break
     print( f"** {orders.count(response)} order of {response} have been added to your meal **")
     
