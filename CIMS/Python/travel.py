def calculate_fare():
    return 5000

def total_bill():
    fare = calculate_fare()   # Consuming another function
    gst = 500
    return fare + gst

def book_trip():
    bill = total_bill()       # Consuming another function
    print("Trip booked.")
    print("Total Bill:", bill)

book_trip()
=============================================

def calculate_fare(passengers):
    return passengers * 5000

def total_bill(passengers):
    fare = calculate_fare(passengers)
    return fare + 500

def book_trip(name, passengers):
    print("Customer:", name)
    print("Total Bill:", total_bill(passengers))

book_trip("Rahul", 2)



