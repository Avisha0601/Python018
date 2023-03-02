import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

plt.scatter(x, y, label="stars", color= "teal",
            marker="*", s=50)

plt.xlabel('timeX')
plt.ylabel('distanceX')
plt.title('SPEED!!')
plt.legend()
plt.show()