import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None

    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''

        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim), [0, 0], 'k-')
        plt.plot([0, 0], (-y_dim, y_dim), 'k-')
        plt.xlim(-x_dim, x_dim)
        plt.ylim(-y_dim, y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.poly = A
        self.old_poly = []
 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        self.old_poly = self.poly
        self.poly = []
        Shape.translate(self, dx, dy)
        for i in range(0, len(self.old_poly)):
            mat = np.array([self.old_poly[i][0], self.old_poly[i][1], 1])
            ans = np.dot(mat, self.T_t)
            self.poly.append([ans[0], ans[1]])


        return self.poly



    
    def scale(self, sx, sy ):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        self.old_poly = self.poly
        self.poly = []
        Shape.scale(self, sx, sy)
        for i in range(0, len(self.old_poly)):
            mat = np.array([self.old_poly[i][0], self.old_poly[i][1], 1])
            ans = np.dot(mat, self.T_s)
            self.poly.append([ans[0], ans[1]])

        return self.poly
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        self.old_poly = self.poly
        t = [rx, ry]*len(self.poly)
        t = np.array(t)
        self.poly = np.array(self.poly)
        ar = self.poly - t

        self.poly = []
        Shape.scale(self, deg)
        for i in range(0, len(self.old_poly)):
            mat = np.array([ar[i][0], ar[i][1], 1])
            ans = np.dot(mat, self.T_r)
            self.poly.append([ans[0], ans[1]])

        return self.poly

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        figure, axes = plt.subplots()
        axes.set_aspect(1)

        axes.add_artist(plt.Circle((self.x, self.y), self.radius, color='pink'))

        axes.add_artist(plt.Circle((self.x_old, self.y_old), self.rad_old, linestyle='--', fill=False))

        Shape.plot(self, (self.x + self.radius), (self.x + self.radius))


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.x_old = 0
        self.y_old = 0
        self.rad_old = 0

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        self.x_old = self.x
        self.y_old = self.y
        self.rad_old = self.radius
        mat = np.array([self.x, self.y, 1])
        Shape.translate(self, dx, dy)
        ans = np.dot(self.T_t, mat)
        return ans[0], ans[1], self.radius
        
    def scale(self, sx = 1):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.x_old = self.x
        self.y_old = self.y
        self.rad_old = self.radius
        Shape.scale(self, sx, sx)
        mat = np.array([self.radius, 0, 0])
        ans = np.dot(mat, self.T_s)
        return self.x, self.y, ans[0]

    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.x_old = self.x
        self.y_old = self.y
        self.rad_old = self.radius
        Shape.rotate(self, deg)
        mat = np.array([self.x - rx, self.y - ry, 1])
        ans = np.dot(mat, self.T_r)
        return ans[0], ans[1], self.radius
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        figure, axes = plt.subplots()
        axes.set_aspect(1)

        axes.add_artist(plt.Circle((self.x, self.y), self.radius, color='pink'))

        axes.add_artist(plt.Circle((self.x_old, self.y_old), self.rad_old, linestyle='--', fill=False))

        Shape.plot(self, (self.x + self.radius)*2, (self.x + self.radius)*2)

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    ''' print("welcome!")
    while True:
        a1 = input("enter 1 if you want to see the plot after transformation otherwise enter 0")
        if a1 != '1' or a1 != '0':
            print("please enter correct choice")
        else:
            a1 = int(a1)
            break
    while True:
        a2 = input("enter 1 if you want to generate a circle, enter 0 to generate a polygon")
        if a2 != '1' or a2 != '0':
            print("please enter correct choice")
        else:
            a2 = int(a2)
            break

    if a2 == 0:
        co_ord = []
        n = int(input("enter the number of sides of polygon"))
        for i in range(0, n):
            x = input("enter space separated co-ordinates x"+ str(i) + " y" + str(i)).split()
            li = [x[0], x[1]]
            co_ord.append(li)
            Polygon(co_ord)



    print("choose the shape you would like to generate")
    print("")
    '''
    c = Circle(1,1,3)
    print(c.radius)
    (c.x, c.y, c.radius) = c.rotate(45,0,0)
    print(c.radius)

    c.plot()