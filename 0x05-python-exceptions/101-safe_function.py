#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as m:
        print("Exception: {}".format(m), file=sys.stderr)
        return None
