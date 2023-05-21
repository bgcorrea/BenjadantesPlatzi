import matplotlib.pyplot as plt

'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.ylabel('y numbers')
plt.xlabel('x numbers')

plt.show()
'''


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
  # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)

