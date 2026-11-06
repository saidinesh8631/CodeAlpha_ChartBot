"""
CodeAlpha - Python Programming Internship
Task 3 : Basic Chatbot

"""

import os
import sys
import datetime
import random

# Enable UTF-8 output encoding on Windows terminals if supported
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Enable ANSI color escape sequence processing on Windows
if sys.platform == "win32":
    os.system("")


# Terminal Color Codes
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # Foreground Colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


def print_banner():
    
    width = 56
    line = f"{Color.CYAN}{Color.BOLD}{'=' * width}{Color.RESET}"
    title = f"{Color.YELLOW}{Color.BOLD}      Welcome to  Basic Chatbot!       {Color.RESET}"
    subtitle = f"{Color.MAGENTA}{Color.BOLD}          Interactive Python Assistant          {Color.RESET}"

    print(line)
    print(title)
    print(subtitle)
    print(line)
    print()


def get_response(user_input, user_name="User"):
    """
    Evaluates user input string and returns predefined replies
    using clean if-elif-else logic matching the task guidelines.
    """
    text = user_input.lower().strip()

    # 1. Greetings
    if text in ["hello", "hi", "hey", "howdy"]:
        return f"Hi {user_name}! How can I help you today?"

    elif "good morning" in text:
        return f"Good morning, {user_name}! Wishing you a productive day ahead!"

    elif "good afternoon" in text:
        return f"Good afternoon, {user_name}! Hope your day is going well!"

    elif "good evening" in text:
        return f"Good evening, {user_name}! How can I assist you tonight?"

    elif "good night" in text:
        return f"Good night, {user_name}! Have a restful night and sweet dreams!"

    # 2. Status & Well-being
    elif "how are you" in text or text == "how r u" or "how are things" in text:
        return "I'm fine, thanks for asking! How are you doing today?"

    elif "i am good" in text or "i am fine" in text or "doing well" in text:
        return "That's great to hear! Keep that positive energy going!"

    # 3. Identity & Creator
    elif "what is your name" in text or "who are you" in text:
        return "I am a simple rule-based AI Chatbot created for CodeAlpha!"

    elif "who created you" in text or "who made you" in text:
        return f"I was built using Python by as part of the CodeAlpha internship!"

    # 4. Exit / Goodbye
    elif text in ["bye", "goodbye", "exit", "quit", "cya", "see you"]:
        return f"Goodbye, {user_name}! Wishing you all the best!"

    # 5. Help & Available Questions
    elif text in ["help", "what can you do", "commands", "menu", "questions"]:
        return (
            "Here are some questions you can ask me:\n"
            "  - Greetings: 'hello', 'how are you', 'good morning'\n"
            "  - Python: 'what is python', 'who created python', 'what is pip'\n"
            "  - AI & Tech: 'what is ai', 'what is machine learning'\n"
            "  - Internship: 'what is codealpha', 'what are the tasks', 'what is task 1', 'internship duration'\n"
            "  - Utilities: 'what time is it', 'what is today date'\n"
            "  - Fun: 'tell me a joke', 'tell me a fact', 'what is your favorite color'\n"
            "  - Exit: type 'bye' or 'exit'"
        )

    # 6. Python & Programming Questions
    elif "who created python" in text or "who invented python" in text:
        return "Python was created by Guido van Rossum and was first released in 1991."

    elif "what is python" in text:
        return "Python is a high-level, easy-to-read programming language widely used in AI, web dev, and automation."

    elif "what is pip" in text:
        return "PIP stands for 'Pip Installs Packages'. It is the standard package manager used to install Python libraries."

    elif "what is a variable" in text:
        return "In programming, a variable is a named storage container used to hold data values in memory."

    # 7. AI & Machine Learning Questions
    elif "what is ai" in text or "what is artificial intelligence" in text:
        return "Artificial Intelligence (AI) is the simulation of human intelligence by machines to reason, learn, and problem-solve."

    elif "what is machine learning" in text or "what is ml" in text:
        return "Machine Learning (ML) is a branch of AI that enables systems to learn and improve from experience without explicit programming."

    # 8. CodeAlpha Internship Questions
    elif "what is codealpha" in text or "about codealpha" in text:
        return "CodeAlpha is a software company providing student internships in Python, AI, Web Development, and more."

    elif "what are the tasks" in text or "task list" in text:
        return (
            "CodeAlpha Python Programming Tasks:\n"
            "  - Task 1: Hangman Game (Console-based word guessing game)\n"
            "  - Task 2: Stock Portfolio Tracker (Investment value calculation)\n"
            "  - Task 3: Task Automation (File organizer or email scraper)\n"
            "  - Task 4: Basic Chatbot (Simple rule-based conversational agent)"
        )

    elif "task 1" in text or "hangman" in text:
        return "Task 1 is 'Hangman Game': A text-based console game where players guess words one letter at a time within 6 incorrect tries."

    elif "task 2" in text or "portfolio" in text or "stock" in text:
        return "Task 2 is 'Stock Portfolio Tracker': Calculates total investment based on stock prices of top companies."

    elif "task 3" in text or "automation" in text:
        return "Task 3 is 'Task Automation': Python scripts to automate repetitive tasks like sorting files or extracting data."

    elif "task 4" in text or "chatbot" in text:
        return "Task 4 is 'Basic Chatbot': A rule-based conversational agent using if-elif, functions, and loops."

    elif "internship duration" in text or "how long is the internship" in text:
        return "The CodeAlpha Python Programming Internship is designed to be completed in 4 weeks, with each task taking approximately 1 week."
    
    elif "certificate" in text:
        return "CodeAlpha issues a verified completion certificate after you complete and submit your assigned internship tasks."

    # 9. Time & Date Utilities
    elif "time" in text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in text or "day" in text:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}."

    # 10. Fun & Entertainment
    elif "joke" in text:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why do Java programmers wear glasses? Because they don't C#!",
            "There are 10 types of people: those who understand binary, and those who don't!"
        ]
        return random.choice(jokes)

    elif "fact" in text:
        facts = [
            "Did you know? Python was named after 'Monty Python's Flying Circus', not the snake!",
            "Did you know? The first computer bug was an actual real moth found in a Harvard Mark II computer in 1947!",
            "Did you know? Ada Lovelace is widely considered the world's very first computer programmer!"
        ]
        return random.choice(facts)

    elif "favorite color" in text:
        return "My favorite color is Python Blue and Yellow!"

    # 11. Gratitude
    elif "thank you" in text or "thanks" in text or "thx" in text:
        return f"You're very welcome, {user_name}! Always happy to help."

    # 12. Fallback / Default Response
    else:
        return (
            "I'm sorry, I don't understand that question yet.\n"
            "'bye' to exit."
        )


def chatbot():
    """
    Main chatbot interaction loop using while True and console I/O.
    """
    print_banner()

    # Get user name input
    try:
        user_name = input(f"{Color.BOLD}Enter your name: {Color.RESET}").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        return

    if not user_name:
        user_name = "User"

    # Colorful Welcome Message
    print(f"\n{Color.GREEN}{Color.BOLD}Welcome, {user_name}!{Color.RESET}")
    print(f"{Color.CYAN}Chatbot is ready. Type {Color.RED}'bye'{Color.CYAN} to exit\n")

    # Main Conversation Loop
    while True:
        try:
            prompt = f"{Color.GREEN}{Color.BOLD}{user_name}:{Color.RESET} "
            user_input = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Color.CYAN}{Color.BOLD}Bot:{Color.RESET} Goodbye, {user_name}!")
            break

        # Ignore empty enter presses
        if not user_input:
            continue

        # Get bot response using if-elif logic
        reply = get_response(user_input, user_name)

        # Print Bot Response
        print(f"{Color.CYAN}{Color.BOLD}Bot:{Color.RESET} {reply}\n")

        # Exit check
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit", "cya", "see you"]:
            break


if __name__ == "__main__":
    chatbot()
