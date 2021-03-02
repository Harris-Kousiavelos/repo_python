List=[]

Q=input("Give the name of the file")
f = open(Q,"r")
data=f.read()
f.close()

while len(data)!=1:

    if data[0]+data[1]=="{\"" or (data[0]+data[1])==",\"" or (data[0]+data[1])=="{\'" or (data[0]+data[1])=="{'":
        x=data.find(":")
        y=data[:x]
        List.append(y[2:-1])
        data=data[x:]
    else:
        data=data[1:]
