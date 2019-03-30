""" Function"""
def join_strings(word1, word2):
    """
    :param word1:
    :param word2:
    :return sum:
    """
    return word1 + ' ' + word2

def uplowcase(string):
    """
    :param string:
    :return:
    """
    upcase = 0
    lowcase = 0
    for i in string:
        if i.isupper():
            upcase = upcase + 1
        elif i.islower():
            lowcase = lowcase + 1

    return (upcase, lowcase)
