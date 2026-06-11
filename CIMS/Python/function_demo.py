def accept_cust_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    return {"name": name, "age": age, "email": email}       

def book_seat():
    seat_number = input("Enter the seat number you want to book: ")
    return seat_number

def calc_bill():
    price_per_seat = 100
    num_seats = int(input("Enter the number of seats you want to book: "))
    total_bill = price_per_seat * num_seats
    return total_bill

accepted_data = accept_cust_data()
print("Customer Data:", accepted_data)
seat = book_seat()
print("Seat booked:", seat)     
bill = calc_bill()
print("Total bill amount:", bill)


=======================
Positional Arguments
==========================
def total_marks(*marks):
    print("Marks received:", marks)
    print("Total:", sum(marks))

total_marks(80, 75, 90)
total_marks(60, 70, 85, 95)

===========================
keyword args
========================
def student_details(**details):
    print(details)

student_details(name="Rahul", course="Python", city="Mumbai")

==================
combined
==================
def booking(customer, phone, *tickets, **details):
    print("Customer:", customer)
    print("Phone:", phone)
    print("Tickets:", tickets)
    print("Details:", details)

booking(
    "Amit",
    "9876543210",
    "Goa",
    "Mumbai",
    meal="Veg",
    seat="Window"
)

