# graphs computation

class Node:             # узел

    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:                     #ребро

    def __init__(self, src, dest):
    # Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest
        
    def __src__(self):
        return self.src.getName() + '=>' + self.dest.getNane()


