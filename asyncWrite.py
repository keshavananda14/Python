import threading
import time

class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out
		
	def run(self):
		f = open(self.out,"a")
		f.write(self.text + '\n')
		f.close()
		time.sleep(2)
		print "Finished Background file write to " + self.out

def Main():
	message = raw_input("Enter the string to Store: ")
	background = AsyncWrite(message,"out.txt")
	background.start()
	print "Program can continue to run while it run in another thread"
	print 100+400
	
	background.join()
	print "Waited untill thread was complte"

if __name__=='__main__':
	Main()
