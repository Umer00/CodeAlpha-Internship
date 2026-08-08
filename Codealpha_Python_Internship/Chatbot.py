import datetime
import random   # wapis add kar diya sirf jokes ke liye

def chatbot():
    name = "CodeAlpha Bot"
    print(f"🤖 {name}: Hello! I am {name}. Type 'help' to see menu. Type 'bye' to exit.\n")

    jokes = [
        "Why do Python programmers prefer snakes? Because they don't like bugs!",
        "Why did the computer go to therapy? Too many bytes!",
        "What do you call a fake noodle? An Impasta!",
        "Why don't programmers like nature? It has too many bugs.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem."
        "Unemployment is better than an unpaid internship"

    ]

    while True:
        user_input = input("You: ").lower().strip()

        # 1. Exit
        if "bye" in user_input or "exit" in user_input:
            print(f"Bot: Goodbye! Have a great day 👋")
            break

        # 2. Greetings
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print(f"Bot: Hey there! How can I help you today?")

        # 3. How are you
        elif "how are you" in user_input:
            print("Bot: I'm running great, thanks for asking! How are YOU?")

        # 4. Name
        elif "name" in user_input:
            print(f"Bot: My name is {name}. What's your name?")
            user_name = input("You: ")
            print(f"Bot: Nice to meet you, {user_name.title()}!")

        # 5. Time
        elif "time" in user_input:
            now = datetime.datetime.now()
            print(f"Bot: Current time is {now.strftime('%I:%M %p')}")

        # 6. Date
        elif "date" in user_input:
            now = datetime.datetime.now()
            print(f"Bot: Today's date is {now.strftime('%d %B %Y')}")

        # 7. Joke - ab direct bole to bhi random
        elif "joke" in user_input or "funny" in user_input:
            print(f"Bot: {random.choice(jokes)}")

        # 8. Calculator
        elif "calculate" in user_input or any(op in user_input for op in ['+', '-', '*', '/']):
            try:
                result = eval(user_input)
                print(f"Bot: The answer is {result}")
            except:
                print("Bot: I couldn't calculate that. Try something like: 5 + 3")

        # 9. Help Menu with Number Selection
        elif "help" in user_input:
            print("\nBot: Please choose an option:")
            print(" 1. Greet me")
            print(" 2. Tell Time")
            print(" 3. Tell a Random Joke")   # yahan update kiya
            print(" 4. Tell Date")
            print(" 5. Calculator")
            print(" 6. Exit")
            choice = input("You: ")

            if choice == "1":
                print("Bot: Hey there! How can I help you today?")
            elif choice == "2":
                now = datetime.datetime.now()
                print(f"Bot: Current time is {now.strftime('%I:%M %p')}")
            elif choice == "3":   # RANDOM JOKE
                print(f"Bot: {random.choice(jokes)}")
            elif choice == "4":
                now = datetime.datetime.now()
                print(f"Bot: Today's date is {now.strftime('%d %B %Y')}")
            elif choice == "5":
                calc = input("Bot: Enter calculation like 5+3: ")
                try:
                    print(f"Bot: The answer is {eval(calc)}")
                except:
                    print("Bot: Invalid calculation")
            elif choice == "6":
                print(f"Bot: Goodbye! Have a great day 👋")
                break
            else:
                print("Bot: Invalid choice. Please select 1-6")

        # 10. Default - fixed reply
        else:
            print("Bot: I didn't get that. Type 'help' to see the menu.")

chatbot()