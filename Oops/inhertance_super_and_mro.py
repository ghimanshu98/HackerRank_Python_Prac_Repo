# MRO - Method Resolution order

class A:
    def __init__(self) -> None:
        print('In init of class A')

    def feature1(self):
        pass

    def feature2(self):
        pass


class B1(A):  # Single lever inheritance - B <- A
    # def __init__(self) -> None:
    #     print('In init of class B')

    def feature3(self):
        pass

    def feature4(self):
        pass


class B2(A):  # Single lever inheritance - B <- A
    def __init__(self) -> None:
        print('In init of class B2')

    def feature3(self):
        pass

    def feature4(self):
        pass

class B3(A):  # Single lever inheritance - B <- A  and use of SUPER method
    def __init__(self) -> None:
        super().__init__()
        print('In init of class B3')

    def feature3(self):
        pass

    def feature4(self):
        pass

class B4():  # Single lever inheritance - B <- A  and use of SUPER method
    def __init__(self) -> None:
        print('In init of class B4')

    def feature3(self):
        pass

    def feature4(self):
        pass

# Multilevel Inheritance
class C(B4,A):
    def __init__(self) -> None:
        super().__init__()
        print("In init of class C")




b_obj = B1()
print()
b2_obj = B2()
print()
b3_obj = B3()

print()
c_obj = C()