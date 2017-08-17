#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 00:09:18 2017

@author: sss
"""

class MyObject(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return self.name + str(self.age)
    
class MySubObject(MyObject):
    def __init__(self, name, age, slogan):
        super().__init__(name, age)
        self.slogan = slogan
    
    def getSlogan(self):
        return self.slogan
    
    def __str__(self):
        return super().__str__() + self.slogan