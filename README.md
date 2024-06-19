This is my second task as a Cyber Security Intern at Prodigy InfoTech where I built a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters and provides feedback to users on the password's strength.

I have used resources like Visual Studio Code as the text editor and used internet resources for debugging. This task is executed using the following steps:

<h4>Importing Libraries:</h4>
We used the re module for this task. The _re_ module in Python is used for working with regular expressions. It offers a set of functions that allows you to search, edit, and manipulate text strings based on patterns. For example, you can use _re.search()_ to find a pattern within a string, _re.match()_ to check if a string matches a pattern from the beginning, and _re.findall()_ to find all occurrences of a pattern in a string 
![image](https://github.com/gpanushka/PRODIGY_CS_03/assets/167328539/dfbac48c-1a81-49dd-af40-30ec92f748d8)
<h4>Functions to check Password:</h4>
<h5>1. Criteria</h5>
**Length Check**: Sets length to True if the password length is greater than 8, otherwise False.
**Uppercase Check**: Uses a regular expression to check if the password contains at least one uppercase letter. re.search returns None if no match is found, and bool converts the result to True or False.
**Lowercase Check**: Uses a regular expression to check for at least one lowercase letter.
**Digit Check**: Uses a regular expression to check for at least one digit.
**Special Character Check**: Uses a regular expression to check for at least one special character (anything that's not a letter or digit).
<h5>2. Calculate score</h5>
Calculates the score by summing the boolean values of the checks. Each True contributes 1, leading to a possible score range from 0 to 5.
Evaluates the password strength based on the score:
Strong: If all criteria are met (score == 5).
Moderate: If most criteria are met (score >= 3).
Weak: If few or none of the criteria are met (score < 3).
