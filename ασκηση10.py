import deque

   def depth(x):

       queue=deque([id(x),x,1])
       memo=set()

        while queue:
            id_,y,level=queue.popleft()
            if id_ in memo:
                continue
            memo.add(id_)

            if isinstance(y,dict):
                queue+=((id(z),z,level+1) for z in y.values())
        return level

Q=input("Give the name of the file")        
file=open(Q,"r")
       data=file.read()
       dict=ast.literal_eval(data)


print(depth(dict))
