import re

def Main():

	line = "I think I understand Regular Expressions" 
	matchResult = re.match(r'think', line , re.M|re.I)
	if matchResult:
		print "Match result found " + matchResult.group()
	else:
		print "No match was found"
	searchresult = re.search(r'think',line,re.M|re.I)
	if searchresult:
		print "Serach result found",searchresult.group()

if __name__ == "__main__":
	Main()
