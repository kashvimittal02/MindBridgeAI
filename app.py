"""
app.py

Main entry point for MindBridge AI.
"""

from chatbot import MindBridge


def main():
    """
    Starts the chatbot.
    """

    # Create the chatbot
    bot = MindBridge()

    print("=" * 60)
    print("Welcome to MindBridge AI")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        # Get user input
        user_input = input("\nYou: ")

        # Exit
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        # Generate response
        response = bot.chat(user_input)

        print(f"\nMindBridge: {response}")


if __name__ == "__main__":
    main()