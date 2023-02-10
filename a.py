"""HELLO"""
import os

def get_score(filepath : str) -> float:
    """This method will return the score by given filepath"""
    output_stream = os.popen('pylint ' + filepath)
    output = output_stream.read()
    print(output)
    for index in range(len(output.split())):
        if output.split()[index] == 'at':
            return float(output.split()[index + 1].replace('/10', ''))

print(get_score('a.py'))
