# this is my first github addition

def print_menu():
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")

def get_input():
	choice = int((input("Please enter an option: ")))
	return choice

def encode(password):
    encoded_pass = ""
    for c in password:
        encoded_pass += str((int(c) + 3) % 10)
    return encoded_pass

def decode(encoded_pass):
	decoded_pass = "Decoded_Password_Here"
	print(f"The decoded {encoded_pass} is {decoded_pass}")

if __name__ == "__main__":
	while True:
		print_menu()
		choice = get_input()
		if choice == 1:
			password = input("Please enter your password to encode: ")
			encoded_pass = encode(password)
			print(f"Your password has been encoded and stored!")
		elif choice == 2:
			og_pass = decode(encoded_pass)
			print(f"The encoded password is {encoded_pass}, and the original password is decoded_pass.")
		elif choice == 3:
			break
		else:
			print("Invalid option, try again.")


