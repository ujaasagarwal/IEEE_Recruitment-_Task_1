List_1= [3, 4, 5, 1, 4, 6, 1, 7, 7]
List_2= [5, 8, 2, 9, 9, 4, 6, 3]
final_list=[]

for i in range(0 , len(List_1)):
    if List_1[i] in List_2:
        if List_1[i] not in final_list:
            final_list.append(List_1[i])
        
print(f"the intersection is {final_list}")