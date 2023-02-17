from address import Address

class Perosn:
    def __init__(self, first, last, dob, phone, address) -> None:
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone = phone
        self.addresses = []

        if isinstance(address,Address):
            self.addresses.append(address)
        elif isinstance(address, list):
            for entry in address:
                if not isinstance(entry, Address):
                    raise ValueError('Invalid Address!')
            
            self.addresses = address
        else:
            raise ValueError('Invalid address!')
                
    def add_address(self, address):
        if not isinstance(address, Address):
            raise ValueError('Invalid Address!')
        
        self.addresses.append(address)