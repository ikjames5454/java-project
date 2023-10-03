class CustomerInfo:
    def __init__(self, name, address, phoneNumber, email):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.phoneNumber

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def getInfo(self):
        return "Full name: " + self.name + "Address: " + self.address + "PhoneNumber: " + self.phoneNumber + "Email: " + self.email
