Q=input("Give the name of the file")
with open(Q,"r") as af:
    asciiv=f.read()

counter=0
i=0
j=3
words=[]
chars=[]

  for l in len(asciiv)

      if chr(int(ascii[i:j]))!=" " :

          chars[counter]+=1
          words[counter]+=chr(int(ascii[i:j]))
          i=j
          j+=3
          ascii+=ascii[j:]

    else:
        counter+=1


for x in range(counter)
    if x%2=0 :
        print(words[x],":",chars[x])
        print(words[x+1]),":",chars[x+1])
