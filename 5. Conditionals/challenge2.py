# Challenge:
# Combining several conditions into one price
# Compute a cinema ticket price from three inputs: age, whether the person is a student (yes/no), and the day of the week.

# Rules, applied to a base price of Rs 200:
# • Age under 12 OR 60+  -> 50% off the base price
# • Student               -> an extra 20% off
# • Weekend (Saturday/Sunday) -> add a 50% surcharge, applied AFTER the discounts

# Print a clear breakdown and the final price.

# Example:
# Age: 20
# Student (yes/no): yes
# Day: Saturday

# Base price:        Rs 200
# Student discount:  -Rs 40
# Weekend surcharge: +Rs 80
# Final price:       Rs 240

# Solution:
age = int(input("enter your age: "))
is_student = input("Are you a student? (yes/no): ")
day = input("enter the day: ")

ticket_price = 200                              #Total Ticket Price
age_discount = ticket_price / 2                 #Discount for Senior citizen and children 
student_discount = (ticket_price * 20) / 100    #Discount for Students

print(f"Age: {age}")
print(f"Student: {is_student}")
print(f"Day: {day}")

print(f"Ticket Base Price: {ticket_price}")
if(age <= 12 or age > 60):
    print(f"Age Discount: Rs -{ticket_price / 2}")
    ticket_price /= 2
if(is_student == "yes"):
    print(f"Student Discount: Rs -{student_discount}")
    ticket_price -= student_discount
if(day == "saturday" or day == "sunday"):
    week_surcharge = (ticket_price * 50) / 100      #Surcharge for weekends
    print(f"Weekend Surcharge: Rs +{week_surcharge}")
    ticket_price += week_surcharge
    
    
print(f"Final Ticket Price: {ticket_price}")