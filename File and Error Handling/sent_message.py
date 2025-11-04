
# Original message
sent_message = 'Hey there! This is a secret message.'

# Open the file in read/write mode
with open('sent_message.txt', 'r+') as file:
    # Write the sent message
    file.write(sent_message)

    # Move cursor to the beginning to read the message
    file.seek(0)
    original_message = file.read()

    # Move cursor to the beginning again to overwrite
    file.seek(0)

    # Message to simulate unsending
    unsent_message = 'This message has been unsent.'

    # Write the new message
    file.write(unsent_message)

    # Truncate the file to match new message length
    file.truncate()

# Print both messages
print("Original message:", original_message)
print("After unsending:", unsent_message)
