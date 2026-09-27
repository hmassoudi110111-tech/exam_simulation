# 📝 Python Excel Quiz

A simple and interactive **Quiz Application** developed with **Python**.

The application randomly selects a number of questions from an **Excel file** and presents them to the user. For each question, the user must enter the **number of the correct answer** instead of selecting an option using radio buttons.

After answering all questions, the application automatically checks the submitted answers, calculates the user's score, and displays the final result.

---

## ✨ Features

* 📊 Load quiz questions from an Excel file
* 🎲 Randomly select questions from the question bank
* 📝 Display questions and multiple-choice answers
* 🔢 Enter the answer by typing the option number
* ✅ Automatically check submitted answers
* 🧮 Calculate the final score
* 🏆 Display the user's final result
* 🚫 Validate incorrect or invalid inputs
* 📚 Easily update questions by editing the Excel file

---

## 🛠️ Technologies Used

* **Python 3**
* **Pandas** – Reading and processing Excel data
* **OpenPyXL** – Working with Excel files
* **Random** – Random question selection
* **Tkinter** – Graphical User Interface (if used in the project)

---

## 📂 Project Structure

```text
Python-Excel-Quiz/
│
├── main_code.py
├── questions.xlsx
├── README.md
└── images/
    └── quiz.png
```

> You can change the file names above according to the actual structure of your project.

---

## 📊 Excel Question Bank

The questions and their answers are stored in an Excel file.

A typical structure can be:

| Question        | Option 1          | Option 2               | Option 3 | Option 4  | Correct Answer |
| --------------- | ----------------- | ---------------------- | -------- | --------- | -------------- |
| What is Python? | A Database        | A Programming Language | An OS    | A Browser | 2              |
| What is HTML?   | A Markup Language | A Database             | An IDE   | An OS     | 1              |

The **Correct Answer** column contains the number of the correct option.

The Excel file can easily be modified to add, remove, or update questions.

---

## 🎲 Random Question Selection

The application uses Python's randomization functionality to select questions from the Excel question bank.

This means that the user may receive a different set of questions each time the quiz is started.

For example, if the Excel file contains 50 questions and the quiz is configured to use 10 questions, the application randomly selects 10 questions from the available question bank.

---

## 🔢 Answering Questions

Instead of using radio buttons or checkboxes, the application asks the user to enter the **number of the selected answer**.

For example:

```text
1. Python
2. Java
3. C++
4. HTML

Enter your answer: 1
```

The entered number is then compared with the correct answer stored in the Excel file.

---

## 🧮 Score Calculation

After all questions have been answered, the application compares the user's answers with the correct answers.

The final score is calculated based on the number of correct answers.

For example:

```text
Total Questions: 10
Correct Answers: 8
Incorrect Answers: 2

Final Score: 80%
```

---

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installed version:

```bash
python --version
```

### 2. Install Required Libraries

Install the required packages using:

```bash
pip install pandas openpyxl
```

If the project uses Tkinter, it is normally included with Python.

### 3. Run the Application

Navigate to the project directory and run:

```bash
python quiz.py
```

---

## 🎯 Project Goals

This project was created to practice and demonstrate several Python programming concepts:

* Reading data from Excel files
* Processing structured data
* Random selection
* Working with lists and data structures
* User input validation
* Conditional statements
* Loops
* Score calculation
* Building a simple quiz system

---

## 🔮 Future Improvements

Possible future improvements include:

* ⏱️ Adding a time limit for the quiz
* 🏆 Creating a high-score system
* 👤 Adding user profiles
* 📈 Saving quiz results
* 📊 Generating performance reports
* 🎯 Adding different difficulty levels
* 📚 Supporting multiple question categories
* 🔀 Randomizing answer choices
* 🌐 Creating a web-based version
* 🗄️ Migrating from Excel to a database such as SQLite or MySQL

---

## 📸 Screenshot

You can add a screenshot of the application to the `images` folder and display it in the README:

```markdown
![Python Quiz](images/quiz.png)
```

---

## 📚 Educational Purpose

This project was developed as an **educational Python project** to demonstrate how Python can be used to create a simple quiz application using an Excel-based question bank.

It is particularly useful for practicing **file handling, data processing, randomization, user input, and basic application logic**.

---

## 👩‍💻 Author

**Dr. Hadis Massoudi**

University Lecturer | Python Developer

---

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.

Feel free to fork the project and add your own features and improvements.

---

## 📄 License

This project is created for **educational and learning purposes**.
