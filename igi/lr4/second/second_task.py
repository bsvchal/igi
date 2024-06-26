from zipfile import *
import os
from .service import *

class Task(TextServiceMixin):
    """
    A class that encapsulates the functionality for reading, processing, and zipping text data.

    Attributes:
        __filepath (str): Path to the input text file.
        __output_filepath (str): Path to the output text file where results will be written.
    """

    def __init__(self, path: str = '/home/main/igilab/l4/second/data/data.txt',
                 output_path='/home/main/igilab/l4/second/data/results.txt'):
        """
        Initializes the Task instance with paths for input and output files.

        Args:
            path (str): The file path for reading data.
            output_path (str): The file path for writing results.
        """
        self.__filepath = path
        self.__output_filepath = output_path

    def read_data_from_file(self) -> str:
        """
        Reads data from the file at the specified file path.

        Returns:
            str: The content of the file as a string.
        """
        with open(self.__filepath, 'r') as text:
            return text.read()

    def zip_results(self):
        """
        Zips the results file and prints the details of the zipped items. Removes the original results file after zipping.
        """
        with ZipFile('/home/main/igilab/l4/second/data/results.zip', 'w',
                     compression=ZIP_DEFLATED, compresslevel=3) as zp:
            zp.write(self.__output_filepath, arcname='results.txt')

            for item in zp.infolist():
                print(f"Filename: {item.filename}, Date: {item.date_time}, Size: {item.file_size}")

        os.remove(self.__output_filepath)

    def execute(self):
        """
        Executes the main functionality of the Task class. It reads data, processes it to calculate various statistics,
        writes the results to an output file, and then zips this output file.
        """
        data = self.read_data_from_file()

        amount_of_dot_sentences = self.amount_of_sentences_by_ending_symbol(data, '.')
        amount_of_question_sentences = self.amount_of_sentences_by_ending_symbol(data, '?')
        amount_of_exclaim_sentences = self.amount_of_sentences_by_ending_symbol(data, '!')
        amount_of_sentences = amount_of_dot_sentences + amount_of_question_sentences + amount_of_exclaim_sentences

        with open(self.__output_filepath, 'w') as output:
            print(f'Amount Of Sentences Is { amount_of_sentences }', file=output)
            print(f'Amount Of Sentences Ending With "." Is { amount_of_dot_sentences }.', file=output)
            print(f'Amount Of Sentences Ending With "?" Is { amount_of_question_sentences }.', file=output)
            print(f'Amount Of Sentences Ending With "!" Is { amount_of_exclaim_sentences }.', file=output)
            print(file=output)

            sentences = self.list_of_sentences(data)
            words = self.list_of_words(sentences)

            print(f'Average Sentence Length Is { self.average_sentence_length(sentences) }.', file=output)
            print(f'Average Word Length Is { self.average_word_length(words) }.', file=output)

            print(f'Amount Of Smiles Is { self.amount_of_smiles(data) }.', file=output)
            print(file=output)

            replace_with = input('Enter Symbol To Replace Spaces With: ')[0]
            print(f'Replaced Spaces With "{ replace_with }":', file=output)
            print(data.replace(' ', replace_with), file=output)

            print(file=output)
            print(f'This Text Is { "" if self.is_guid(data) else "Not" } Guid.', file=output)
            print(f'Amount Of Lowercase Letters Is { self.amount_of_lowercase_letters(data) }.', file=output)
            print(f'Amount Of Uppercase Letters Is { self.amount_of_uppercase_letters(data) }.', file=output) 

            word_with_z, index_of_word_with_z = self.first_word_with_letter(words, 'z') 
            print(f'First Letter With Letter "Z" Is { word_with_z }, At Position { index_of_word_with_z }', file=output)

            print(file=output)
            print('Text Without Words Starting With "A":', file=output)
            print(self.remove_words_starting_with(data, 'a'), file=output)

        self.zip_results()