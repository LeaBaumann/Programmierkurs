# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:42:59 2021

@author: Admin
"""

import numpy, matplotlib.pyplot as plt

import math
T = numpy.loadtxt("Pendel-Messung.dat")
a = 0
for i in T:
    a += i

T_mean = a / len(T)
x = 0
for i in T:
    x += (i-T_mean)**2

T_var = 1/(len(T)-1) * x
T_mean_std = math.sqrt(T_var)/ math.sqrt(len(T))

T_10 = T[::10]

#print(T_mean_std)
#print(T[::10])

x1 = numpy.linspace(0, len(T), len(T_10))
y1 = T_10

#1. Diagramm

plt.subplot(221)
plt.title("Mathematisches Pendel")
plt.plot(x1, y1, "mo", markersize=2)
plt.ylabel("T[s]")
plt.xlabel("Index der Messung")
plt.errorbar(x1, y1, yerr=20*T_mean_std, fmt='none', color = 'green')

#2. Diagramm

r = max(T) - min(T) #range
b = r/(1+math.sqrt(len(T))) #intervalllänge
Intervalle = [min(T)]
i = min(T)
while i < max(T):
    i += b
    Intervalle.append(i)

plt.subplot(223)
hist, bins = numpy.histogram(T, bins = Intervalle)
h1 = []
i = 0
while i < 28:
    h1.append(hist[i])
    i +=1

#I = Intervalle.pop(0)
Intervalle.pop()
plt.plot(Intervalle, hist, "mo", markersize=2)
plt.ylabel("absolute Häufigkeit")
plt.xlabel("T[s]")
#error = math.sqrt(h1)

#fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
#plt.errorbar(Intervalle, h1, yerr = error, fmt='-o')

#print(hist)
#print(Intervalle)

#3. Diagramm

sum = 0
k = 0
while k < 28:
    sum += h1[k]
    k +=1

h2 = []
j = 0
while j < 28:
    h2.append(h1[j]/sum)
    j +=1

plt.subplot(222)
plt.plot(Intervalle, h2, "mo", markersize=2)
plt.ylabel("relative Häufigkeit")
plt.xlabel("T[s]")


plt.show





#Aufgabe 3

x_i = numpy.array((4.334, 10.274, 15.752))
y_i = numpy.array((5.4, 6.5, 4.5))

x = numpy.array([[4.334**2, 4.334, 1], [10.274**2, 10.274, 1], [15.752**2, 15.752, 1]])

a, b, c = numpy.linalg.solve(x, y_i)
print(a, b, c)

y0 = c
alpha = math.atan(b)
v0 = math.sqrt(-9.81/(2*a))/math.cos(alpha)
p = numpy.polynomial.Polynomial((c, b, a))

x1, x2 = numpy.polynomial.Polynomial.roots(p)
#print(x1, x2)
xw = x2

pd = numpy.polynomial.Polynomial.deriv(p)
#print(pd)
xe = numpy.polynomial.Polynomial.roots(pd)
#print(xe)
ye = p(xe)
#print(ye)