#!/usr/bin/python3

def multiple_returns(sentence):
  """
  Returns a tuple containing the length of a string and its first character.

  Args:
      sentence (str): The string to analyze.

  Returns:
      A tuple with the length of the string (int) and the first character (str or None).
  """
  if not sentence:
    return len(sentence), None  # Return length 0 and None for empty string
  return len(sentence), sentence[0]

# Example usage
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
