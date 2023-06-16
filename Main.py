import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
import csv
from sklearn import linear_model
from sklearn.metrics import r2_score

# خواندن فایل housePrice.csv ( فایلی که تمیز شده است )
df = pd.read_csv("housePrice.csv")

# تبدیل شدن مقادیر Parking به ازای True : 1 و به ازای False : 0 -
pdf = df['Parking']
parking = list()
for i in pdf:
    if i == True:
        parking.append([1])
    else:
        parking.append([0])

# تبدیل شدن مقادیر Ware house به ازای True : 1 و به ازای False : 0 -
wdf = df['Warehouse']
warehouse = list()
for i in wdf:
    if i == True:
        warehouse.append([1])
    else:
        warehouse.append([0])

# تبدیل شدن مقادیر Elevator به ازای True : 1 و به ازای False : 0 -
edf = df['Elevator']
elevator = list()
for i in edf:
    if i == True:
        elevator.append([1])
    else:
        elevator.append([0])

# خواندن فایل temp.csv ( فایلی که تمام آدرس ها در آن نوشتن شده است )
newFile = pd.read_csv("temp.csv")
nf = newFile['address']

# شناسه دادن به آدرس ها به ازای نام آن ها
adf = df['Address']
addressDi = dict()
a = 1
for i in nf:
    addressDi[i] = a
    a += 1
addressli = list()
for i in adf:
    for j in addressDi:
        if i == j:
            addressli.append([addressDi[j]])

# ذخیره کردن کل داده ها به همراه جایگذاری داده های تبدیل شده در فایل جدید
ariadf, roomdf, pricedf, usddf = df['Area'], df['Room'], df['Price'], df['Price(USD)']
myLi = list()
c = 0
for i in ariadf:
    myLi.append([i,roomdf[c],parking[c][0],warehouse[c][0],elevator[c][0],addressli[c][0],pricedf[c],usddf[c]])
    c += 1
mfile = open("newhousePrice.csv", "w", newline="")
writer = csv.writer(mfile)
writer.writerow(['Area','Room','Parking','Warehouse','Elevator','Address','Price','Price(USD)'])
writer.writerows(myLi)
mfile.close()

df = pd.read_csv("newhousePrice.csv")
cdf = df[['Area','Room','Parking','Warehouse','Elevator','Address','Price','Price(USD)']]
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['Area','Room','Parking','Warehouse','Elevator','Address']])
y = np.asanyarray(train[['Price']])
regr.fit(x,y)
print('Coefficents: ', regr.coef_)
print('Intercept: ', regr.intercept_)

test_x = np.asanyarray(test[['Area','Room','Parking','Warehouse','Elevator','Address']])
test_y = np.asanyarray(test[['Price']])
test_y_ = regr.predict(test_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print('Residual sum of squares (MSE): %.2f' % np.mean((test_y_ - test_y) ** 2))
print('Variance score: %.2f' % regr.score(test_x, test_y))
print("R2-score: %.2f" % r2_score(test_y, test_y_))

_area = int(input('Area: '))
_room = int(input('Room: '))

_parking = bool(input('Parking (True or False): '))
if _parking == True:
    _ptemp = 1
else :
    _ptemp = 0

_ware = bool(input('Ware House (True or False): '))
if _ware == True:
    _wtemp = 1
else :
    _wtemp = 0

_eleva = bool(input('Ware House (True or False): '))
if _eleva == True:
    _etemp = 1
else :
    _etemp = 0

_address = input('Address: ')
_ad = addressDi[_address]

Result = regr.predict([[_area,_room,_ptemp,_wtemp,_etemp,_ad]])
print('Result : ',Result[0][0])