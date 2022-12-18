import time
import os
# Define the length of the countdown in seconds
countdown_length = 10

# Explaining Rules
print("Write the given phrase as fast as you can, after the Countdown Phrase")


# Create a for loop to count down from the countdown length to zero
for i in range(countdown_length, 0, -1):
    # Print the current countdown value
    print(i)

    # Sleep for one second before starting the next iteration
    time.sleep(1)
    os.system("cls")

# Print a message when the countdown is finished
print("Countdown finished!")
print('Write...Write...Write...Write !!!')

def measure_typing_speed():
    # Start the timer
    start_time = time.time()

    # Prompt the user to type the given word or phrase
    print("Your Phrase is")
    time.sleep(2)
    
    typed_phrase = input("Please type the following phrase as quickly as possible: ")

    

    # Stop the timer after the user has typed the phrase
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Calculate the typing speed in words per minute
    words_per_minute = len(typed_phrase.split()) / elapsed_time * 60

    # Print the elapsed time and the typing speed
    print(f"Elapsed time: {int(elapsed_time)} seconds")
    print(f"Typing speed: {int(words_per_minute)} words per minute")

measure_typing_speed()
