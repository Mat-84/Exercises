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
    contacts[name] = contacts.keys()
    if name in contacts:
        return name
    else :
        return "its not in the dictionary"

#delete_contact
def delete():
    pass

#view
def views():
    pass

#input
user = input("\nplease select an option : ")
if user == "1":
    cont = input("please enter the name : ")
    number = input("please enter the number : ")
    add(contact=cont,num=number)
    print(f"{cont} with number {number} has added to contacts")


