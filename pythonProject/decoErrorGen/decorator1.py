def some_decorator(fn):
    def wrap(*args,**kwargs):
        print("********")
        fn(*args,**kwargs)
        print('********')
    return wrap
@some_decorator
def print_hello(greeting,emoji=':)'):
    print(greeting,emoji)

print_hello('Byeeeeee')