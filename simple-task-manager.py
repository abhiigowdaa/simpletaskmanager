checklists=[]
completed_task=[]
incomplete_task=[]

print("enter the task(type 'end' if task done): \n")
while True:
    items=input(">>")
    if items.lower()=='end':
        break
    checklists.append(items)

print("did you complete the work(yes/no)")    
for items in checklists:
    answer=input(f"did you complete '{items}'? ").lower()
    if answer=="yes":
        completed_task.append(items)
    else:
        incomplete_task.append(items)
print("----results completed----\n")
print("completed taskes: \n")
if completed_task:
     for items in completed_task:
         print(">>",items)
else:
    print("NO TASKS!! \n")
print("incomplete tasks: \n")   
if incomplete_task:
    for items in incomplete_task:
       print(">>",items)       
else:
    print("NO TASKS!! \n")      
