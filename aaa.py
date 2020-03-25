#!/usr/bin/env python

import time
print("Content-Type: text/html\n\n")  # html markup follows

timeStr = time.strftime("%c") # obtains current time

htmlFormat = """
<html>
 <Title>The Time Now</Title>
<body>
 <p>The current date and time is:  {timeStr}</p>
</body>
</html> """

print(htmlFormat.format(**locals()))  # see {timeStr} embedded above
