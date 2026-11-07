#Challenge 5- Ask for the length and width of a rectangle and calculate its area and perimeter. 
length = float(input("What is the length of your rectangle: "))
width =  float(input("What is the width of your rectangle: "))
area = (length * width)
perimeter = ((length*2)+(width*2))
print("The area of you rectangle is "+ str(area) + " and the perimeter is "+ str(perimeter))