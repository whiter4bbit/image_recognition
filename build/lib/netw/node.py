class Node(object):
    def __init__(self):
        self.value = 0.0
        self.forwards = []
        self.backwards = []

    def activate(self):
        self.value = 0.0
        for con in self.backwards:
            self.value+=con.backward.value*con.weight
        return self.value

