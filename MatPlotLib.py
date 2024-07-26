import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(10):
    x.append(random.randint(1, 10))
    y.append(i * x[i])

print(x, y)
plt.plot(x, y)
plt.bar(x, y, 10, alpha=0.25)
plt.title('Комбинирование графиков')
plt.legend(loc='upper left', title= 'Два графика')
plt.show()


