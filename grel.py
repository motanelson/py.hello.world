import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

def calcX(i):
    X=[]
    for n in range(i):
        X.append([n*0.1 , n*2.25])
    return X

def calcY(X):
    return [a+b for a,b in X]

X = calcX(20)
XX = calcX(40)

y = calcY(X)
yy= calcY(XX)
print(yy)
scaledX = scale.fit_transform(X)

model = LinearRegression()
model.fit(scaledX,y)

scaledXX = scale.transform(XX)

pred = model.predict(scaledXX)
def prints(tt):
    for t in tt:
        print(f"{t:.0f}", end=" , ")

prints(pred)