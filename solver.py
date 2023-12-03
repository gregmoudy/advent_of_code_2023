import os.path
import timeit


class Solver:
    def __init__(self, file):
        dirname = os.path.dirname(file)
        basename = os.path.splitext(os.path.basename(file))[0]

        self._file_input_sample_1 = os.path.join(dirname, basename + '_input_sample_1.txt')
        self._file_input_sample_2 = os.path.join(dirname, basename + '_input_sample_2.txt')
        self._file_input = os.path.join(dirname, basename + '_input.txt')

        self._title = basename.title().replace('_', ' ')


    def read_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()

        return lines
    

    def get_answer(self, data, part2 = False):
        raise NotImplemented


    def run(self):
        start_time = timeit.default_timer()

        print('================================================================================')
        print(self._title)
        print('================================================================================')

        # Part 1 Sample
        if not os.path.exists(self._file_input_sample_1):
            print(f'No sample input file 1 found: {self._file_input_sample_1}')

        else:
            data = self.read_input(self._file_input_sample_1)

            answer_1_sample = self.get_answer(data)
            print(f'Part 1 Sample: {answer_1_sample}')

        # Part 2 Sample
        file_input_sample_2 = self._file_input_sample_2
        if not os.path.exists(file_input_sample_2):
            # Fallback to using the sample 1 input, most of the time it is reused but not always.
            file_input_sample_2 = self._file_input_sample_1
            if not os.path.exists(file_input_sample_2):
                print(f'No sample input file 2 found: {self._file_input_sample_2}')

        if os.path.exists(file_input_sample_2):
            data = self.read_input(file_input_sample_2)

            answer_2_sample = self.get_answer(data, part2 = True)
            print(f'Part 2 Sample: {answer_2_sample}')

        # Part 1 and 2 Answers
        print('\n')
        if not os.path.exists(self._file_input):
            print(f'No input file found: {self._file_input}')

        else:
            data = self.read_input(self._file_input)

            answer_1 = self.get_answer(data)
            print(f'Part 1: {answer_1}')

            answer_2 = self.get_answer(data, part2 = True)
            print(f'Part 2: {answer_2}')

        print('\n')
        print('Runtime: {} seconds.'.format(round(timeit.default_timer() - start_time, 5)))
        #print('================================================================================')
        print('\n')
