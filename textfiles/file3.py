"""Class: CS230--Section 1 
Name: Arlette Osuna
Description: (Give a brief description for Exercise name--See below)
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. """
fhand = open('mbox.txt')
inp = fhand.read()
print('Contents of file mbox.txt from read()')
print(inp)
print('Number of characters in the file is',len(inp))
print('First 20 characters in the file is',inp[:20])