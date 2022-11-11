from Contact import Contact


class PhoneBook:

    def __init__(self):
        """
        The phonebook keeps track of all contacts. This class is an example of 
        interacting with other classes a coder will make. 

        Instance variables provided for this constructor.
        """
        # My answer works
        self.contactsLst = []
        self.count = 0

    def addContact(self, c):
        """
        Given a contact, determine if you are given a dictionary or an instance of 
        a Contact class. Handle the adding to our phone book appropriately and update the counter.

        If you are given a dictionary, assume that a dictionary has the following keys 
        (and the values are in the correct format):
        - name
        - number
        - email
        - birthday

        NOTE: Why do we have to manually update the counter?
        """
        # if type(c) == dict:
        #     self.contacts.append(
        #         Contact(c['name'], c['number'], c['email'], c['birthday']))
        # elif type(c) == Contact:
        #     self.contacts.append(c)
        if isinstance(c, Contact):
            self.contactsLst.append(c)
        elif isinstance(c, dict):
            name = c['name']
            number = c['number']
            email = c['email']
            birthday = c['birthday']
            newContact = Contact(name, number, email, birthday)
            self.contactsLst.append(newContact)
        self.count += 1

    def getContactCount(self):
        """
        Returns the number of contacts stored in the 
        """
        # Ans works
        return self.count

    def findContact(self, lName):
        """
        Given a last name, find the contact(s) and return the contact information. 

        Will be a list. 
        """
        # My answer works
        self.contactInfo = []
        for i in self.contactsLst:
            if i.last == lName:
                self.contactInfo.append(i)
        return self.contactInfo

    def groupChat(self, message):
        """
        Send a message to every contact in the phonebook
        """
        # Ans dont work
        # self.message = message
        for i in self.contactsLst:
            i.sendMessage(message)

    def __str__(self):
        """
        Returns a string representation of the phonebook class. 

        The output will be
        > Phone Book: #

        Where # is the number of contacts in the phonebook. 
        """
        # Kind of works
        # return "Phone Book: " + str(self.getContactCount())
        return "Phone Book: {}".format(self.getContactCount())
