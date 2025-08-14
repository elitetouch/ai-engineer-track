


# collect the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
attendees = set()

name = input("Enter the name of an attendee one: ")
attendees.add(name)
name = input("Enter the name of an attendee two: ")
attendees.add(name)
name = input("Enter the name of an attendee three: ")
attendees.add(name)
name = input("Enter the name of an attendee four: ")
attendees.add(name)
name = input("Enter the name of an attendee five: ")
attendees.add(name)
print(f"Attendees:\n {sorted(attendees)}")

