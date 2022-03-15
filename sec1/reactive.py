import rx

def print_number(x):
    print('The number is {}'.format(x))

rx.from_(range(10)).subscribe(print_number)
