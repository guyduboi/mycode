#!/usr/bin/env python3

# create a list. In practice, we might read data in from an excel file, 
# or an email. Lists are made with square brackets.

my_list = [ "192.168.0.5", 5060, "UP" ]

# write a line of code to return the IP address from out list

print("The first item in the list (IP): " + my_list[0] )

# return the port 5060. The problem is 5060 is an integer, not a string. 
# Strings are surrounded with quotes.

print("The second item in the list (port): " + str(my_list[1]) )

# return the last item in the list, this is a string value “UP”.

print("The last item in the list (state): " + my_list[2] )

# single print() function to display all of the data from your list

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Create a print command to do the following:
# When I ssh into IP addresses 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.

print("When I ssh into the IP address: " + new_list[3] + "  or  " + new_list[4] + "  -  I am unable to ping ports: " + str(new_list[0]) + "  "  + new_list[1] + "  " + str(new_list[2]) )




