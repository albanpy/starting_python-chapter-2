R=float(input("Enter the length of the row, in feet:"))
E=float(input("Enter the amount of space used by an end-post assembly, in feet:"))
S=float(input("Enter the amount of space between the vines, in feet:"))

#V is the number of grapevines that will fit in the row
V=(R-2*E)/S
print(f'The number of grapevines that will fit in the row are {V:,}feet')
