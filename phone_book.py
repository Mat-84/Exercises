#menu
print("="*15,"Contact book","="*15)
print("\n1.Add contact\n2.Search contact\n3.Delete contact\n4.View All contacts\n")
print("="*15)

#contacts-dict
contacts = {}

#add_contact
def add(contact,num):
    contacts[contact] = num

#search_contact
def search(name):
    return contacts.get(name,"Contact not find")

#delete_contact
def delete():
    pass

#view
def views():
    pass

#input
user = input("\nplease select an option : ")
if user == "1":
    cont = input("\nplease enter the name : ")
    number = input("\nplease enter the number : ")
    add(contact=cont,num=number)
    print(f"{cont} with number {number} has added to contacts")
elif user == "2":
    search_input = input("\nplease enter the name that you want to find : ")
    res = search(name=search_input)
    print(f"\n{res}")
elif user == "3":
    pass
elif user == "4":
    pass