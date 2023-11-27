# --- Day 1: PLACEHOLDER ---


import timeit



def read_input():
    '''Read the input file and return the string data as tuple of int tuples.'''
    with open('./day_01_input.txt', 'r') as file:
        lines = file.read().splitlines()
    
    elves_calories_per_snack = list() # All the elves snack calories lists.
    elf_calories_per_snack = list()

    for line in lines:
        if not line:
            elves_calories_per_snack.append(tuple(elf_calories_per_snack))
            elf_calories_per_snack = list()
            continue

        elf_calories_per_snack.append(int(line))
 
    elves_calories_per_snack = tuple(elves_calories_per_snack)

    return elves_calories_per_snack



def get_top_total_calories(total_calories_per_elf, elf_count=None):
    '''Using the list given go through and create a tuple of however many max calories per elf were asked for.'''

    # Make a copy so we don't mangle the original as we will be removing items from the list as we find the current max item.
    total_calories_per_elf = list(total_calories_per_elf)

    # If no elf_count is proveded, use the entire list.
    elf_count = elf_count or len(total_calories_per_elf)
    
    # Don't allow elf_count to be higher than what is available in the list.
    elf_count = min(elf_count, len(total_calories_per_elf))
    
    # Go through the list however many times we were told and find the current max value and then remove it from the list keep track of those items along the way.
    top_total_calories = list()
    for _i in range(elf_count):
        top_total_calories_for_elf = max(total_calories_per_elf)
        top_total_calories.append(top_total_calories_for_elf)
        total_calories_per_elf.remove(top_total_calories_for_elf)
    
    top_total_calories = tuple(top_total_calories)

    # Here is a more streamlined approach:
    #top_total_calories = sorted(total_calories_per_elf, reverse=True)[0:elf_count]

    return top_total_calories



def run():
    print("TEST")
    return
    elves_calories_per_snack = read_input()

    print('DAY 01')    

    # Part 1 Answer
    total_calories_per_elf = [sum(x) for x in elves_calories_per_snack]
    elf_max_total_calories = max(total_calories_per_elf)
    print(f'Find the Elf carrying the most Calories. How many total Calories is that Elf carrying? : {elf_max_total_calories}') # 69528

    #Part 2 Answer
    top_total_calories = get_top_total_calories(total_calories_per_elf, elf_count=3)
    top_total_calories_sum = sum(top_total_calories)
    print(f'Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total? : {top_total_calories_sum}') # 206152



if __name__ == '__main__':
    start_time = timeit.default_timer()
    run()
    print('Runtime: {} seconds.'.format(round(timeit.default_timer() - start_time, 5)))
