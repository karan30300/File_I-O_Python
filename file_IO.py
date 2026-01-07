"""
Docstring for File_IO.file_IO
We can Write File with Python inbuilt functions 
"""
# main file read write function is 
'''
open() : to open fiel in diffrent mode (r,w,a,b,t,r+,w+,a+).
        r = read mode > file open default Read mode
        w = to write into file > it Overrite file Old data Erase.
        a = appen into file > add at the end data write not erase old data 
        b = read Binary file
        t = read text file > a default file mode
        r+ = open for reading adn writing file ,r+ overwrite data from the start, it not Truncated (not erase old data)
        w+ = open fro writing file, w+ Truncated (Erace all old data)
        a+ = open read and append mode, pointer set end of file.
        
read() : to read file
readlines() : to read file line by line.
write() : to write into file 


'''
a = open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", 'r')
data = a.read()
print(data)
a.close()

b = open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", 'w')
wr = b.write("This Line write with write() function that erase all Old Data and add this New line ")
b.close()

c= open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", 'a')

ap = c.write("\nThis Line Write with Append Mode that not erace old data it write at end of the file ")
c.close()

"""
Note: in Write 'w' and append 'a' if there is no Existing file so, "w" and "a" mode create File Automatically
"""
d = open("D:\Code\Python\YT\Apna_Collage\File_IO\Test_data1.txt","w")
# This Cretae automatically Test_data1.txt file in currant folder
d.close()

e = open("D:\Code\Python\YT\Apna_Collage\File_IO\Test_data2.txt","a")
e.close()

f = open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", "r+")
f.write("Data overwrite in file from the Bignning ")
print(f.read())# Maybe Data is not show full Bec..  The curcer is read file after Data Add of abow data
f.close()

g = open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", 'w+')
g.write("This Line is Write with W+ mode that erase all Old data")
print(g.read())
g.close()

h = open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt",'a+')
print(h.read()) 
h.write("abc")
print(h.read())
h.close()

"""
With Syntax:
we can open file with batter way with (With)

with opne("file_name.txt", "mode") as f:
    data = f.read()
"""

with open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", 'r') as ab:
    demo = ab.read()
    print(demo) #It close File Auto..

with open("D:\Code\Python\YT\Apna_Collage\File_IO\data.txt", 'w')as write_f:
    write_f.write("data write with WITH Syntax")
    print(write_f)

"""with the help of OS module we can remove/delete File """
import os

os.remove("D:\Code\Python\YT\Apna_Collage\File_IO\Test_data2.txt")
os.remove("D:\Code\Python\YT\Apna_Collage\File_IO\Test_data1.txt")


"""Practice File_IO"""

"""
Q1>Create a new file "practice.txt" using python. Add the following data in it:
    Hi everyone
    we are learning File I/O
    using Java.
    I like programming in Java.
Q2>WAF that replace all occurrences of “java” with “python” in above file.
Q3>Search if the word "learning" exists in the file or not."""

# Q1
with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt") as f:
    data = f.read()

with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt", 'w')as f:

    f.writelines("""Hii Everyone.
we are learning File I/O.  
using Java
I like programming in Java""")

## Q2>
with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt") as f:
    data =f.read()
new_data = data.replace("Java", "Python")
print(new_data)

with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt", 'w') as f:
    f.write(new_data)

# Q3>
def check_word(word):
    with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt") as f:
        data = f.read()

        if word in data:
            print("Yes")
        else:
            print("No")
    return 0

word = "Python"
check_word(word)


"""
Q4> WAF to find in which line of the file does the word "learning"occur first.Print -1 if word not found.
Q5> From a file containing numbers separated by comma, print the count of even numbers.
"""
# Q4>

def check_line(word):
    data = True
    line_no = 1
    with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt", 'r') as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no +=1

        return -1

check_line("Python")

# Q5 >

def count_even_no():
    with open("D:\Code\Python\YT\Apna_Collage\File_IO\practice.txt")as f:
        data = f.read()
        # print(data)
        
        nums = data.split(",")
        # print(nums)
        count = 0

        for i in nums:
            if (int(i)%2 == 0):
                count += 1 
    return count
                

print(count_even_no())

