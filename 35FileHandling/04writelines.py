# The writelines0 method in Python writes a sequence of
# strings to a file. The sequence can be any iterable object,
# such as a list or a tuple.

f = open('35FileHandling/file2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n'] # \n is used to gice enter in the file elements
f.writelines(lines)
f.close()