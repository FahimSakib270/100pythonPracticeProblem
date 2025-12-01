angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

sum_of_angles = angle1 + angle2 + angle3

if sum_of_angles == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("These angles can form a triangle")
else:
    print("These angles cannot form a triangle")