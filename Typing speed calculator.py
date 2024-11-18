import time

def typing_speed_calculator():
    print("Typing Speed Calculator")
    print("You will be given a sentence to type. Your typing speed will be measured.")
    
    # The sentence for the user to type
    sentence = "The quick brown fox jumps over the lazy dog."
    print("\nType the following sentence as quickly and accurately as possible:")
    print(f"Sentence: \"{sentence}\"\n")
    
    # Start the timer
    input("Press Enter when you are ready to start...")
    start_time = time.time()
    
    # Get the user input
    user_input = input("\nType the sentence here: ")
    
    # End the timer
    end_time = time.time()
    
    # Calculate the typing duration
    time_taken = end_time - start_time
    
    # Count words in the sentence
    word_count = len(sentence.split())
    
    # Calculate typing speed in WPM
    typing_speed = (word_count / time_taken) * 60
    
    # Accuracy calculation
    accuracy = len([1 for i, j in zip(user_input, sentence) if i == j]) / len(sentence) * 100
    
    # Display the results
    print("\n--- Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")
    
    # Check if the input matches exactly
    if user_input == sentence:
        print("Great! You typed the sentence perfectly.")
    else:
        print("You made some mistakes. Keep practicing!")

# Run the typing speed calculator
typing_speed_calculator()










