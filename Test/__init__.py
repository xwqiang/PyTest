import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            print 'begin'
            func(*args, **kw)
            print 'end'
        return wrapper
    return decorator


@log("test")
def myfun(x=12):
    print x
    
myfun(232) 