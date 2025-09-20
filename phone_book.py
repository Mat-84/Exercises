#menu
print("="*15,"Contact book","="*15)
print("\n1.Add contact\n2.Search contact\n3.Delete contact\n4.View All contacts\n5.Exit\n")
print("="*15)

#contacts-dict
contacts = {}

#add_contact
def add(contact,num):
    contacts[contact] = num

#search_contact
def search(name):
    return contacts.get(name)

#delete_contact
def delete(cnt):
    if cnt in contacts :
        del contacts[cnt]
        print(f"{cnt} has deleted from contacts")
    else :
        print(f"{cnt} not found in contacts")
    
    

#view
def views():
    for x,y in contacts.items():
        print(f"\n{x}:{y}")

#input
while True:
    user = input("\nplease select an option : ")
    if user == "1":
        cont = input("\nplease enter the name : ")
        number = input("\nplease enter the number : ")
        add(contact=cont,num=number)
        print(f"\n{cont} with number {number} has added to contacts")
    elif user == "2":
        search_input = input("\nplease enter the name that you want to find : ")
        res = search(name=search_input)
        if res :
            print(f"\nnumber for {search_input} is {res}")
        else:
            print(f"\ncontact '{search_input}' not find")
    elif user == "3":
        name_to_delete = input("\nplease enter the name that you want to delete :")
        delete(name_to_delete)
    elif user == "4":
        views()
    elif user == "5":
        print("\ngood bye ^-^")
        break
    else:
        print("\nplease enter a valid option")