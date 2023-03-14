import time
import json
import math

print("Opening points file")

filein = open("spline.json")
coordinates = json.load(filein)
filein.close()

nPoints = len(coordinates[1])

l1 = 7
l2 = 13

print("Number of points: " + str(nPoints))
angles = [[0] * nPoints, [0] * nPoints]
for i in range(0, nPoints):
    
    y = coordinates[0][i]
    x = coordinates[1][i]
    
    l3 = math.sqrt(x**2+y**2)
    if l3 > (l1 + l2):
        print("Error: target position out of range")
        break
    
    b1 = (l1**2 + l3**2 - l2**2)/(2*l1*l3);
    a1 = math.atan2(math.sqrt(1-b1**2),b1);

    t1 = math.atan2(y,x) - a1

    
    b2 = (l1**2 + l2**2 - l3**2)/(2*l1*l2);
    a2 = math.atan2(math.sqrt(1-b2**2),b2);

    t2 = math.pi - a2
    
    # convert to degrees
    t1 = t1 * 180/math.pi
    t2 = t2 * 180/math.pi
    
    #print("Shoulder angle: " + str(t1))
    #print("Elbow angle: " + str(t2))
    angles[0][i] = t1
    angles[1][i] = t2

print("Opening file to print")
file = open("listangle.json", "w")
print("Exporting points to file")
json.dump(angles, file)
print("Closing file")
file.close()