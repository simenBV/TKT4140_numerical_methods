import numpy as np
import matplotlib.pyplot as plt

# A)


def helloWorld():
    print('Hello, world!')


# B)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
A = np.array([[1, 1, 2], [2, 3, 3], [4, 4, 5]])
B = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

print('a+b = ', a+b)
print('a•b = ', a*b)
print('AB = ', A@B)
print('A^T = ', A.T)
print('A^-1 = ', np.linalg.inv(A))
print('Ax = b', np.linalg.inv(A)*b)

# C)


def fib(n):
    f1 = 0
    f2 = 1
    print(f1, f2, end=' ')
    for i in range(n-2):
        temp = f1
        f1 = f2
        f2 = f2 + temp
        print(f2, end=' ')


def improvedFib(n):
    f1 = 0
    f2 = 1
    ar = np.array([0, 1])
    for i in range(n-2):
        temp = f1
        f1 = f2
        f2 = f2 + temp
        ar = np.append(ar, f2)

    x = np.linspace(0, n, n)
    plt.plot(x, ar, 'o')
    plt.grid(True)
    plt.yscale('log')
    plt.xlabel('n')
    plt.ylabel('fib(n)')
    plt.title('Fibonacci series')

    plt.show()



def plotSin():
    plt.figure()
    x1 = np.linspace(0, 2*np.pi, 10)
    y1 = np.sin(x1)
    x2 = np.linspace(0, 2 * np.pi, 50)
    y2 = np.sin(x2)
    p1, p2 = plt.plot(x1, y1, x2, y2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('sin(x) plot')
    plt.legend((p1, p2), ('10 points', '50 points'))
    plt.show()
    plt.savefig('sinX.png', bbox_inches='tight')



if __name__ == '__main__':
    fib(5)
    # plotSin()
    # improvedFib(30)


