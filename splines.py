from scipy.interpolate import PchipInterpolator
import matplotlib.pyplot as plt
import numpy as np
import json



# x and y knot positions for the step arc
x_knots1 = [-6, -4, 0, 4, 6]
y_knots1 = [14, 12.5, 11.51, 12.5, 14]


# evaluation points for first spline
x_eval1 = np.linspace(x_knots1[0], x_knots1[-1], 20)

y_spline1 = PchipInterpolator(x_knots1, y_knots1)

coords = [x_eval1, (y_spline1(x_eval1, 0))]


# convert the coords into list format so it can be exported in a json
coords = [coords[0].tolist(),coords[1].tolist()]

# plot to make sure shape is what I expected
plt.plot(coords[0], coords[1])
plt.show()

# dumps coordinates into a json to be flashed onto arduino
# to be used in the code to control the arm
print("Opening file to print")
file = open("spline.json", "w")
print("Exporting points to file")
json.dump(coords, file)
print("Closing file")
file.close()