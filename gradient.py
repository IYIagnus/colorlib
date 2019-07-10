# Inspired by martineau:
# https://stackoverflow.com/questions/10901085/range-values-to-pseudocolor
from copy import deepcopy
from colorsys import hsv_to_rgb


# angles of common colors in hsv colorspace
RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA = range(0, 360, 60)


class Gradient(object):
    def __init__(self, minval, maxval, start_hue, stop_hue, s=1., v=1.):
        self.minval = minval
        self.maxval = maxval
        self.start_hue = start_hue
        self.stop_hue = stop_hue
        self.s = s
        self.v = v

    def sample(self, val):
        """ Convert val in range minval..maxval to the range start_hue..stop_hue
            degrees in the HSV colorspace.
        """
        val = max(val, self.minval)
        val = min(val, self.maxval)

        h = (float(val-self.minval) / (self.maxval-self.minval)) * \
            (self.stop_hue-self.start_hue) + self.start_hue

        r, g, b = hsv_to_rgb(h/360, self.s, self.v)
        return r*255, g*255, b*255

    def invert(self, inplace=False):
        if inplace:
            start = self.start_hue
            stop = self.stop_hue
            self.start_hue = stop
            self.stop_hue = start
        else:
            inverted_gradient = deepcopy(self)
            inverted_gradient.stop_hue = self.start_hue
            inverted_gradient.start_hue = self.stop_hue
            return inverted_gradient


class GreenRed(Gradient):
    def __init__(self, minval, maxval):
        super().__init__(minval, maxval, GREEN, RED)
