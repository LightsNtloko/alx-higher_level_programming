#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence:
        # Return a tuple with the length and the first character
        return (len(sentence), sentence[0])
    else:
        # Return a tuple with length 0 and None for the first character
        return (0, None)
