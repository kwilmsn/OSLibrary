'''This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
The program should then prompt the user for their name, address, and phone number.
Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 

Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes. 

Submit a link to your Github repository.'''
import os

userDirectory = input('What directory would you like to save this file to? ')
#checking to make sure that the directory doesn't already exsist
if os.path.exists(userDirectory):
	pass
#if it doesn't exsist create a new directory
else:
	try:
		os.mkdir(userDirectory)
	except OSError:
		print("Creation of directory %s failed. Please Try Again!")
	else:
		print("Success")

userFile = input('What is the name of the file? ')
#if the userFile doesn't end in .txt add .txt and add userDirectory at the beginning
if userFile[-4:] != '.txt':
	userFile = userDirectory + '/' + userFile + '.txt'
#if userFile does have .txt only add userDirectory at the beginning
else:
	userFile = userDirectory + '/' + userFile
#checking user input
while True:
	userName = input('What is your name? ')
	if userName.isnumeric():
		print("Invalid input. Please try again!")
		continue
	else:
		break
#checking user input
while True:
	userAddress = input('What is your address? ')
	if userAddress[:2].isnumeric() and userAddress[-3:-1].isalpha():
		break
	else:
		print("Invalid input. Please try again!")
#checking user input
while True:
	try:
		userPhoneNumber = int(input('What is your phone number? '))
		break
	except:
		print("Invalid input. Please try again!")
#checking user input
while True:
	if len(str(userPhoneNumber)) == 10:
		break
	else:
		print("Invalid input. Please try again!")
		userPhoneNumber = int(input('What is your phone number? '))
		continue
with open(userFile, 'w') as file_object:
	file_object.write(userName + ', ' + userAddress + ', ' + str(userPhoneNumber) + '.')
with open(userFile) as file_object:
	contents = file_object.read()
	print(contents)
