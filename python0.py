import matplotlib.pyplot as plt

subjects = ['Computer', 'Science', 'German', 'Hindi', 'English', 'Maths', 'SST']
slices = [9,6,8,4,7,10,7]
colors = ['green', 'brown', 'purple', 'red', 'pink', 'aqua', 'orange']

plt.pie(slices, labels = subjects, colors=colors, 
        startangle=60, shadow = False, explode=(0,0,0,0,0,0,0),
        radius = 2, autopct = '%4.4f%%')
plt.legend()
plt.show()