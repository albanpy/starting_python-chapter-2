a=int(input("Enter price of Item 1:"))
b=int(input("Enter price of Item 2:"))
c=int(input("Enter price of Item 3:"))
d=int(input("Enter price of Item 4:"))
e=int(input("Enter price of Item 5:"))
subtot=a+b+c+d+e
tax=subtot*0.07
total=subtot+tax
print(f'The subtotal of the sale={subtot:,}')
print(f'The amount of sales tax={tax:,.2f}')
print(f'The Total amount of sales={total:,.2f}')
