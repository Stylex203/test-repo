while True:
	inp = input("Inpput what to calc/(exit): ")
	if inp == "exit":
		print("Bye!")
		break
	else:
		print("Result: ", eval(inp))

