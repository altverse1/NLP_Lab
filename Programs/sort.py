#CiperSquad
def f(l,n):
   for i in range(n):
      for j in range(n-i-1):
         if l[j]>l[j+1]:l[j],l[j+1]=l[j+1],l[j]
   print(l)  

if __name__=='__main__':
   lst=[53,7,4,42,6,7]
   f(lst,len(lst))