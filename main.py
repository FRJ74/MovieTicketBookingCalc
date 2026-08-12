# This is a Movie Ticket Booking System in python
base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"

# Calculate ticket price based on age and seat type

if age > 17:
    print("User is eligible to book a ticket")
if age >= 21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for Evening shows")

# Calculate discount based on membership status
is_member = True
is_weekend = False
discount = 0

if is_member:
    discount = 3
    print("User qualifies for membership discount")
else:
    print("User does not qualify for membership discount")

print("Discount:", discount) 



