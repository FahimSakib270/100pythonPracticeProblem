# Given a string s representing time in 24-hour format "HH:MM", compute the smallest angle in degrees between the hour and minute hands of an analog clock.

hour = int(input("Enter the time in hour "))
minutes = int(input("Enter the time in minutes "))

h = hour % 12

angle_diff = abs(60 * h - 11 * minutes) / 2.0

smallest_angle = min(angle_diff, 360 - angle_diff)

print(f"The smallest angle between hour and minute hands is {smallest_angle}°")
