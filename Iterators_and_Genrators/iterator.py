nums = [7,8,5,9]

iter_obj = iter(nums)

try:
    print(iter_obj.__next__())
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
except StopIteration as s:
    print("Iterator is Exhausted")