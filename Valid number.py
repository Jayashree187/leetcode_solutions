class Solution(object):

  def isNumber(self, s):
    """:type s: str

    :rtype: bool
    """
    seen_digit = False
    seen_exponent = False
    seen_dot = False

    for i, char in enumerate(s):
      if char.isdigit():
        seen_digit = True
      elif char in "+-":
        # A sign is only valid at the beginning of the string
        # or immediately after an exponent ('e' or 'E').
        if i > 0 and s[i - 1] not in "eE":
          return False
      elif char in ".":
        # A dot is invalid if we have already seen a dot or an exponent.
        if seen_dot or seen_exponent:
          return False
        seen_dot = True
      elif char in "eE":
        # An exponent is invalid if we already saw one
        # or if we haven't seen any digits yet.
        if seen_exponent or not seen_digit:
          return False
        seen_exponent = True
        # Reset seen_digit to ensure digits follow the exponent.
        seen_digit = False
      else:
        return False

    return seen_digit
