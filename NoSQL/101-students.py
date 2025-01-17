#!/usr/bin/env python3
"""
Log stats in Python
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Find all students
    """
    students = mongo_collection.find()
    student_list = []
    for student in students:
        scores = [topic['score'] for topic in student.get('topics', [])]
        if scores:
            average_score = sum(scores) / len(scores)
            student['averageScore'] = average_score
        else:
            student['averageScore'] = 0
        student_list.append(student)
    student_list.sort(key=lambda x: x['averageScore'], reverse=True)
    return student_list
