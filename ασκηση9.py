Q=input("Give the name of the file")
with open(Q) as f:
    data=f.read()

data=data.replace(" ","") #afairw ta kena
data=data.replace("\n","") #afairw tis kenes grammes
star="*"
listchar=[]
liststars=[]

   for char in data:
       if (ord(char)%2!):
           if char in listchar:
               index=listchar.index(char)
               liststars[index]+=1
           else:
               liststars.append(1)
               listchar.append(char)

for j in listchar:
    result= star * liststars(j)
    print(listchar(j),":","result")+
