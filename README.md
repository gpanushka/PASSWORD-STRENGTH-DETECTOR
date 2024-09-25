I built a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters and provides feedback to users on the password's strength.

I have used resources like Visual Studio Code as the text editor and used internet resources for debugging. This task is executed using the following steps:

<h3>Importing Libraries:</h3>
We used the re module for this task. The _re_ module in Python is used for working with regular expressions. It offers a set of functions that allows you to search, edit, and manipulate text strings based on patterns. For example, you can use _re.search()_ to find a pattern within a string, _re.match()_ to check if a string matches a pattern from the beginning, and _re.findall()_ to find all occurrences of a pattern in a string.


![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/33354571-32fe-4068-81a6-2eedccdc55fe)


<h3>Functions to check Password:</h3>

<h4>1. Criteria</h4>

**Length Check**: Sets length to True if the password length is greater than 8, otherwise False.

**Uppercase Check**: Uses a regular expression to check if the password contains at least one uppercase letter. re.search returns None if no match is found, and bool converts the result to True or False.

**Lowercase Check**: Uses a regular expression to check for at least one lowercase letter.

**Digit Check**: Uses a regular expression to check for at least one digit.

**Special Character Check**: Uses a regular expression to check for at least one special character (anything that's not a letter or digit).


![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/00dbdef9-c45c-481d-a988-1184b631dc1a)


<h4>2. Calculate score</h4>
Calculates the score by summing the boolean values of the checks. Each True contributes 1, leading to a possible score range from 0 to 5.
Evaluates the password strength based on the score:
Strong: If all criteria are met (score == 5).
Moderate: If most criteria are met (score >= 3).
Weak: If few or none of the criteria are met (score < 3).


![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/55b10d9a-5588-44e0-adba-9c9ec5e1afd5)

<h4>3. Feedback</h4>


![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/430b3f8e-539d-416b-8de4-b2e673e37bcf)





Initializes an empty list feedback to store feedback messages.
Appends specific feedback messages to the feedback list if any criteria are not met.
Prints the feedback list containing messages about what is missing from the password.

<h3>Taking input from user:</h3>
Takes input from user and runs the above function.

![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/548f5fd9-7d07-49c4-8690-52c1e62aaf8b)



<h3>Output:</h3>
Here's how outputs for different inputs would look like:


![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/7ffe900f-eb6c-4769-b9d4-ff4752d49528)

![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/26c3400f-207e-4dff-93c3-ee393b0d45b6)

![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/fcfe2712-14ae-40b7-abbf-7b21b1218b44)

![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/aae6b1f3-5ccd-431c-9e01-c22dc9f88468)




