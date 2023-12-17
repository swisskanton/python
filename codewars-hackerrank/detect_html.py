"""
Detect HTML Tags, Attributes and Attribute Values

You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:
Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]

Sample Input
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

Sample Output
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            [print(f'-> {atr[0]} > {atr[1]}') for atr in attrs]

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            [print(f'-> {atr[0]} > {atr[1]}') for atr in attrs]


parser = MyHTMLParser()
html = ''
for _ in range(int(input())):
    html += input()
parser.feed(html)
parser.close()
