# We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.
# Take input as
# 1. Number of Interior walls
# 2. Number of Exterior walls
# 3. Surface Area of each Interior 
# 4. Wall in units of square feet
# Surface Area of each Exterior Wall in units of square feet
# If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.
# Calculate and display the total cost of painting the property
# Example 1:
# 6
# 3
# 12.3
# 15.2
# 12.3
# 15.2
# 12.3
# 15.2
# 10.10
# 10.10
# 10.00
# Total estimated Cost : 1847.4 INR


INTERIOR_PAINT = 18
EXTERIOR_PAINT = 12

#No of interior walls
NoOfIntWall = int(input())
IntWallArea = []

#No of exterior walls
NoOfExtWall = int(input())
ExtWallArea = []

IntTotalArea = 0.0
for i in range(NoOfIntWall):
    #Interior walls
    temp = float(input())
    IntWallArea.append(temp)
    IntTotalArea = IntTotalArea + IntWallArea[i]

ExtTotalArea = 0.0
for i in range(NoOfExtWall):
    #Exterior walls
    temp = float(input())
    ExtWallArea.append(temp)
    ExtTotalArea = ExtTotalArea + ExtWallArea[i]

print(f"Total Estimated Cost : {(IntTotalArea*INTERIOR_PAINT + ExtTotalArea*EXTERIOR_PAINT)} INR")
