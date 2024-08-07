print("--------------------------------")
print("            APP MENU            ")
print("--------------------------------")
print("Press 0 for creating new list")
print("Press 1 for adding element into the list")
print("Press 2 for reading element from the list")
print("Press 3 for deleting last element from the list")
print("Press 4 for adding element at specific index")
print("Press 5 for deleting specific element of the list")
print("Press 6 to Exit")


x=''
list=list(x)
while True:
 
    ch=int(input("Enter your choice:"))
    if ch==0:
        print(list)
        print("Empty List is created")
    elif ch==1:
        a=int(input("Enter element to add in a list:"))
        list.append(a)
        print(list)
    elif ch==2:
        print("Reading element as follows:")
        print(list) 
    elif ch==3:
        y=[]
        if list==y:
            print("list is empty")
        else:    
            a=list.pop()
            print("Last element deleted",a) 
            print(list)
    elif ch==4:
        i=int(input("Enter the index no."))
        e=int(input("Enter the element to be added:")) 
        list.insert(i,e) 
        print(list)
    elif ch==5:
        no=int(input("Enter the number to be deleted:"))
        list.remove(no)
        print(list) 
    elif ch==6:
        print("Exiting!!")
        break   
    else:
        print("Enter valid choice")

    