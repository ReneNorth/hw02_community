"""
from datetime import datetime
import time

seconds = time.time()


print('test', seconds)
print(datetime.now())
time.sleep(2)
print(datetime.now())


start_time = 1
execution_time = time.time() - start_time

"""

"""
cache = {1: 2, 2: 4}

class Try:
    def __init__(self, number):
        self.number = number

    def func(self):
          # create empty dictionary
        print(self.number, '<- to check')
        print(cache, '<- cache before the iterations')
        
        for key in list(cache.keys()):  # iterate through the dict 
            if self.number in cache.keys():  # if the argument is in the dic
                print(self.number, '-> value is already here')  # print value of that key
            else:
                new_entry = self.number * 2
                cache.update({self.number: new_entry})  # if the argument is not in the dictionary ->  
                print("added a new entry")
                print(cache)
            return cache


p1 = Try(1)
p1.func()

p2 = Try(4)
p2.func()

p3 = Try(3)
p3.func()

p4 = Try(4)
p4.func()
"""


"""
cache = {1: 2, 2: 4}


def func(number):
        # create empty dictionary
    print(number, '<- to check')
    print(cache, '<- cache before the iterations')
    
    for key in list(cache.keys()):  # iterate through the dict 
        if number in cache.keys():  # if the argument is in the dic
            print(number, '-> value is already here')  # print value of that key
        else:
            new_entry = number * 2
            cache.update({number: new_entry})  # if the argument is not in the dictionary ->  
            print("added a new entry")
            print(cache)
        return cache


func(55)
func(66)
func(55)

"""


"""

def func(*args, **kwargs):
    print(kwargs)
    for key in kwargs.keys():
        if key == '1':
            print(kwargs, 'if')
            print('1 in *args')
            result = 'x'
        else:
            print(kwargs, 'else')
            print('there is no one')
            result = 'xx'
    return result


a = {'1': 1, '2': 2}
func(**a)

"""

"""
def func(*args, **kwargs):
    if '1' in kwargs.keys():
        result = '1 in *args'
    else:
        result = 'there is no one'
    return result


a = {'1': 1, '2': 2}
print(func(**a))
"""

"""
def func(*args, **kwargs):
    if len(kwargs) >= 3:
        result = 'reset'
    else:
        result = 'not full yet'
    return result


a = {'1': 1, '2': 2}
b = {'1': 1, '2': 2, '3': 3}
print(func(**a))
print(func(**b))
"""
"""
count = {}


def func(*args, **kwargs):   
    cached_results = {}
    count[heavy.__name__] = 0
    
    if count[func.__name__] <= 2:
        result = cached_results[func.__name__]
        count[func.__name__] += 1
    else:
        result = func(*args, **kwargs)
        cached_results[func.__name__] = result 
    return result

def heavy():
    print('Сложные вычисления')
    return 1
"""
"""
count = {}

def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
x = heavy.__name__
print(x)

count[heavy.__name__] = 0
print(count)
count[heavy.__name__] += 1
print(count, 'count')
print(count[heavy.__name__], 's')

"""

import datetime
print(datetime.today())