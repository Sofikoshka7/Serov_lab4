import numpy as np

from scipy.optimize import linprog

qf1=3
qf2=2

#1
# коэфициенты при х1 и х2 в D,
A = np.array([[1, 2], [-2, -1],[-1, 0],[1, 0], [0, -1],[0, 1]])
# правая часть неравенств
b = np.array([52, -13, 0, 26, 0, 19.5])
# коэфициенты при х1 и х2 в функции по которой идет оптимизация, но умноженные на -1
c = np.array([3, -1])
res = linprog(c, A_ub=A, b_ub=b)
print('первая максимизация по f2:', round(res.fun*-1-qf2, ndigits=2))

#2
f1 = res.fun*-1-qf1
A1 = np.array([[1, 2], [-2, -1], [-1, 0], [1, 0], [0, -1], [0, 1], [3, -1]])
b1 = np.array([52, -13, 0, 26, 0, 19.5, -f1])
c1 = np.array([-1, -1])
res1 = linprog(c1, A_ub=A1, b_ub=b1)
print('вторая максимизация по f1:', round(res1.fun*-1-qf1, ndigits=2))

#3
f2=res1.fun*-1-qf2
A2 = np.array([[1, 2], [-2, -1], [-1, 0], [1, 0], [0, -1], [0, 1], [3, -1], [-1, -1]])
b2 = np.array([52, -13, 0, 26, 0, 19.5, -f2, -f1])
c2 = np.array([-1, 3])
res2 = linprog(c2, A_ub=A2, b_ub=b2)
print('третья максимизация по f3:', round(res2.fun*-1, ndigits=2), '\nточка максимума:', res2.x)
print('Значение f1 в точке: ',f1,'\n','Значение f1 в точке: ',f2)

