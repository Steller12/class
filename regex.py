import re

value = "This is a string"
output = re.search("^This.*string$", value)

print(output)

pattern = r"^(?=.[A-Za-z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!%*#?&]{8,}$"

# "" - common use of regular expressions is to validate user input. For example, you could use a regular expression to ensure that a password meets certain criteria, like containing at least one letter, one digit, and one special character.

# ^ - In a regular expression pattern, the caret (^) symbol has a special meaning. When it appears at the start of a character class (a group of characters inside square brackets), it negates the class. This means that it matches any character that is not in the class.

# ? - Zero or one occurrences

# = - the equal sign (=) is used in lookahead and lookbehind assertions. Lookahead and lookbehind assertions are special syntax that allow you to check whether a certain pattern appears before or after the current match, without including it in the actual match.

# . - Any character (except newline character)

# * - 	Zero or more occurrences

# [] - A set of characters

# () - Capture and group

# \ - Signals a special sequence (can also be used to escape special characters)

# {} - 	Exactly the specified number of occurrences

# $ - 	Ends with