# Write a program that prints "true"
# if the Ethereum address is valid; 
# otherwise, print "false." 
# (You can use any Ethereum address from Etherscan for testing.)
import re

def is_valid_ethereum_address(address):
    # Ethereum address regular expression
    eth_address_regex = re.compile(r'^0x[a-fA-F0-9]{40}$')

    # Check if the address matches the regular expression
    return bool(eth_address_regex.match(address))

def main():
    address = input("Enter Ethereum address: ")
    if is_valid_ethereum_address(address):
        print("true")
    else:
        print("false")

while True:
    choice = input("1. Check Ethereum address\n2. Exit\nEnter choice: ")
    if choice == "1":
        main()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")
