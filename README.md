### README for Random Statistics with Command-Line Arguments Exercise

---

# 🎲 Random Statistics with Command-Line Arguments in Python

Welcome, students! 🚀 This exercise is crafted to enhance your proficiency in using Python libraries, generating random numbers, performing statistical computations, and manipulating command-line arguments.

## 🎯 Objectives

- Utilize standard Python libraries to achieve complex tasks.
- Generate random data sets and compute their statistical properties.
- Learn to handle command-line arguments for dynamic script execution.
- Practice writing Python code with proper exception handling.
- Validate your code with unit tests.

## 🔍 Overview

You will be working with `exercise.py`, which includes function stubs that you'll need to implement. These functions revolve around generating random numbers, computing statistics, and slicing data based on command-line arguments.

Additionally, `exercise.py` should be able to be run from the command line, taking arguments for the range of data to be processed.

## ✅ Tasks

### 1️⃣ Familiarize Yourself with the Codebase

In `exercise.py`:
- Read the provided stubs and the docstrings carefully to understand what you need to code.
- Test the script with:

```bash
python random_stats.py 10 20
```

Initialially, nothing will show up on the terminal. As you implement each function, 
uncomment the next line and you should see

You should see output indicative of a random data set's statistics based on the provided range.

Run the unit tests with:

```bash
pytest
```


You'll need to pass these tests by implementing the stubs correctly.

### 2️⃣ Implement the Functions

For each stub in `random_stats.py`:
- Fill in your code where the `TODO` comments are placed.
- Use command-line arguments to test the script's functionality by running:

```bash
python random_stats.py [start_index] [end_index]
```


- Confirm the correct operation by running `pytest` and ensuring all tests pass.

### 3️⃣ Utilize VSCode Codespaces for Development

After you have implemented the functions and passed the tests:

1. **Stage Changes**: 
   - Observe your changes in the Source Control panel.
   - Click the `+` symbol to stage files you modified.

2. **Commit Changes**: 
   - Write a meaningful commit message.
   - Use `Ctrl + Enter` (or `Cmd + Enter` on Mac) to commit the staged files.

3. **Push Changes**: 
   - Press the `...` in Source Control.
   - Choose **Push** to upload your changes to the remote repository.

4. **Check the Automated Tests**: 
   - Ensure the automated tests pass after pushing your changes.

## 📘 Resources

- **Python `random` Library**: Refresh your memory on generating random numbers using Python's [random library documentation](https://docs.python.org/3/library/random.html).
- **Python `statistics` Library**: Check out how to compute statistical metrics with Python's [statistics library documentation](https://docs.python.org/3/library/statistics.html).
- **Command-Line Arguments in Python**: Learn more about handling command-line arguments in Python with this [tutorial on `sys.argv`](https://docs.python.org/3/using/cmdline.html#cmdoption-arg).

## 🤔 Need Help?

- **Clarifications**: If you need any clarifications, don't hesitate to reach out on Discord.
- **Debugging**: In case you face any bugs, remember that debugging is a crucial part of coding. Seek help if you're stuck.
- **Solutions**: A file named `solution.py` is available. Refer to it only if you've spent a significant amount of time (30+ minutes) on a problem without progress.

Should you encounter unexpected behaviors:
- Implement breakpoints in your code within VSCode.
- Utilize the VSCode debugger to examine your code, check variable states, and understand issues.
- Update your code as necessary based on your findings.
- Watch the [Debugger Tutorial](https://www.youtube.com/watch?v=7qZBwhSlfOo&t=7s) if you are unfamiliar with debugging in VSCode.

