import numpy as np
import matplotlib.pyplot as plt

#inisiasi nilai awal
A = 1.5
x = A
k = 0.08
m = 2
t = 0
v = 0
dt = 0.1
tmax = 50

listA_x = []
listA_t = []

#Solusi Analitik
i = t
while i<=tmax:
    w = np.sqrt(k/m)
    xT = A*np.cos(w*i)
    vT = - w*A*np.sin(w*i)
    aT = -(w*w)*A*np.cos(w*i)
    T = (2*3.14)/w
    
    i += dt
    listA_x.append(xT)
    listA_t.append(i)
    
plt.plot(listA_t,listA_x,label='Analitik')
plt.xlabel('posisi')
plt.ylabel('waktu')
plt.title('Analitik')
plt.legend()
plt.show()

# print ("posisi",listA_x)
print ("")
# print ("waktu",listA_t)

x_list = []
t_list = []

#solusi numerik
while t <= tmax:
    a = (-k * x)/m
    v += a * dt
    x += v*dt
    t += dt
    x_list.append(x)
    t_list.append(t)
    
plt.plot(t_list,x_list,label='Numerik')
plt.xlabel('posisi')
plt.ylabel('waktu')
plt.title('Numerik')
plt.legend()
plt.show()

# print ("posisi",x_list)
print ("")
# print ("waktu",t_list)

plt.plot(t_list,x_list,label='Numerik')
plt.plot(listA_t,listA_x,label='Analitik')
plt.xlabel('waktu')
plt.ylabel('posisi')
plt.title('Analitik v Numerik')
plt.legend()
plt.show()

