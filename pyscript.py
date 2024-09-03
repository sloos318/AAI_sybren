
# for a mean: the average number
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

speed1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x1 = np.mean(speed1)

print(x1)

# for a meadian: the center value


speed2 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x2 = np.median(speed2)

print(x2)

# for a mode: the most comon value

speed3 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x3 = stats.mode(speed3)

print(x3)

# for standard deviation: how spread out the values are

speed4 = [86,87,88,86,87,85,86]

x4 = np.std(speed4)

print(x4)

# for the variance: how spread out the values are

speed5 = [32,111,138,28,59,77,97]

x5 = np.var(speed5)

print(x5)

# for the percentile: how much % is less than the given number

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x6 = np.percentile(ages, 75) 
# 75 is asking for the numer that 75% of the other numbers is lower to. Here it's 43.

print(x6)

# creating a data set

x7 = np.random.uniform(0.0, 5.0, 250)
# here we see making an array of random numbers between 0.0 and 5.0. We are making 250 of them.

print(x7)

# here we are creating a histogram to show our data
plt.hist(x7, 5)
plt.show()


# Here we create a gausian data set: data set arround a certain number.
x8 = np.random.normal(5.0, 1.0, 100000)

plt.hist(x8, 100)
plt.show()

# scatterplot
x9 = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y9 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x9, y9)
plt.show()

# scatterplot with normal deviation

x10 = np.random.normal(5.0, 1.0, 1000)
y10 = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x10, y10)
plt.show()

#creating linear expression
x11 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y11 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x11, y11)

def myfunc(x11):
  return slope * x11 + intercept

mymodel = list(map(myfunc, x11))

plt.scatter(x11, y11)
plt.plot(x11, mymodel)
plt.show()

# finding r the relationship
x12 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y12 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r12, p12, std_err = stats.linregress(x12, y12)

print(r12)

# predicting values
x13 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y13 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x13, y13)

def myfunc(x13):
  return slope * x13 + intercept

speed13 = myfunc(10)

print(speed13)

# for polynomial reggresions
x14 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y14 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x14, y14, 3))

myline = np.linspace(1, 22, 100)

plt.scatter(x14, y14)
plt.plot(myline, mymodel(myline))
plt.show()

# getting R-squared: the relation for poynomial regresions
x15 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y15 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x15, y15, 3))

# print(r2_score(y15, mymodel(x15)))


