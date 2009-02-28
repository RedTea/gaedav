"""
Implement cache mechanism.
"""
import logging

def sessioncached(f):
    """
    The cache only live in one session.
    """
    cache_dict = dict()  # used by the inner function
    def cached_func(*args, **kwargs):
        t = (args, kwargs.items())
        try:
            hash(t)
            key = t
        except TypeError:
            try:
                import pickle
                key = pickle.dumps(t)
            except pickle.PicklingError:
                logging.warn("Cache FAIL: can't hash %s(args=%s, kwargs=%s)", repr(f), repr(args), repr(kwargs))
                return f(*args, **kwargs)
        if cache_dict.get(key) is not None:
            logging.info("Cache HIT: %s(args=%s, kwargs=%s)", repr(f), repr(args), repr(kwargs))
            return cache_dict[key]
        logging.info("Cache MISS: %s(args=%s, kwargs=%s)", repr(f), repr(args), repr(kwargs))
        value = f(*args, **kwargs)
        cache_dict[key]=value
        return value
    try:
        cached_func.func_name = f.func_name
    except AttributeError:
        # for class method which has no func_name
        pass
    return cached_func


