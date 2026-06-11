def calculate_fare():
    return 5000

def book_trip():
    fare = calculate_fare()   # Consuming another function
    print("Trip booked.")
    print("Fare:", fare)

book_trip()
