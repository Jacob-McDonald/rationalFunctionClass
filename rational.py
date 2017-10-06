import numpy as np

class rational():

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __add__(self,other):

        new_num = np.polyadd(np.polymul(self.n, other.dim) + np.polymul(other.num, self.d))
        new_dim = np.polymul(self.d, other.dim)

        return rational(new_num,new_dim)


    def __sub__(self, other):
        new_num = np.polysub(np.polymul(self.n, other.dim) + np.polymul(other.num, self.d))
        new_dim = np.polymul(self.d, other.dim)
        return rational(new_num, new_dim)


    def __mul__(self, other):

        new_num = np.polymul(self.n, other.num)
        new_dem = np.polymul(self.n, other.num)
        return rational(new_num,new_dem)



    def __truediv__(self, other):

        new_num = np.polymul(self.n, other.num)
        new_dem = np.polymul(self.n, other.num)
        return rational(new_num, new_dem)

    def __str__(self):

        order_n = len(self.n)-1

        order_d = len(self.d)-1

        max_order = max(order_n, order_d)

        text = str(np.poly1d(self.n)) + '\n'+ (max_order) * '------' + '--' +'\n' + str(np.poly1d(self.d))

        return text


    def roots(self):
        return np.roots(self.n)

    def yint(self):
        return np.polyval(self.n, 0) / np.polyval(self.d, 0)

    def asymv(self):
        return np.roots(self.d)