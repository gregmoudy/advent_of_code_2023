# --- Day 1: Trebuchet?! ---

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") 
# and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") 
# when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended 
# by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble 
# reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration 
# value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and 
# the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?


# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, 
# two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?


import solver
import re


class Solver(solver.Solver):
    def get_answer(self, data, part2 = False):
        answer = 0

        number_lookup = { 
            '1' : 1, 
            '2' : 2, 
            '3' : 3, 
            '4' : 4, 
            '5' : 5, 
            '6' : 6, 
            '7' : 7, 
            '8' : 8, 
            '9' : 9, 
        }

        if part2:
            number_word_lookup = { 
                'one'   : 1, 
                'two'   : 2, 
                'three' : 3, 
                'four'  : 4, 
                'five'  : 5, 
                'six'   : 6, 
                'seven' : 7, 
                'eight' : 8, 
                'nine'  : 9, 
            }

            number_lookup.update( number_word_lookup )

        for line in data:
            # https://stackoverflow.com/questions/33406313/how-to-match-any-string-from-a-list-of-strings-in-regular-expressions-in-python
            # Join the list on the pipe character |, which represents different options in regex.
            matches = re.findall(r"(?=("+'|'.join(number_lookup.keys())+r"))", line)

            digit_1 = number_lookup[matches[0]]
            digit_2 = number_lookup[matches[-1]]

            number = int(f'{digit_1}{digit_2}')
            answer += number

        return answer
    


def run():
    solver = Solver(__file__)
    solver.run()
    # 54951
    # 55218



if __name__ == '__main__':
    run()
