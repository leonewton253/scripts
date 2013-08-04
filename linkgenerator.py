f = open("copy", "a")

for x in range(0, 84):
  f.write("python getnewlinks.py http://...(URL goes here)/?paged=%d" % (x))
	f.write("\n")

"""
Script that writes to file named "copy" with a python command looping from 0 to 84.
It thus generates the nessesary command to execute the command with every URL from page 1 to 84.
I just copy and pasted this list into the terminal. Still need to figure out how to feed the list into
getnelinks.py process function.
"""
