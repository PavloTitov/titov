a=[2,45,-2,77,16,3.14,8,10,10,2]
b=[4,56,-2,77,10,8.9,-99,-2]
c=[]        
for i in a:
    for j in b:
        c=a+b
print(c)
a=[2,45,-2,77,16,3.14,8,10,10,2]
b=[4,56,-2,77,10,8.9,-99,-2]
c=list(set(a+b))
print(c)
a=[2,45,-2,77,16,3.14,8,10,10,2]
b=[4,56,-2,77,10,8.9,-99,-2]
c=[]        
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)  
a=[2,45,-2,77,16,3.14,8,10,10,2]
b=[4,56,-2,77,10,8.9,-99,-2]
c=[]
for i in a:
    for j in b:
        if i!=j:
            c=set(a+b)
print(c)  
a=[2,45,-2,77,16,3.14,8,10,10,2]
b=[4,56,-2,77,10,8.9,-99,-2]
c=[min(a),max(a),min(b),max(b)]        
print(c)