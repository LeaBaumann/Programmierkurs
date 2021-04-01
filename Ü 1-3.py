# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:52:25 2021

@author: Admin
"""

import math


def fizz_buzz(zahl):
    if zahl % 15 == 0:
        print("fizzbuzz")
    elif zahl % 3 == 0:
        print("fizz")
    elif zahl % 5 == 0:
        print("buzz")
    else:
        a = str(z)
        print(a)


fizz_buzz(-100)

omega0_1 = 3.14      # 1/s
omega0_2 = 5         # 1/s
omega0_3 = 1         # 1/s

delta_1 = 1.57       # 1/s
delta_2 = 1          # 1/s
delta_3 = 0.95       # 1/s

x_0 = 10
t = 1.23             # s

# Ihre Implementierung folgt hier ↓


def harm_oszi(omega, delta):
    ergebnis = 10 * (math.exp(-delta * 1.23)) * math.sin(1.23 * math.sqrt(omega ** 2 - delta ** 2))
    return ergebnis


# Speichern Sie die Ergebnisse Ihrer Berechnung in die folgenden Variablen:
x_1 = harm_oszi(omega0_1, delta_1)
x_2 = harm_oszi(omega0_2, delta_2)
x_3 = harm_oszi(omega0_3, delta_3)

print(x_1)
print(x_2)
print(x_3)


# Implementieren Sie die Klasse hier ↓
class Rectangle:
    def __init__(self, a, b):
        self.a = abs(a)
        # Maximale Geschwindigkeit in km/h
        self.b = abs(b)
    
    def __abs__(self):
        return self.a * self.b
    
    def __mul__(self, zahl):
        return self.a * zahl and self.b * zahl
    
    def __lt__(self, other):
        return (self.a * self.b) < (other.a * other.b)
    
    def __le__(self, other):
        return (self.a * self.b) <= (other.a * other.b)
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b 


pink_car = Rectangle(2, 3)
blue_car = Rectangle(2, 3)

z = 5

print(pink_car == blue_car)
print(pink_car < blue_car)
print(pink_car <= blue_car)
print(pink_car * z)
print(math.exp(3))
print(math.sqrt(4))


# Aufgabe a)
def pi_leibniz(number):
    m = 0
    for i in range(0, number+1, 1):
        m += (-1)**i / (2*i + 1)
    return m


# Aufgabe b)
pi = pi_leibniz(1000000) * 4
print(pi_leibniz(1000000) * 4)
print(pi_leibniz(0) * 4)

for x in (1, 2, 3):
    print(x)

for character in "Hallo":
    print(character)
    
    
def fib_rec(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib_rec(n-1) + fib_rec(n-2)

    
def fib_iter(n):
    f_0 = 0
    f_1 = 1
    k = 2
    while k < (n + 1):
        line = f_0 + f_1
        f_0 = f_1
        f_1 = line
        k += 1
        
    return f_1


print(fib_iter(10))


def fib_seq(n):
    liste = [0]
    for i in range(1, n+1, 1):
        liste.append(fib_iter(i))
        
    return liste


print(fib_seq(10))
