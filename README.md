
# Python_Archive
```
A collection of Python programs created throughout my learning journey. 
This repository contains
Practice exercises,
Coding challenges, and
Small projects,
covering Python fundamentals, problem-solving, and core programming concepts. 
It documents my progress as I continue to improve my Python skills.
```



<details>

<summary>🧮 Advanced_Calculator</summary> 

##

A simple command-line calculator built with Python that performs basic arithmetic operations through a menu-driven interface.

## Features

- Addition (multiple numbers)
- Subtraction
- Division
- Floor Division (`//`)
- Multiplication (multiple numbers)
- Exponentiation (Power)
- Modulus (`%`)
- Input validation for menu selection
- Type `"Done"` to finish or cancel an operation

## Technologies Used

- Python 3
- Lists
- Loops
- Conditional statements
- User input handling

## How to Run

```bash
python calculator.py
```

Select an operation from the menu and follow the on-screen instructions to perform calculations.

## Note
This project was created as a beginner Python practice project to improve understanding of loops, conditionals, lists, and arithmetic operators.
</details>




<details>
<summary>🕵 Code_Language_Encode_Decode</summary>

##

A simple Python command-line program that encodes and decodes words using a custom cipher.

## Features

- Encode words with a custom algorithm
- Decode previously encoded words
- Supports single-word input validation
- Uses user-defined random prefixes and suffixes for encoding
- Handles short words separately
- Menu-driven command-line interface

## Encoding Rules

- **3 or more letters:** Move the first letter to the end, then add three random letters to the beginning and end.
- **2 letters:** Reverse the word.
- **1 letter:** No encoding is performed.

## Technologies Used

- Python 3
- String slicing
- Loops
- Conditional statements
- User input validation

## How to Run

```bash
python encoder_decoder.py
```

Follow the on-screen prompts to encode or decode a word.

## Note

This project was built as a beginner Python exercise to practice string manipulation, slicing, loops, and input validation.
</details>





<details>
<summary>👋 Time_Based_Greeting</summary>

##

A simple Python program that displays the current time and greets the user based on the current hour.

## Features
- Displays the current system time in `HH:MM:SS` format.
- Prints a greeting depending on the time of day:
  - Good Morning
  - Good Afternoon
  - Good Evening
  - Good Night

## Modules Used
- `time`

## How It Works
1. Imports the `time` module.
2. Retrieves the current time using `time.strftime()`.
3. Extracts the current hour.
4. Uses conditional statements to determine the appropriate greeting.
5. Prints the current time and greeting.

## Example Output
```
The time is 09:45:12
Good morning
```

## Note
The last condition:

```python
elif 20 <= int(hour) < 00:
```

will **never execute**, because an hour cannot be both greater than or equal to `20` and less than `0`. A better condition is:

```python
elif 20 <= int(hour) <= 23:
    print("Good night")
```

or simply use:

```python
else:
    print("Good night")
```
</details>




<details>
<summary>🪪 Age_Eligibility_Checker</summary>

##

A simple Python program that checks whether a user is old enough to drive and drink based on their age.

## Features
- Accepts the user's age as input.
- Displays the entered age.
- Determines driving eligibility.
- Determines drinking eligibility.

## Concepts Used
- User input with `input()`
- Type conversion using `int()`
- Formatted strings (f-strings)
- Conditional statements (`if`, `elif`, `else`)
- Comparison operators (`>=`, `<`)

## How It Works
1. Prompts the user to enter their age.
2. Converts the input to an integer.
3. Prints the entered age.
4. Checks if the user is at least 18 years old to determine driving eligibility.
5. Checks if the user is at least 21 years old to determine drinking eligibility.

## Example Output

### Input
```
Enter your age: 22
```

### Output
```
Your age is: 22
You can drive!
you can drink, but dont
```

## Note
The driving and drinking checks are independent. Even after checking whether the user can drive, the program performs a separate check for drinking eligibility.
</details>




<details>
<summary>🏛 Library_Management_System</summary>

##

A simple Python console application that allows users to manage a small library by adding books, viewing all books, and checking the total number of books.

## Features
- Add new books to the library.
- View all books currently stored.
- Display the total number of books.
- Runs continuously until manually stopped.

## Concepts Used
- Classes and class variables
- Lists
- `while` loops
- Conditional statements (`if`)
- User input (`input()`)
- List methods (`append()`)
- Exception handling with `ValueError`
- `for` loops
- f-strings

## How It Works
1. Creates a `Library` class to store:
   - Total number of books.
   - A list of book names.
2. Displays a menu with three options:
   - **1** → Show the total number of books.
   - **2** → Display all books in the library.
   - **3** → Add a new book.
3. Updates the library whenever a new book is added.
4. Continues running until the user manually exits the program (e.g., `Ctrl + C`).

## Example

