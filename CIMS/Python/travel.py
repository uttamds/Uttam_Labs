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
