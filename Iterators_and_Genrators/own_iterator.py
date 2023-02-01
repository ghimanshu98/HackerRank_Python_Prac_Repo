class Topten:
    def __init__(self) -> None:
        self.num = 1

    # creates and return an object of iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


obj = Topten()

print(obj)

print(next(obj))
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

for i in obj:
    print(i)