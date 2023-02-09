## (subtitle)
Nowadays there are so many tools that can help us with data preparation, such as Python, Perl, R,
and some even with Graphic User Interface like Microsoft Excel, Jupyter Notebook, Tableau Prep, etc. 
You may have already mastered some of those modern technologies, so that you might ask: “Why should I learn some old-fashioned command line languages, given that learning something new can be such a painful process?”

[image: learn new things from lovethispic.com]

Well, it's true that sed and awk are old -- they're already in their 40s -- but that doesn't mean they're outdated. In some ways they still perform better than other tools:

### 1.	They Are Pre-Installed in Unix and Unix-Like Systems
Have you ever been in a situation where your lab has just bought a new workstation, or your company's IT support team has just updated the workstation and reinstalled system, or you are simply using someone else’s device, and you need to process a batch of data before the environment and software being configured? It can be a dilemma when your task is urgent or you don’t want to waste time configuring or waiting for the IT Technician to configure the environment. But don’t worry, all the command line tools mentioned above are typically pre-installed on Unix-based systems, and you don’t need to install any extra packages like what you do for Python.

### 2.	They Are One-Liner-Friendly
The syntax of sed and awk is designed to be concise, allowing people to accomplish a lot of actions with relatively few lines of code, or even possibly only one line of code if the programmer is familiar with their features. For the same task, sed/awk code is usually shorter than high-level programming language code. Here is an example of using awk to extract the first column of the input csv file and write it into the output file:

    $ awk -F, '{print $1}' input > output

And its equivalent Python implementation:

~~~python
with open(“input_path”, “r”) as f_input, open(“output_path”, “w”) as f_output:
    for line in f_input:
        f_output.write(line.split(“,”)[0] + “\n”)
~~~