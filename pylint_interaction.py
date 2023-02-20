"""THIS SCRIPT WAS MADE TO SIMPLY INTRACT WITH PYLINT"""

#region Libraries
import os
#endregion

#region Variables

#endregion


def get_score(filepath):
    """This method will return the score by given filepath"""
    if filepath == '':
        return
    output_stream = os.popen('pylint ' + filepath)
    output = output_stream.read()
    for index in range(len(output.split())):
        if output.split()[index] == 'at':
            score_str = output.split()[index + 1].replace('/10', '')
            
            try:
                score = float(score_str)
            except ValueError:
                return 0.0
            return score


def get_output_lines(filepath) -> list:
    """This method will return the whole output in lines by given filepath"""
    if filepath == '':
        return
    output_stream = os.popen('pylint ' + filepath)
    output = output_stream.read().split('\n')
    # remove extra elements from output list
    output = output[1:-5]
    return output


def get_output_warnings(filepath) -> list:
    """This method will return the output's in lines by given filepath"""
    results = []
    output_lines = get_output_lines(filepath)
    for line in output_lines:
        fifth_colon = line.find(':', line.find(':', line.find(':', line.find(':') + 1) + 1) + 1)
        result = line[fifth_colon + 2:]
        results.append(result)
    return results




# pylint's warning:
# format = filename.py:linenum:colnum: warning_code: warning message (warning msg inshort)
# example = Test.py:6:0: C0103: Constant name "c" doesn't conform to UPPER_CASE naming style (invalid-name)

# let's imagine player have 4 warnings in some specific task of a level
# what player can do :
#   1. pay some coins to get warning highlight or details
#   2. 



# db : u3
# os : u3
# os : u4
# pp : u4
# se : u3