```
What do you want to do?
1. Total books.
2. All books.
3. Add a book.

Choice: 3
Enter the name of book to add: The Hobbit
Book "The Hobbit" added successfully.

Choice: 2
Books in library:
The Hobbit

Choice: 1
The total amount of books in the library is 1.
```

## Future Improvements
- Add an **Exit** option.
- Prevent duplicate book entries.
- Remove books from the library.
- Search for books by title.
- Save the library to a file so books persist after closing the program.
- Use class methods and create `Library` objects instead of relying only on class variables.

</details>




<details>
<summary>🪨 Rock_Paper_Scissors</summary>

##

A simple Python-based Rock Paper Scissors game where the user competes against the computer. The computer randomly selects an option, and the program determines the winner.

## Features
- User can choose:
  - Rock
  - Paper
  - Scissors
- Computer makes a random choice.
- Automatically compares both choices.
- Displays the winner.
- Runs continuously until an invalid input is entered.

## Modules Used
- `random`

## Concepts Used
- Importing modules
- Lists
- Infinite `while` loops
- User input handling
- Random selection using `random.choice()`
- Conditional statements (`if`, `elif`)
- String comparison
- Basic game logic

## How It Works
1. The user selects Rock, Paper, or Scissors.
2. The computer randomly chooses one option.
3. The program compares both choices:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
4. The result is displayed as:
   - User Wins
   - Computer Wins
   - Draw

## Example Output

```
Choose:
1. Rock
2. Paper
3. Scissors

Enter your choice: 1

Computer chose PAPER
User chose ROCK
Computer Wins!!!
```

## Future Improvements
- Add a score counter for multiple rounds.
- Add an option to exit instead of stopping with an error.
- Reduce repeated code using dictionaries/functions.
- Add a GUI using Tkinter or PySide6.
- Add animations and sound effects.

</details>




<details>
<summary>🔢 Simple_Calculator</summary>

##

A simple Python calculator program that performs basic arithmetic operations on two numbers entered by the user.

## Features
- Takes two numbers as input.
- Performs multiple mathematical operations:
  - Addition
  - Subtraction
  - Division
  - Floor Division
  - Multiplication
  - Power
  - Modulus (remainder)

## Concepts Used
- User input using `input()`
- Type conversion using `int()`
- Arithmetic operators:
  - `+` Addition
  - `-` Subtraction
  - `/` Division
  - `//` Floor Division
  - `*` Multiplication
  - `**` Exponentiation
  - `%` Modulus
- Printing formatted results

## How It Works
1. The user enters two numbers.
2. The program applies different arithmetic operators.
3. The results of each operation are displayed.

## Example Output

```
Please enter the first number: 10
Please enter the first number: 3

Addition of 10 and 3 is: 13
Subtraction of 10 and 3 is: 7
Division of 10 and 3 is: 3.3333333333333335
Float Division of 10 and 3 is: 3
Multiplication of 10 and 3 is: 30
The result of 10 raised to the power 3 is: 1000
Remainder when 10 is divided by 3 is: 1
```

## Future Improvements
- Add a menu-based system to select operations.
- Add support for decimal numbers using `float()`.
- Handle division by zero errors.
- Use functions to make the code cleaner and reusable.
- Add a graphical user interface (GUI).
</details>




<details>
<summary>📝 Who_Wants_to_be_a_Millionare demo.py</summary>

##

A simple Python quiz game inspired by a "Who Wants to Be a Millionaire" style format. The player answers multiple-choice questions and earns prize money for every correct answer.

## Features
- Multiple-choice quiz questions.
- Checks user answers.
- Awards ₹500 for every correct answer.
- Shows current winnings.
- Stops the game when an incorrect answer is given.

## Concepts Used
- Lists
- Conditional statements (`if`, `else`)
- `for` loops
- User input handling
- Integer conversion using `int()`
- List methods:
  - `append()`
  - `pop()`
- `sum()` function

## How It Works
1. The game displays a question with four options.
2. The user selects an answer by entering the option number.
3. If the answer is correct:
   - The player earns ₹500.
   - The next question appears.
4. If the answer is incorrect:
   - The game ends.
   - The final prize amount is displayed.

## Example Output

```
Question 1. What is the capital of France?

1. Madrid
2. Berlin
3. Paris
4. Rome

Enter your answer: 3

correct!! You won Rs. 500


Question 2. Which planet is known as the Red Planet?

1. Venus
2. Jupiter
3. Saturn
4. Mars

Enter your answer: 4

correct!! You won Rs. 1000
```

## Future Improvements
- Store questions and answers in dictionaries instead of separate lists.
- Use loops to avoid repeating code for every question.
- Add more questions and different prize levels.
- Add a timer for each question.
- Add lifelines like:
  - 50-50
  - Audience poll
  - Skip question
- Create a GUI version using Tkinter or PySide6.

</details>
