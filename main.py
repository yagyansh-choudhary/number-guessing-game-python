"""
Number Guessing Game
====================

A fun, interactive console-based number guessing game built with Python.

This game generates a random number between 1 and 100, and the player
attempts to guess it. After each guess, the game provides hints indicating
whether the guess was too high or too low.

Course: ETCCCP105 - Computer Science Fundamentals & Career Pathways
Assignment: 04 - Build & Document a Mini Project Using GitHub and VS Code
Institution: K.R. Mangalam University, School of Engineering & Technology
Program: B.Tech CSE (Specialization in AI & Robotics)
Faculty: Prof. Rajesh Kumar

Author: [Your Name]
Enrollment No: [Your Enrollment Number]
Date: [Current Date]

Features:
---------
- Random number generation (1-100)
- User input with validation
- Intelligent hint system (Too High/Too Low)
- Attempt counter
- Performance rating based on attempts
- Play again functionality
- Error handling for invalid inputs

Usage:
------
Run the script using Python 3.x:
    $ python main.py
    or
    $ python3 main.py

License:
--------
This project is created for academic purposes as part of ETCCCP105 coursework.

Version: 1.0
"""

# ============================================================================
# IMPORTS
# ============================================================================

import random  # For generating random numbers

# ============================================================================
# CONSTANTS
# ============================================================================

# Game configuration constants
MIN_NUMBER = 1       # Minimum number in range
MAX_NUMBER = 100     # Maximum number in range

# Performance rating thresholds
EXCELLENT_THRESHOLD = 5   # Attempts <= 5 = Excellent
GOOD_THRESHOLD = 10       # Attempts <= 10 = Good

# ============================================================================
# MAIN GAME FUNCTION
# ============================================================================

