#func to profile
#just type @do_profile at the start
# inspired from https://zapier.com/engineering/profiling-python-boss/


"""not used in actual assignment!"""
"""not used in actual assignment!"""
"""not used in actual assignment!"""
"""not used in actual assignment!"""
"""not used in actual assignment!"""
"""not used in actual assignment!"""
"""not used in actual assignment!"""
"""Only for profiling"""

import cProfile
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func
