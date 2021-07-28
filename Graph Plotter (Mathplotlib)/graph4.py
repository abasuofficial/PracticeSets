import matplotlib.pyplot as plt

def graphplotter(x,y):
    plt.plot(x, y)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Simulator')
    plt.show()


#X Axis Inputs
xaxis_max=int(input("Enter The Highest Value along X-Axis"))
xaxis_box=int(input("Enter The Total Boxes(Graph Units) along X-Axis"))

xaxis_smallest_divison=(xaxis_max/xaxis_box)


#Y Axis Inputs
yaxis_max=int(input("Enter The Highest Value along Y-Axis"))
yaxis_box=int(input("Enter The Total Boxes(Graph Units) along Y-Axis"))

yaxis_smallest_divison=(yaxis_max/yaxis_box)


#1 Large Box = 10 * Small Box
xaxis_largebox=(xaxis_box//10)

#Scale X Axis
temp = 0.0
for i in range (0,xaxis_largebox):
    print(f"Value of {i} Large Box along X-Axis (Without Origin)")
    valueX=xaxis_smallest_divison*10
    #increment
    #print(valueX)
    temp=temp+valueX
    print(temp)

#1 Large Box = 10 * Small Box
yaxis_largebox=(yaxis_box//10)

#Scale Y Axis
temp2 = 0.0
for i in range (0,yaxis_largebox):
    print(f"Value of {i} Large Box along Y-Axis (Without Origin)")
    valueY=yaxis_smallest_divison*10
    #increment
    #print(valueY)
    temp2=temp2+valueY
    print(temp2)

#Input Data
x_axis_value_inputs = []
y_axis_value_inputs = []

numberofpoints=int(input("How many points do you want to plot?"))

print("Enter The Values in following format X_Axis_Value - Y_Axis_Value")

for i in range (0, numberofpoints):
    x_axis_value_inputs_temp=int(input(f"Enter X axis Value for {i} point"))
    x_axis_value_inputs.append(x_axis_value_inputs_temp)
    y_axis_value_inputs_temp=int(input(f"Enter Y axis Value for {i} point"))
    y_axis_value_inputs.append(y_axis_value_inputs_temp)


#Plotting/Mapping in Graph
x_axis_value_outputs = []
y_axis_value_outputs = []

for i in range (numberofpoints):
    x_axis_value_output_temp=(x_axis_value_inputs[i]//xaxis_smallest_divison)
    x_axis_value_outputs.append(x_axis_value_output_temp)

    y_axis_value_output_temp=(y_axis_value_inputs[i]//yaxis_smallest_divison)
    y_axis_value_outputs.append(y_axis_value_output_temp)


#Output
print("Based on your inputed data the following point's co-ordinate will be(On Graph Paper):-\n")
for i in range (numberofpoints):
    print(f"({x_axis_value_inputs[i]},{y_axis_value_inputs[i]}) This Point will be on your graph at this ( {x_axis_value_outputs[i]} , {y_axis_value_outputs[i]}) point")

#Simulation
choice = int(input("Do yo want to Run Simulator?\n 1 - Yes\n 0 - Exit"))
x = x_axis_value_inputs
y = y_axis_value_inputs

if choice == 1:
    graphplotter(x,y)

elif choice == 0:
    exit(0)