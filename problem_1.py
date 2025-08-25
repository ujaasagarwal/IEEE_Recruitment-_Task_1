n=int(input("enter the number of linres u want to print"))

for i in range(1 , n+1) :
    spaces=' ' *(n-i)
    stars='*' * i
    print(spaces + stars)
        
