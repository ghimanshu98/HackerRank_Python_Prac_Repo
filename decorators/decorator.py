from generic_div import gen_div

def decorated_smart_div(function):
    def inner_func(a,b):
        if a<b:
            a,b=b,a
        return function(a,b)
    return inner_func


# calling decorated func:

div = decorated_smart_div(gen_div)

div(3,6)