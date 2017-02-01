Run HW1_E.py using python3
Enter the support threshold as the first input and press enter
Then enter the file path (Easiest if the files are in the same directory) and press enter
Will output all frequent item sets separated by commas

Sample run w/ different directories:
ASHUNG-01:Homeworks alex.shung$ python3 HW1_E.py
Enter the support threshold
2
Enter the name of the file
/Users/alex.shung/Dropbox/UCLA Grad/Classes/CS 249/input.txt
p,ab,bc,r,ac,cr,c,abc,a,b

Sample run w/ same directory:
ASHUNG-01:Homeworks alex.shung$ python3 HW1_E.py
Enter the support threshold
2
Enter the name of the file
input.txt
r,a,cr,c,b,ac,ab,bc,abc,p

Sample input.txt:
c,r,a
p,b
r,c,b
p,c,a
a,b,s,c
t,a,b,c
