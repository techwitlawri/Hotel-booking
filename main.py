import pandas


df = pandas.read_csv("hotels.csv", dtype= {"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
 
    def book(self):
        """Book a hotel by chaning its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)
        pass

    def available(self):
        
        availability= df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        pass


class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
        pass
    def generate(self):
        # content = f"Name of the customer hotel"
        # return content
        pass
        

print(df) 
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book() 
    name = input("Enter your name: ")
    reservation_ticket= ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
