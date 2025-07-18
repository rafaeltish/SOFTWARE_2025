# Simple ID to Name program

# You can use a dictionary to store IDs and names
users = {
    "101": "Rafael Wambua",
    "102": "Mary Ndunge",
    "103": "Samuel Mutua"
}

# Ask user to enter their ID
user_id = input("Enter your ID: ")

# Check if ID exists in the dictionary and print name
if user_id in users:
    print("Your name is:", users[user_id])
else:
    print("ID not found.")