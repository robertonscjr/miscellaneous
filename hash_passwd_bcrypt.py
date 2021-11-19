import time                         
import bcrypt                       
                                    
passwd = b's$cret12'                
                                    
salt = bcrypt.gensalt(rounds=16)    
                                    
start = time.time()                 
hashed = bcrypt.hashpw(passwd, salt)
end = time.time()                   
                                    
print(end - start)                  
print(salt)                         
print(hashed)                       
                                    
if bcrypt.checkpw(passwd, hashed):  
    print("match")                  
else:                               
    print("does not match")
