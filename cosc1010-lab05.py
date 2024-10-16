
# Caleb Behrman
# UWYO COSC 1010
# 10/15/24
# HW 01
# Lab Section: 2
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student and their scores
# in different subjects.
#
# Student Data:
# students = [
# {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
# {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
# {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
# {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
# ]
#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.
#Solution

#all of the solutions are under this hashtag
students=[
    {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
    {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
    {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
    {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}]
#this stuff above is just what has already been given to me

#dictionary to store the average things
average_scores={}

#this code below will calculate average score for each of the studs above
for student in students:
    name=student["name"]
    scores=student["scores"]
    average=sum(scores.values())/len(scores)
    average_scores[name]=average

#i had to look up what the "items()" and the "len()" did cause I forgot
#this prints students with an average score greater than 80
print("Studs with an average score greater than 80:")
for name, average in average_scores.items():
    if average>80:
        print(name)
#im pretty sure this is everything we need, if not sorry haha