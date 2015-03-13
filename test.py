import contact

def main():
    contact_list = [] 
    while True:
        name = input("Add Contact: ")
        if name == 'Done':
   	     break
        else:
   	     contact_list = contact.add_contact(contact_list, name)
    contact.get_contact(contact_list)

main()