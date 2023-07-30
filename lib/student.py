#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, string):
        print(string)
        self.knowledge.append(string)
        print(self.knowledge)