class Flight():
    def __init__(self, seatCount):
        self.seatCount = seatCount
        self.passengers = []

    def addPassenger(self, passenger):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(passenger)
            return True

    def open_seats(self):
        return self.seatCount - len(self.passengers)
    
flight = Flight(3)

people = {"Luke","Leia","Chewbacca","Han"}
for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"Could not add {person} to flight. No available seats.")