def number_guessing_game():
    """
    Main function to run the Number Guessing Game.
    
    This function implements the complete game logic including:
    - Welcome message display
    - Random number generation
    - Game loop for guessing
    - Input validation and error handling
    - Hint system (Too High/Too Low)
    - Attempt counting
    - Performance rating
    - Play again functionality
    
    The game continues until the player chooses not to play again.
    
    Parameters:
        None
    
    Returns:
        None
    
    Example:
        >>> number_guessing_game()
        # Starts the interactive game session
    """
    
    # ========================================================================
    # WELCOME MESSAGE
    # ========================================================================
    
    # Display decorative welcome banner
    print("\n" + "=" * 60)
    print("         🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯")
    print("=" * 60)
    
    # Display game instructions
    print("\nHow to Play:")
    print("  • I will think of a number between 1 and 100")
    print("  • You try to guess it in as few attempts as possible")
    print("  • I will tell you if your guess is too HIGH or too LOW")
    print("  • Keep guessing until you find the correct number!")
    print("\n" + "-" * 60)
    
    # ========================================================================
    # GAME INITIALIZATION
    # ========================================================================
    
    # Variable to control the play again loop
    play_again = 'yes'
    
    # Track total games played in this session
    total_games = 0
    best_score = float('inf')  # Initialize with infinity for comparison
    
    # ========================================================================
    # MAIN GAME LOOP (Play Again Loop)
    # ========================================================================
    
    while play_again.lower() in ['yes', 'y']:
        
        # Increment game counter
        total_games += 1
        
        # --------------------------------------------------------------------
        # Generate Secret Number
        # --------------------------------------------------------------------
        
        # Generate a random integer between MIN_NUMBER and MAX_NUMBER (inclusive)
        secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        
        # Initialize game variables for this round
        attempts = 0        # Counter for number of guesses
        guessed = False     # Flag to track if correct guess was made
        
        # Display round information
        print(f"\n🎮 GAME #{total_games}")
        print(f"\nI have selected a secret number between {MIN_NUMBER} and {MAX_NUMBER}.")
        print("Try to guess it!\n")
        
        # --------------------------------------------------------------------
        # Guessing Loop
        # --------------------------------------------------------------------
        
        while not guessed:
            
            # ----------------------------------------------------------------
            # Get User Input with Validation
            # ----------------------------------------------------------------
            
            try:
                # Prompt user for input
                user_input = input("🔢 Enter your guess: ")
                
                # Check for quit command
                if user_input.lower() in ['quit', 'q', 'exit']:
                    print("\n👋 Thanks for playing! See you next time!")
                    return  # Exit the function
                
                # Check for help command
                if user_input.lower() in ['help', 'h', '?']:
                    print("\n📖 HELP:")
                    print("  • Enter a number between 1-100")
                    print("  • Type 'quit' to exit the game")
                    print("  • Use the hints to narrow down your guess")
                    print("  • Tip: Start with 50 and use binary search!\n")
                    continue  # Skip to next iteration
                
                # Convert input to integer
                user_guess = int(user_input)
                
                # ----------------------------------------------------------------
                # Validate Input Range
                # ----------------------------------------------------------------
                
                if user_guess < MIN_NUMBER or user_guess > MAX_NUMBER:
                    print(f"⚠️  Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
                    print("   (This guess doesn't count!)\n")
                    continue  # Skip to next iteration without incrementing attempts
                
                # ----------------------------------------------------------------
                # Increment Attempt Counter
                # ----------------------------------------------------------------
                
                attempts += 1
                
                # ----------------------------------------------------------------
                # Compare Guess with Secret Number
                # ----------------------------------------------------------------
                
                if user_guess < secret_number:
                    # Guess is too low
                    difference = secret_number - user_guess
                    
                    # Provide hint intensity based on difference
                    if difference > 30:
                        print("📉 Too Low! Way too low... Try a much higher number.\n")
                    elif difference > 15:
                        print("📉 Too Low! Try a higher number.\n")
                    else:
                        print("📉 Too Low! But you're getting close!\n")
                
                elif user_guess > secret_number:
                    # Guess is too high
                    difference = user_guess - secret_number
                    
                    # Provide hint intensity based on difference
                    if difference > 30:
                        print("📈 Too High! Way too high... Try a much lower number.\n")
                    elif difference > 15:
                        print("📈 Too High! Try a lower number.\n")
                    else:
                        print("📈 Too High! But you're getting close!\n")
                
                else:
                    # Correct guess!
                    guessed = True
                    
                    # --------------------------------------------------------
                    # Victory Message
                    # --------------------------------------------------------
                    
                    print("\n" + "🎉" * 20)
                    print(f"\n   ✅ CONGRATULATIONS! YOU GUESSED IT! ✅")
                    print(f"\n   The secret number was: {secret_number}")
                    print(f"   Total attempts: {attempts}")
                    
                    # --------------------------------------------------------
                    # Performance Rating
                    # --------------------------------------------------------
                    
                    print("\n   📊 Performance Rating:")
                    
                    if attempts == 1:
                        # Perfect luck!
                        print("   🏆 INCREDIBLE! First try! Are you psychic?!")
                        rating = "Legendary"
                    elif attempts <= EXCELLENT_THRESHOLD:
                        # Excellent performance
                        print("   🌟 EXCELLENT! Outstanding guessing skills!")
                        rating = "Excellent"
                    elif attempts <= GOOD_THRESHOLD:
                        # Good performance
                        print("   👍 GOOD JOB! Nice work!")
                        rating = "Good"
                    elif attempts <= 15:
                        # Average performance
                        print("   👌 NOT BAD! Room for improvement.")
                        rating = "Average"
                    else:
                        # Needs practice
                        print("   💪 KEEP PRACTICING! You'll get better!")
                        rating = "Beginner"
                    
                    print(f"   Rating: {rating}")
                    
                    # --------------------------------------------------------
                    # Update Best Score
                    # --------------------------------------------------------
                    
                    if attempts < best_score:
                        best_score = attempts
                        if total_games > 1:
                            print(f"\n   🏆 NEW BEST SCORE! {best_score} attempts!")
                    
                    print("\n" + "🎉" * 20)
            
            # ----------------------------------------------------------------
            # Error Handling
            # ----------------------------------------------------------------
            
            except ValueError:
                # Handle non-numeric input
                print("❌ Invalid input! Please enter a valid number.")
                print("   (Type 'help' for assistance or 'quit' to exit)\n")
            
            except KeyboardInterrupt:
                # Handle Ctrl+C
                print("\n\n👋 Game interrupted. Thanks for playing!")
                return
        
        # --------------------------------------------------------------------
        # Play Again Prompt
        # --------------------------------------------------------------------
        
        print("\n" + "-" * 60)
        print(f"\n📈 Session Statistics:")
        print(f"   Games Played: {total_games}")
        print(f"   Best Score: {best_score} attempts")
        print()
        
        # Ask if user wants to play again
        play_again = input("🔄 Do you want to play again? (yes/no): ").strip()
        
        # Validate play again input
        while play_again.lower() not in ['yes', 'y', 'no', 'n']:
            print("   Please enter 'yes' or 'no'.")
            play_again = input("🔄 Do you want to play again? (yes/no): ").strip()
    
    # ========================================================================
    # FAREWELL MESSAGE
    # ========================================================================
    
    print("\n" + "=" * 60)
    print("         👋 THANK YOU FOR PLAYING! 👋")
    print("=" * 60)
    print(f"\n📊 Final Statistics:")
    print(f"   Total Games Played: {total_games}")
    print(f"   Best Score: {best_score} attempts")
    print("\n🌟 Hope you enjoyed the game! See you next time! 🌟")
    print("\n" + "=" * 60 + "\n")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    """
    Entry point of the program.
    
    This block ensures that the game only runs when the script is executed
    directly (not when imported as a module).
    """
    
    # Run the main game function
    number_guessing_game()


# ============================================================================
# END OF FILE
# ============================================================================
