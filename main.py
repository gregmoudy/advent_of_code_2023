# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; 
#     on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is 
# unlocked when you complete the first. Each puzzle grants one star. Good luck!

import glob
import os

# Get all the day_<int>.py files and import them.
DAY_PYTHON_FILES = glob.glob('./day_*.py')
DAY_MODULE_NAMES = [os.path.splitext(os.path.basename(x))[0] for x in DAY_PYTHON_FILES]
for day_module_name in DAY_MODULE_NAMES:
    exec(f'import {day_module_name}')


if __name__ == '__main__':
    # Run each day solver to view the output and timings.
    for day_module_name in DAY_MODULE_NAMES:
        eval(f'{day_module_name}.run()')
