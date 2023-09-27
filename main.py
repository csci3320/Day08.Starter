from data import data

class ArrayList:

    def __init__(self):
        self.block = [0] * 2
        self.last_index = 0

    def expand(self):
        new_size = len(self.block) * 2
        new_block = [0] * new_size
        for i in range(len(self.block)):
            new_block[i] = self.block[i]
        self.block = new_block

    def add(self, value):
        if self.last_index >= len(self.block):
          self.expand()
        self.block[self.last_index] = value
        self.last_index += 1
        return self  # Do not change this final line

    def remove(self, value):
        for i in range(self.last_index):
            if self.block[i] == value:
                for j in range(i, self.last_index-1):
                    self.block[j] = self.block[j+1]
                self.last_index -= 1
                return self
        return self  # Do not change this final line

    def size(self):
        return self.last_index

    def contains(self, value):
        for i in range(self.last_index):
            if self.block[i] == value:
                return True
        return False

    def asList(self):
        to_return = [0] * self.last_index
        for i in range(self.last_index):
            to_return[i] = self.block[i]
        return to_return
    
print("Start")
list = ArrayList()
list.add(1)
list.add(2)
list.add(3)
print(list.asList())
print(list.size())
print(list.contains(2))
print(list.contains(4))
list.remove(1)
print(list.asList())
list.remove(3)
print(list.asList())

for d in data:
    list.add(d)

print(list.asList())
