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
            mat = np.array(self.old_poly[i])
            ans = np.dot(self.T_t, mat)
            self.poly.append(ans)

        y_ar = []
        x_ar = []
        for i in range(0, len(self.poly)):
            self.poly[i][0] = round(self.poly[i][0], 2)
            self.poly[i][1] = round(self.poly[i][1], 2)
            y_ar.append(self.poly[i][1])
            x_ar.append(self.poly[i][0])
        return x_ar, y_ar




    def scale(self, sx, sy ):
        '''
        Function to scale the polygon

        This function takes 2 arguments: sx and sx

        This function returns the final coordinates
        '''
        self.old_poly = self.poly
        self.poly = []

        y_ar = []
        x_ar = []
        for i in range(0, len(self.old_poly)):
            y_ar.append(self.old_poly[i][1])
            x_ar.append(self.old_poly[i][0])
        cen_x = sum(x_ar)/len(x_ar)
        cen_y = sum(y_ar)/len(y_ar)

        x_ar = np.array(x_ar) - np.array([cen_x]*len(x_ar))
        y_ar = np.array(y_ar) - np.array([cen_y]*len(y_ar))

        Shape.scale(self, sx, sy)
        for i in range(0, len(self.old_poly)):
            mat = np.array([x_ar[i], y_ar[i], 1])
            ans = np.dot(mat, self.T_s)
            self.poly.append(list(np.array(ans) + np.array([cen_x,cen_y,0])))
        y_ar_f = []
        x_ar_f = []
        for i in range(0, len(self.poly)):
            self.poly[i][0] = round(self.poly[i][0], 2)
            self.poly[i][1] = round(self.poly[i][1], 2)
            y_ar_f.append(self.poly[i][1])
            x_ar_f.append(self.poly[i][0])
        return x_ar_f, y_ar_f

    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates
        '''
        self.old_poly = self.poly
        t = [[rx, ry, 0]]*len(self.poly)
        t = np.array(t)
        self.poly = np.array(self.poly)
        ar = self.poly - t

        self.poly = []
        Shape.rotate(self, deg)
        for i in range(0, len(self.old_poly)):
            mat = np.array(ar[i])
            ans = np.dot(mat, self.T_r.transpose())
            self.poly.append(ans)
        self.poly = np.array(self.poly)
        self.poly = self.poly + t
        for i in range(0, len(self.poly)):
            self.poly[i][0] = round(self.poly[i][0], 2)
            self.poly[i][1] = round(self.poly[i][1], 2)
        x_ar = []
        y_ar = []
        for i in range(0, len(self.poly)):
            y_ar.append(self.poly[i][1])
            x_ar.append(self.poly[i][0])

        self.poly = list(self.poly)
        return x_ar, y_ar

    def plot(self):
        '''
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''

        x_ar_n, x_ar_o, y_ar_n, y_ar_o = [], [], [], []
        for i in range(0, len(self.poly)):
            x_ar_n.append(self.poly[i][0])
            y_ar_n.append(self.poly[i][1])

            x_ar_o.append(self.old_poly[i][0])
            y_ar_o.append(self.old_poly[i][1])

        x_ar_n.append(x_ar_n[0])
        y_ar_n.append(y_ar_n[0])
        x_ar_o.append(x_ar_o[0])
        y_ar_o.append(y_ar_o[0])

        plt.plot(x_ar_n, y_ar_n)

        plt.plot(x_ar_o, y_ar_o, linestyle='--', color='k')
        x_ar_n.extend(x_ar_o)
        y_ar_n.extend(y_ar_o)
        x_ar_n = list(map(abs, x_ar_n))
        y_ar_n = list(map(abs, y_ar_n))

        Shape.plot(self, max(max(x_ar_n), max(y_ar_n)), max(max(x_ar_n), max(y_ar_n)))


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x = round(x,2)
        self.y = round(y,2)
        self.radius = round(radius,2)
        self.x_old = 0.00
        self.y_old = 0.00
        self.rad_old = 0.00


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
        self.x = round(ans[0],2)
        self.y = round(ans[1],2)
        return (self.x, self.y, self.radius)

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
        self.radius = round(ans[0], 2)

        return self.x, self.y, self.radius


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
        self.x = round(ans[1], 2) + rx
        self.y = round(ans[0], 2) + ry
        return self.x, self.y, self.radius

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

        axes.add_artist(plt.Circle((self.y, self.x), self.radius, color='pink'))
        axes.add_artist(plt.Circle((self.y_old, self.x_old), self.rad_old, linestyle='--', fill=False))

        Shape.plot(self, (abs(self.x) + self.radius)*2, (abs(self.x) + self.radius)*2)


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    print("welcome!")
    while True:
        a1 = input("enter 1 if you want to see the plot after transformation otherwise enter 0")
        if a1 != '1' and a1 != '0':
            print("please enter correct choice")
        else:
            a1 = int(a1)
            break

    while True:
        t = int(input("Number of test cases"))
        if t >= 0:
            break

    for i in range(0, t):

        while True:
            a2 = input("enter 1 if you want to generate a circle, enter 0 to generate a polygon")
            if a2 != '1' and a2 != '0':
                print("please enter correct choice")
            else:
                a2 = int(a2)
                break

        if a2 == 0:
            co_ord = []
            while True:
                n = int(input("enter the number of sides of polygon"))
                if n < 3:
                    print("a polygon must have at least 3 vertices")
                    continue
                else:
                    break

            for j in range(0, n):
                x = input("enter space separated co-ordinates x"+ str(j) + " y" + str(j)).split()
                li = [round(float(x[0]),2), round(float(x[1]),2), 1]
                co_ord.append(li)
                pg = Polygon(co_ord)

            p = int(input("enter the number of queries"))
            print("for translation - t <distance along x> <distance along y>")
            print("for Scaling - s <scaling factor along x> <scaling factor along y>")
            print("for rotation - r <angle of rotation in deg> <x co-ord of rotation(optional)> <y co-ord of rotation(optional)>")

            if a1 == 0:
                print("Enter Query:  '()' represent optional arguments")
                print("1) r deg (rx) (ry)")
                print("2) t dx (dy)")
                print("3) s sx (sy)")
                print("4) p")

                y_ar = []
                x_ar = []

                for j in range(0, p):
                    print("enter query")
                    q = input().split()
                    y_ar = []
                    x_ar = []
                    for z in range(0, len(pg.poly)):
                        y_ar.append(pg.poly[z][1])
                        x_ar.append(pg.poly[z][0])

                    if q[0] == 't':
                        print(x_ar, y_ar)

                        print(pg.translate(float(q[1]), float(q[2])))

                    elif q[0] == 's':
                        print(x_ar, y_ar)
                        if len(q) == 3:
                            print(pg.scale(float(q[1]), float(q[2])))
                        else:
                            print(pg.scale(float(q[1]), float(q[1])))

                    elif q[0] == 'r':
                        print(x_ar, y_ar)
                        if len(q) == 2:
                            pg.rotate(float(q[1]), 0, 0)
                        elif len(q) == 4:
                            pg.rotate(float(q[1]), float(q[2]), float(q[3]))

                    elif q[0] == 'p':
                        pg.plot()

            if a1 == 1:
                for j in range(0, p):
                    q = input("enter the query").split()

                    if q[0] == 't':
                        pg.translate(float(q[1]), float(q[2]))
                        pg.plot()

                    elif q[0] == 's':
                        if len(q) == 3:
                            pg.scale(float(q[1]), float(q[2]))
                        elif len(q) == 2:
                            pg.scale(float(q[1]), float(q[1]))
                        pg.plot()

                    else:
                        if len(q) ==2 or len(q) == 3:
                            pg.rotate(-float(q[1]), 0, 0)
                        elif len(q) == 4:
                            pg.rotate(-float(q[1]), float(q[2]), float(q[3]))
                        pg.plot()

        elif a2 == 1:
            x = input("enter space seprated x co-ordinate, y co-ordinate and radius of circle").split()
            c = Circle(float(x[0]), float(x[1]), float(x[2]))

            p = int(input("enter the number of queries"))

            if a1 == 0:
                print("Enter Query:  '()' represent optional arguments")
                print("1) r deg (rx) (ry)")
                print("2) t dx (dy)")
                print("3) s sx (sy)")
                print("4) p")

                for j in range(0, p):
                    print("enter the query")
                    q = input().split()

                    if q[0] == 't':
                        print(c.x, c.y, c. radius)

                        print(c.translate(int(q[1]), int(q[2])))

                    elif q[0] == 's':
                        print(c.x, c.y, c.radius)

                        print(c.scale(int(q[1])))

                    elif q[0] == 'r':
                        print(c.x, c.y, c.radius)

                        if len(q) == 2:
                            print(c.rotate(-float(q[1]), 0, 0))
                        elif len(q) == 4:
                            print(c.rotate(-float(q[1]), float(q[2]), float(q[3])))

                    elif q[0] == 'p':
                        c.plot()

            if a1 == 1:
                p = int(input("enter the number of queries"))
                print("for translation - t <distance along x> <distance along y>")
                print("for Scaling - s <scaling factor>")
                print("for rotation - r <angle of rotation in deg> <x co-ord of rotation(optional)> <y co-ord of rotation(optional)>")

                for j in range(0, p):
                    q = input("enter the query").split()

                    if q[0] == 't':
                        c.translate(float(q[1]), float(q[2]))
                        c.plot()

                    elif q[0] == 's':
                        c.scale(float(q[1]))
                        c.plot()

                    else:
                        if len(q) == 2:
                            c.rotate(float(q[1]), 0, 0)
                        elif len(q) == 4:
                            c.rotate(float(q[1]), float(q[2]), float(q[3]))
                        c.plot()


    '''
    c = Circle(2.0, 2.0, 3.0)
    c.rotate(45)
    print(c.radius)
    c.plot()

    l = [[1.0, 1.0, 1.0], [1.0, 5.0, 1.0], [5.0, 5.0, 1.0], [5.0, 1.0, 1.0]]
    p = Polygon(l)
    p.scale(3, 2)
    p.plot()
    '''
