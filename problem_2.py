number=int(input("enter number of words u want to type"))
word_list=[]
c=0 

for i in range(1,number+1):
    word=input("enter the words\n")
    word_list.append(word)
def palindrome(word) :
    if word == word[::-1]:
        return 1
    else:
        return 0
    
for i in range(0 , len(word_list)):
    if palindrome(word_list[i])==1:
        print(f"{word_list[i]} is a palindrome")
        c=c+1
if c==0:
    print("0")

        

    
