from datetime import datetime
print("WELCOME")
print("----menu----")
print("nile")
print("club")
print("bell")
print("pil")
print("soda")
x=input("enter your choice\n:")
if x =="nile":
    price=4000
    print(f"{x}={price}")
    y=int(input("enter how many bottles:"))
    total=y*price
    print(f"total cost={total}")
elif x=="club":
    price=4000
    print(f"{x}={price}")
    y=int(input("enter how many bottles:"))
    total=y*price
    print(f"total cost={total}")

elif x=="pil":
    price=3500
    print(f"{x}={price}")
    y=int(input("enter how many bottles:"))
    total=y*price
    print(f"total cost={total}")
    

elif x=="bell":
    price=4000
    print(f"{x}={price}")
    y=int(input("enter how many bottles:"))
    total=y*price
    print(f"total cost={total}")

else :
    price=3000
    print(f"{x}={price}")
    y=int(input("enter how many bottles:"))
    total=y*price
    print(f"total cost={total}")

print(datetime.now())