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








	

