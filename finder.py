import time
password="200"
print("cracking password please wait.............")
for i in range (1000):
     guess=str(i).zfill(3)
     #print("trying",guess)
     time.sleep(0.05)
     
     if guess==password:
         print("password found 😎")
         print("password is :",guess)
         break