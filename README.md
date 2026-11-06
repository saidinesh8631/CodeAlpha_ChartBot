# Basic Chatbot 🤖

This project was developed as part of the **CodeAlpha Python Programming Internship**.

---

## 📋 Official Task Guidelines (From Instructions Sheet)

| Item | Details Specified by CodeAlpha |
| :--- | :--- |
| **Task Goal** | Build a simple rule-based conversational chatbot. |
| **Input Scope** | User inputs like: `"hello"`, `"how are you"`, `"bye"`, and more. |
| **Predefined Replies** | Replies like: `"Hi!"`, `"I'm fine, thanks!"`, `"Goodbye!"`. |
| **Key Concepts Used** | `if-elif`, `functions`, `loops`, `input/output`. |

---

## 📌 Project Overview

This is a clean, console-based Python chatbot that interacts with the user in real time. It features:
- **Personalized Interaction:** Prompts the user for their name (`Enter your name: `) and greets them personally.
- **Colorful Terminal Banner:** Highlights the welcome section using ANSI styling (Cyan, Yellow, Magenta, Green).
- **Rule-Based Intent Evaluation:** Uses `if-elif-else` control flow inside `get_response()` function to match user questions.
- **Interactive While Loop:** Runs continuously until the user enters an exit command like `bye` or `quit`.

---

## 💬 Supported Questions & Topics

- **Greetings:** `"hello"`, `"hi"`, `"good morning"`, `"good afternoon"`, `"good evening"`, `"good night"`
- **Status & Well-being:** `"how are you"`, `"i am good"`
- **Identity & Creation:** `"who are you"`, `"what is your name"`, `"who created you"`
- **Python Programming:** `"what is python"`, `"who created python"`, `"what is pip"`, `"what is a variable"`
- **AI & Data Science:** `"what is ai"`, `"what is machine learning"`
- **CodeAlpha Tasks:** `"what is codealpha"`, `"what are the tasks"`, `"what is task 1"`, `"what is task 2"`, `"certificate"`
- **Live Utilities:** `"what time is it"` (real-time clock), `"what is today date"`
- **Entertainment:** `"tell me a joke"` (random programming jokes), `"tell me a fact"` (random computing trivia)
- **Help & Exit:** `"help"` (view sample questions), `"bye"` / `"exit"` (clean termination)

---

## 🚀 How to Run the Script

### Prerequisites
Ensure **Python 3.x** is installed.

### Execution
1. Navigate to the project directory:
   ```bash
   cd CodeAlpha
   ```
2. Run the script:
   ```bash
   python chatbot.py
   ```

---

## 💻 Sample Program Output

```text
========================================================
      Welcome to CodeAlpha Basic Chatbot!       
          Interactive Python Assistant          
========================================================

Enter your name: Dinesh

Welcome, Dinesh!
Chatbot is ready. Type 'bye' to exit, or 'help' to see what you can ask.

Dinesh: hello
Bot: Hi Dinesh! How can I help you today?

Dinesh: who created python
Bot: Python was created by Guido van Rossum and was first released in 1991.

Dinesh: what is ai
Bot: Artificial Intelligence (AI) is the simulation of human intelligence by machines to reason, learn, and problem-solve.

Dinesh: what are the tasks
Bot: CodeAlpha Python Programming Tasks:
  - Task 1: Hangman Game (Console-based word guessing game)
  - Task 2: Stock Portfolio Tracker (Investment value calculation)
  - Task 3: Task Automation (File organizer or email scraper)
  - Task 4: Basic Chatbot (Simple rule-based conversational agent)

Dinesh: what time is it
Bot: The current time is 06:15 PM.

Dinesh: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

Dinesh: tell me a fact
Bot: Did you know? Python was named after 'Monty Python's Flying Circus', not the snake!

Dinesh: help
Bot: Here are some questions you can ask me:
  - Greetings: 'hello', 'how are you', 'good morning'
  - Python: 'what is python', 'who created python', 'what is pip'
  - AI & Tech: 'what is ai', 'what is machine learning'
  - Internship: 'what is codealpha', 'what are the tasks', 'what is task 1'
  - Utilities: 'what time is it', 'what is today date'
  - Fun: 'tell me a joke', 'tell me a fact', 'what is your favorite color'
  - Exit: type 'bye' or 'exit'

Dinesh: bye
Bot: Goodbye, Dinesh! Wishing you all the best!
```

---

## 👤 Author
- **Intern:** Python Programming Intern at CodeAlpha
