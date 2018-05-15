from string import Template

class myTemplate(Template):
	delimiter = '#'
def Main():
	cart = []
	cart.append(dict(item="Coke", price=5, qty=2))
	cart.append(dict(item="Cake", price=10, qty=3))
	cart.append(dict(item="Pepsi", price=9, qty=4))

	t = myTemplate("#qty * #item = #price")
	total = 0
	print "cart:"
	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "Total: " + str(total)

if __name__=="__main__":
	Main()
