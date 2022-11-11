class Contact:

    def __init__(self, nameList, phoneNumber, email, birthday):
        """
        Variables Sent:
            Name, Phone number, Email, Birthdate

        Create Instance variables:
            - First Name:   first
            - Middle Name:  middle
            - Last Name:    last
            - Phone Number: mobile
            - Email:        email
            - BirthDate:    birthdate
        """
        # Cannot print last name (out of range error)
        # Pervious attempts:
        # self.first = nameList[0]+" "+nameList[1]+" " but this one function won't work+nameList[2]
        # self.first = nameList[0]
        # self.middle = nameList[1]
        # # self.last = nameList[1:]
        # self.mobile = phoneNumber
        # self.email = email
        # self.birthdate = birthday
        # Correct answer:
        self.first = nameList[0]
        if len(nameList) == 3:
            self.middle = nameList[1]
            self.last = nameList[2]
        else:
            self.middle = ""
            self.last = nameList[1]

        self.mobile = phoneNumber
        self.email = email
        self.birthdate = birthday

    def getName(self):

        # return self.first + " " + self.middle
        if self.middle:
            return self.first+" " + self.middle+" " + self.last
        else:
            return self.first + " " + self.last

    def __str__(self):
        """
        Returns a string representing the contact:
        > Contact: Josh Baker - 3178675309
        """
        # This is my attempt: and it kind of works
        # return "Contact: " + self.getName() + " - " + "("+str(self.mobile)+")"
        # Correct answer:
        return "Contact:{} -({})".format(self.getName(), self.mobile)

    def __repr__(self):
        """
        Provided: 
        - Feel free to read more about it here: https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
        """
        return self.__str__()  # This is provided. Helps with something printing a list of contact items.

    def call(self):
        """
        Print "Dialing ..." and then when they dont pick up
        the user should be prompted to input a message and then it should
        be printed
        """
        # print("Dialing...")
        # print("No answer")
        # print("Leave a message:")
        # self.sendText(input())
        # Correct answer:
        print("Dialing...", self.first, "...")

    def sendBirthdayText(self):
        """
        There should be a premade birthday text that uses the name 
        and then prints it out when this is called
        """
        self.sendText("Happy Birthday " + self.first + "!")

    def sendText(self, message):
        """
        Given a message a text to the person
        """
        print("To: " + self.first+":")
        print("\t" + message)

    def updateNumber(self, phoneNumber):
        """
        Take in a new phone number and replace the user's current phone number
        """
        self.mobile = phoneNumber
