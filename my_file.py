#! /opt/anaconda3/bin/ python

'''
First exercise on Print
'''
#first_name = "Shankar"
#last_name = "Swaminathan"
#age = 35
#birth_date = "22-02-1985"

#print("My name is %s %s" % (first_name, last_name))
#print("I was born on %s and I'm %s years old." % (birth_date,str(age)))

'''
Second exercise on if-else and boolean
'''
# user = { 'admin': False, 'active': False, 'name': 'Kevin' }

# if user["admin"] and user["active"]:
#     print("Active - (Admin) " + user["name"])
# elif user["admin"]:
#     print("(Admin) " + user["name"])
# elif user["active"]:
#     print("Active " + user["name"])
# else:
#     print(user["name"])

'''
3rd Exercise - Iterating Over Lists
'''

# user_list = [{ 'admin': True, 'active': False, 'name': 'Kevin' },{ 'admin': False, 'active': True, 'name': 'Shankar' },{ 'admin': True, 'active': True, 'name': 'Aish' }]
# line = 1
# for user in user_list:
#     if user["admin"] and user["active"]:
#         print(str(line) + " Active - (Admin) " + user["name"])
#     elif user["admin"]:
#         print(str(line) + " (Admin) " + user["name"])
#     elif user["active"]:
#         print(str(line) + " Active " + user["name"])
#     else:
#         print(user["name"])
#     line += 1

'''
4th exercise - Function to print the message echo as many times per user input

'''

# def echo_message(message,echo_count = 1):
#     while echo_count >=1:
#         print(message)
#         echo_count -=1

# message = input("Enter a message: ")
# count = int(input("Enter number of times to repeat : "))
# echo_message(message,count)

'''
5th Exercise - Function to print pi with as many decimal places defined in the environment variable

'''
# from math import pi
# import os

# print("%.*f" % (int(os.getenv("DIGITS",default=10)),pi))

'''
File writing exercise
'''

# file_name = input("please enter the file name: ")
# file_contents = [input("What do you want to add in the file (Leave empty line to stop): ")]
# while True:
#     file_contents.append(input())
#     if file_contents[len(file_contents)-1] == "":
#         file_contents.pop()
#         #for line in file_contents:
#         with open(file_name,mode='w') as f:
#             f.writelines(["%s\n" % item  for item in file_contents])
#         break        
# #print(file_contents)

'''
File reading exercise
'''

# file_name = input("please enter the file name: ")
# line_number = int(input("Enter the line number to print: ").strip())
# try:
#     with open(file_name,mode='r') as f:
#         file_contents=f.readlines()
#     if line_number >0 and line_number<len(file_contents):
#         print(file_contents[line_number-1])
#     else:
#         print("The line doesn't exist in the file")
# except:
#     print("Error: File not found")

# Method 2 using arg parser

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('file_name', help='the file to read')
# parser.add_argument('line_number', type=int, help='the line to print from the file')

# args = parser.parse_args()
# file_name  = args.file_name
# line_number = args.line_number
# try:
#     with open(file_name,mode='r') as f:
#         file_contents=f.readlines()
#         print(file_contents[line_number-1])
# except IndexError:
#     print("The line doesn't exist in the File" )
# except IOError:
#     print("Error: File not Found" )

'''
Use OS library to kill a process that runs on a specific port
'''

import os
import argparse
import subprocess
from sys import exit

parser  = argparse.ArgumentParser()
parser.add_argument('port', help= "Port number of process")

args = parser.parse_args()
port = args.port.strip()

try:
    result  = subprocess.run(['lsof','-n', '-i4TCP:%s' % port],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print("There is no process running in the specified port %s" % port)
    exit(1)
else:
    listening = None
    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break
    
    if listening:
        os.kill((int(listening.split()[1])),9)
        print("Process %s has been killed " % str(listening.split()[0]))
    else:
        print("No process to kill in this port %s" % port)
        exit(1)


