
'''
Name:
Date:
Description:
'''


'''#View flights method
Display all available flights in a formatted table.
• Loop through each flight in the flights list
• Format and display the details of each flight.
o The flight details should include flight number,
source, destination, available seats, and price.
• Parameter(s): list of flights
• The function does not return any value including
None.'''
def view_flights(flight_data):
  pass


'''
 Allow a passenger to book seats on an available
flight
• It performs the following steps:
• Prompt the user for flight number
• Search the flights list for a matching flight
• If flight is found:
o Prompt user for number of seats to book
o Check if there are enough available seats
(i.e., requested seats ≤ available seats)
o If there are enough available seats
▪ Update the flight’s available seats.
▪ Call save_flights() to update the flight
file.
▪ Creates a new booking string in the
format passenger name,flight no,seats
booked.
▪ Adds the booking to the bookings list.
▪ Display a success message
o If there are not enough seats, display an
error message
• If flight is not found, display "Flight not found"
© 2026, Southern Alberta Institute of Technology 4
• Parameter(s): passenger name, file name, flights
list, and bookings list.
• The function does not return any value
'''
def book_flights():
  pass




'''
Displays all bookings for the current passenger.
• It performs the following steps:
• Iterate through each booking in the bookings
list.
• Process each booking string to extract booking
information.
• Check if the provided passenger has a booking.
• If a booking is found for this passenger:
o Prints the flight number and seats booked for
that booking.
• If no matching bookings are found, prints “You
have no bookings.”
• Parameter(s): passenger name, and bookings
list.
• The function does not return
'''
def view_bookings():
  pass


'''
• It cancels an existing flight booking by removing it from
the bookings file and returning the reserved seats to
flight’s seats.
• It performs the following main steps:
• It takes input for the flight number to cancel.
• It searches the bookings list for a booking that
matches the passenger’s name and flight number.
• If the flight is found:
o It retrieves the number of seats to cancel.
o It updates the flight’s available seats in the
flights list by adding back the canceled seats.
o It saves the updated flight data to the flights file
(e.g. flights.txt).
o It removes the booking from the bookings list.
o It displays a success message.
• If the flight is not found: it displays an error
message.
• Parameter(s): passenger name, the flights’ file
name, flights list, and bookings list.
• It does not return any value including None
'''
def cancel_booking():
  pass



'''
It reads flights data from the flight file (i.e., file_name)
o The flight data is a comma separated values and
includes flight number, source, destination, seats
available, and price.
• It stores the flights data in a list (i.e., flights list) and
returns it.
• Parameter(s): flights’ file name.
• It returns the flights list.
'''
def load_flights():

  pass




'''
It saves the flights list to the flights file.
• Before saving the flight data, it must be formatted as
comma separated values.
• Parameter(s): flights’ file name and flights list.
• It does not return any value including None.'''
def save_flights(file_name, flight_data):
  
  pass



'''
• It displays the main menu for the flight booking
system.
• It asks the user to select a menu option and return
it.
• Parameter(s): No parameters.
• It returns the user selection.'''
def main_menu():
  pass



'''
 It is the main entry point and control function for
the flight booking system.
• It displays a welcome banner.
• It prompts the user for a flight data filename
(e.g., flights.txt) and checks if the file exists.
o If the file is not found, it displays an error
message and prompts again.
o If the file is found, it loads the flights data
from the file and stores the flights data in a
list.
• It asks for the passenger's name.
• It continuously displays the main menu until the
user chooses to exit (option 5).
• It calls corresponding functions based on user
selection
• It displays an invalid input message if the user
selects an invalid option'''
def main():
  pass
  

if __name__ == "__main__":
 main()