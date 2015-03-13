def add_contact(contact_list, name):
    contact_list.append(name)
    print "You have %d contacts" % (len(contact_list))
    return contact_list

def get_contact(contact_list):	
    print "Your Contacts: %s"%(contact_list)

#if __name__ == "__main__":
contact_list = [] # create a list
get_contact(contact_list)
contact_list = add_contact(contact_list, "David")
get_contact(contact_list)
	