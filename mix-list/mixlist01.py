#!/usr/bin/env python3

# create a list containing three items
my_list = ["192.168.0.5", 5060, "UP"]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0])

#display the second item in the list
print("The second item in the list (port): " + str(my_list[1]))

# display the third item in the list
print("The last item in the list (state): " + my_list[2])

# make a list contianing 6 items
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# display only the IP addresses on the screen
print("The IP addresses are: " + iplist[3] + ", and : " + iplist[4])

#define wordbank list
wordbank = ["indentation", "spaces"]

#Name list
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)

num = int(input("Give me a number between 0 and 18:\n>"))

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


