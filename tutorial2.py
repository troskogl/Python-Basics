#
#                                                                        
# Title: tutorial2.py                                                 
# Author: Trond Skogland (trond.skogland@atea.no)                        
#                                                                        
# Description:                                                             
#                                                                        
#

import random
import sys
import os
import time

# # types of variables -> Numbers, Lists, Tuples, Dictionaries

# quote = "\"Always remember you are unique\""

# print(quote)

# multi_line_quote = '''just like
# like everyone else'''

# # print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
# print('I like the quote', quote, multi_line_quote)

# grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']
# print (grocery_list[1])
# grocery_list.sort()
# print (grocery_list)
# grocery_list.reverse()
# print(grocery_list)
# grocery_list.insert(2,'Pickle')
# print(grocery_list)
# grocery_list.sort()
# print(grocery_list)

# print(len(grocery_list))
# print(max(grocery_list))

# pi_tuple = (3,1,4,1,5,9)

# new_tuple = list(pi_tuple)

# print(pi_tuple)
# print(new_tuple)

# new_list = tuple(new_tuple)
# print(len(pi_tuple))
# print(max(pi_tuple))

# super_villains = {'Fiddler' : 'Isaac Bowin',
# 'Captain Cold' : 'Leonard Snart',
# 'Weather Wizard' : 'Mark Mardon',
# 'Mirror Master': 'Sam Scudder',
# 'Pied Piper' : 'Thomas Peterson'}

# print(super_villains)
# del super_villains['Fiddler']
# print(super_villains)
# super_villains['Pied Piper'] = 'Harley Rathaway'
# print(super_villains)
# print(len(super_villains))
# print(super_villains.get("Pied Piper"))
# print(super_villains.keys())
# print(super_villains.values())

# #if else elif
# age = 21
# if age > 16 :
# 	print("You are old enough to drive")
# else :
# 	print("you ar not old enough to drive")

# if age >=21:
# 	print ("You are old enough to drink")
# elif age >= 16:
# 	print("you are old enough to drive a car")
# else:
# 	print("you are not old enough to drive a car")

# # AND OR NOT

# if ((age >= 1) and (age <=18)):
# 	print("print something")

# Looping

# for x in range (0,10):
# 	if x < 9:
# 		print(x,', ', end="")
# 	else:
# 		print(x, end="")

# print('\n\n\n\n')

# grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']

# for y in grocery_list:
# 	print(y)

# num_list = [[1,2,3],[10,20,30],[100,200,300]]

# for x in range(0,3):
# 	for y in range(0,3):
# 		print(num_list[x][y])
# 		

# WHILE loop
# counter = 0

# random_num = random.randrange(0,100)
# counter = counter + 1
# print(random_num)
# while(random_num != 15):
# 	random_num = random.randrange(0,100)
# 	counter = counter + 1
# 	print(random_num)

# print("counter = ", counter)


# i = 0;

# while(i <=20):
# 	if(i%2 == 0):
# 		print(i)
# 	elif(i==11):
# 		break
# 	else:
# 		i +=1
# 		continue

# 	i +=1

# Functions

# def addNumber(fNum, lNum):
# 	sumNum = fNum + lNum
# 	return sumNum

# print(addNumber(1,4))

# print ("What is your name ")
# name = sys.stdin.readline()

# print("Hello", name)

# long_string = "i'll catch you if you fall - The Floor"

# print(long_string[0:4])
# print(long_string[-5:])
# print(long_string[:-5])

# print(long_string[:4] + " be there")

# print("%c is my %s letter and my number %d number is %.5f" %
# 	('X',"favorite", 1, .14))
# print("***************************")
# print(long_string)
# print(long_string.capitalize())
# print("***************************")
# print(long_string.find("Floor"))

# print(long_string.isalpha())
# print(long_string.isalnum())

# print(len(long_string))
# print(long_string.replace('Floor', 'Ground'))

# print("@@@@@@@\n")
# long_string = "                       I'll catch you if you fall - The Floor"
# print(long_string)
# print(long_string.strip())
# long_string = long_string.strip()
# quote_list = long_string.split(" ")
# print(quote_list)

# File I/O

# test_file = open("test.txt","wb")

# print(test_file.mode)

# print(test_file.name)

# test_file.write(bytes("Write me to the file \n", 'UTF-8'))

# test_file.close()

# test_file= open("test.txt", "r+")

# text_in_file = test_file.read()
# print(text_in_file)
# test_file.close()

# time.sleep(6)

# os.remove("test.txt")



# OBJECTS

class Animal(object):
	__name = None
	__heigh = 0
	__weight = 0
	__sound = 0

	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound


	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_weight(self, weight):
		self.__weight = weight

	def get_weight(self):
		return self.__weight
		
	def set_sound(self, sound):
		self.__sound = sound

	def get_sound(self):
		return self.__sound		

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kilogram and says {}".format(self.__name,self.__height,self.__weight,self.__sound)

cat = Animal('Whiskers',33 ,10 ,'Meow')

print(cat.toString())

class Dog(Animal):
	__owner = ""

	def __init__(self,name,height,weight,sound,owner):
		self.__owner = owner
		super(Dog,self).__init__(name,height,weight,sound)

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		return("Dog")

	def toString(self):
		return "{} is {} cm tall and {} kilogram and says {} His owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)

Donna = Dog('Donna', 50, 39, 'woff','Trond')

print(Donna.toString())

# CLASSES test #2

# class Ph:
# 	def __init__(self):
# 		self.y=5
# 		self.printHam()

# 	def printHam(self):
# 		print('ham')

# x=Ph()
# #x.printHam()
# #print (x.y)

# class Hero:
# 	'''
# 	A Hero who is allergic to apple
# 	'''
# 	def __init__(self,name):
# 		self.name = name
# 		self.health = 100

# 	def eat(self, food):
# 		if (food =="apple"):
# 			self.health -= 100
# 		elif (food == "ham"):
# 			self.health +=20

# Bob = Hero("Bob")

# print(Bob.name)
# print(Bob.health)
# Bob.eat("ham")
# print(Bob.health)

# class BaseClass(object):
# 	def printHam(self):
# 		print("Ham")

# class InheritingClass(BaseClass):
# 	pass

# x=InheritingClass()
# x.printHam()

#class Character(object):
# 	def __init__(self):
# 		self.health=100

# class Blacksmith (Character):
# 	def __init__(self):
# 		super(Blacksmith,self).__init__()

# bs = Blacksmith()
# print (bs.health)

# 