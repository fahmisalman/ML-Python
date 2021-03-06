class FIS(object):

    def __init__(self, name):
        self.name = name
        self.fuzzification = []

    def tri(self, x, a):
        if x <= a[0]:
            return 0
        elif a[0] < x < a[1]:
            return (x - a[0]) / (a[1] - a[0])
        elif x == a[1]:
            return 1
        elif a[1] < x < a[2]:
            return (a[2] - x) / (a[2] - a[1])
        else:
            return 0

    def trap(self, x, a):
        if x <= a[0]:
            return 0
        elif a[0] < x < a[1]:
            return (x - a[0]) / (a[1] - a[0])
        elif a[1] <= x <= a[2]:
            return 1
        elif a[2] < x < a[3]:
            return (a[3] - x) / (a[3] - a[2])
        else:
            return 0

    def add(self, type, a, s):
        self.fuzzification.append([type, a, s])

    def rule(self, s, x):
        a = []
        for member in self.fuzzification:
            if member[2] == s:
                a = member
        if a[0] == 'tri':
            return self.tri(x, a[1])
        elif a[0] == 'trap':
            return self.trap(x, a[1])


def inference(x1, x2):
    return min(x1, x2)
