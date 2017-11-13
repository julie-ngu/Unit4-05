# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program calculates the volume of a cylinder

from math import pi

def calculate(radius_input, height_input):
    # calculates the volume of the cylinder with the inputted parameters
        answer = pi * radius_input ** 2 * height_input
        
        return answer

# input
radius = int(input("Enter radius of cylinder: "))
height = int(input("Enter height of cylinder: "))

# process
if radius < 0 or height < 0:
    print ("Please enter a positive value for the height and radius.")
else:
    show_volume = calculate(radius, height) 
    
    # output
    print("The volume of the cylinder is " + str('{:0.2f}'.format(show_volume)) + " units.")
