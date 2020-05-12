pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False



list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,23]
n=23
if search(list,n):
    print("found",pos)
else:
    print("not found")