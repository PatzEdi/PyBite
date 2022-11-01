#!/usr/bin/env python3

#CREATED BY ZIOZVEVO
#Started: August 12, 2022 at 11:40 AM, LATEST UPDATE: October 1, 2022 at 10:44 PM

import py_compile
import time
import os
import shutil

#Main functions:
def createmovefile():
	global dir, file
	#Split the path into the directory and the file.
	dir, file = os.path.split(filePath)
	#trim the file without .py to add the ".cpython-310.pyc" in order to find and move the file correctly.
	trimmedfile = file.replace(".py" , '')
	#Go to user inputted directory.
	os.chdir(dir)
	#if statememnt here to see if PyBite folder already exists.
	PyBiteAlreadyExistsCheck = os.path.isdir(dir + "/PyBite")
	if PyBiteAlreadyExistsCheck == False:
		print("\nCreating directories...")
		time.sleep(1)
		os.mkdir(dir + "/PyBite")
		print("\nCompiling file in bite code...")
		time.sleep(2)
		py_compile.compile(filePath)
		print("\nMoving file to PyBite Directory...")
		time.sleep(3)
		shutil.move(dir + "/__pycache__/" + trimmedfile + ".cpython-310.pyc", dir + "/PyBite/")
		time.sleep(2)
		os.chdir(dir + "/PyBite/")
		time.sleep(1)
		pycbase = os.path.splitext(trimmedfile + ".cpython-310.pyc")[0]
		os.rename(trimmedfile + ".cpython-310.pyc", pycbase + '.py')
	else:
		print("\nPyBite directory found.")
		time.sleep(1)
		print("\nCompiling file in bite code...")
		py_compile.compile(filePath)
		time.sleep(2)
		print("\nMoving file to PyBite Directory...")
		shutil.move(dir + "/__pycache__/" + trimmedfile + ".cpython-310.pyc", dir + "/PyBite/")
		time.sleep(2)
	#Code here to change from .pyc to .py in order to make it executable by python.
		os.chdir(dir + "/PyBite/")
		time.sleep(1)
		pycbase = os.path.splitext(trimmedfile + ".cpython-310.pyc")[0]
		os.rename(trimmedfile + ".cpython-310.pyc", pycbase + '.py')
#Second part of script (Checking if file is python or not):
def pythonfileornot():
	global filePath
	#Get last three letters of file, verify if Path-To-File is a python file.
	pyfilepattern = filePath[-3] + filePath[-2] + filePath[-1]
	pyfilepattern = str(pyfilepattern)
	if ".py" not in pyfilepattern:
		print("\nSorry, your file does not seem to be a python file.")
	#Detect whether file is python or not:
		while (1):
			filePath = input("\nPlease insert a path to a python file: ")
			filePathExistenceCheck = os.path.exists(filePath)
			pyfilepattern = filePath[-3] + filePath[-2] + filePath[-1]
			if ".py" not in pyfilepattern:
				print("Not a valid option!")
			elif pyfilepattern in filePath:
				createmovefile()
				#Put code to change bite-coded file to normal .py file.
				print("\nBite file created in: "  + dir + "/PyBite/")
				time.sleep(1)
				break
	elif pyfilepattern in filePath:
		createmovefile()
		print("\nBite file created in: "  + dir + "/PyBite/")
		time.sleep(1)

#Back in Menu:
def back():
	global choice, MainMenu
	#print(choice)
	backornot = int(input("\n(00) Back:"))
	if backornot == 00 or backornot == 0:
		choice = 0
		MainMenu = 0
	clearscreen()

#Clearscreen:
def clearscreen():
	if(os.name == 'posix'):
		os.system('clear')
	else:
		os.system('cls')
		
		
#Main Menu starts here:
clearscreen()
questions = "(1) Bite code python file:\n(2) Information:\n(99) Exit:\n Choice: "
choice = int(0)

while 1:
	if choice == 0:
		MainMenu = input(questions)
		MainMenu = int(MainMenu)
	if MainMenu == 1 or choice == 1:
		choice = 1
		clearscreen()
	#Start of script option 1(First part of script, checking if directory/file exists or not):
		print("\nPlease note that a new directory will be created containing the bite-coded file.")
		time.sleep(1.5)
		filePath = input("\nPATH to python file: ")
		
		#if filePath is a directory:
		filePathExistenceCheck = os.path.exists(filePath)
		
		
		if filePathExistenceCheck == False:
			print("\nSorry, that is not a valid path to a python file!")
			while(1):
			#If filePathCheck returns false, do:
				filePath = input("\nPATH to file: ")
				filePathExistenceCheck = os.path.exists(filePath)
				if filePathExistenceCheck == False:
					print("\nPath does not lead to a valid file!")
					#else:
				else:
					pythonfileornot()
					break
		#else		
		else:
			#Get last three letters of file, verify if Path-To-File is a python file.
			pythonfileornot()
	elif MainMenu == 2 or choice == 2:
		choice = 2
		clearscreen()
		print("\n\nBite code transforms your python code into a half human readable form of code. However, most of it is \"Obfuscated\". The good thing about bite code is that even if it isn't human readable, it is still executable by python. You can simply run the bite coded script or program as you would usually do: Calling the python command followed by the bite coded file.\n\nWhy Bite Code? Bite code can help in hiding some of your code from others. It can be decompiled.(However, most bite code decompilers are outdated*) Not only that, but bite code is a compiled version of python, making the script faster. This is useful if you want more efficiency in your scripts when executed.\n\nCreated with <3 by ZIOZVEVO")
	elif MainMenu == 99:
		clearscreen()
		print("\n\nThank you for using PyBite!\n\n")
		exit()
	else:
		choice = 0
		print("\nNot a valid option 1-2!\n")
		time.sleep(2)
		
	if (choice != 0):
		back()