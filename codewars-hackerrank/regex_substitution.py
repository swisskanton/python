"""
https://www.hackerrank.com/challenges/re-sub-regex-substitution
"""
import re


# Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)


print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))


html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

# remove comment
print(re.sub("(<!--.*?-->)", "", html))


def change_to_and_or(match):
    return ' and ' if match.group(0) == ' && ' else ' or '


test1 = ["a = 1;", "b = input();", "", "if a + b > 0 && a - b < 0:", "    start()", "elif a*b > 10 || a/b < 1:",
         "    stop()", "print set(list(a)) | set(list(b))", "", "#Note do not change &&& or ||| or & or |",
         "#Only change those '&&' which have space on both sides.",
         "#Only change those '|| which have space on both sides."]

print('\ntest1: ')
for row in test1:
    line = re.sub(r"( && )|( \|\| )", change_to_and_or, row)
    while line != row:
        line = row
        row = re.sub(r"( && )|( \|\| )", change_to_and_or, row)
    print(line)


test2 = """
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides."""

print('\ntest2: ')
s = re.sub(r" && ", ' and ', test2)
print(re.sub(r" \|\| ", ' or ', s))
