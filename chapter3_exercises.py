# Exercises for chapter 3:

# 3.1 Answer: name 'repeat_lyrics' is not defined

#3.2 - The equation is only running once. 

def print_lyrics():	
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

def repeat_lyrics():
	print_lyrics()
	print_lyrics()
	print_lyrics()

repeat_lyrics()

#3.3: Must put equation before s

def right_justify(s):
	print (70 - len(s) ) * (" ") + s
	
right_justify ("allen")

#3.4

def do_twice(f):
	 f()
	 f()

def print_spam():
	print 'spam'

do_twice(print_spam)

def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')
print ''

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')
print ''












	

