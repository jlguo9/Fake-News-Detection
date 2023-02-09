## (subtitle)
Nowadays there are so many tools that can help us with data preparation, such as Python, Perl, R,
and some even with Graphic User Interface like Microsoft Excel, Jupyter Notebook, Tableau Prep, etc. 
You may have already mastered some of those modern technologies, so that you might ask: “Why should I learn some old-fashioned command line languages, given that learning something new can be such a painful process?”

<img src="img/learn_new_things.jpg" width=300>

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

The awk code here costs less effort to write and is more human-readible than the Python implementation. This is a simplest case and for more complex tasks the difference can be even larger.

### 3.	They Run Fast
<img src="img/fast.jpg" width=300>

Sed and awk are not as extensible as modern languages like Python and Perl, and thus can be used for a narrower range of purposes than the latter; however, it is because of such a concentration that they can avoid any features irrelevant to text processing, keep lightweight, and get an well-optimized interpreter, so that for tasks within their capability they are normally faster than high-level programming languages, not to mention other GUI software.

Another reason why they're fast is that sed uses a simple model of regular expression and awk compiles regular expression into state machine. The former makes it extremely fast for sed to process simple text processing tasks, while the latter helps awk with quickly determining if a line of text matches a complex pattern even for large amounts of text data. 

### 4.	They Are Mouse-Free
This one depends on personal habits. Some programmers like GUI and mouses because they make our life easier, while some other prefer using keyboard only because mouse sometimes interrupt their flow of thoughts and short cuts is usually faster than mouse clicking.

If you are a keyboard lover, then sed and awk is perfect for you: it’s purely text- and keyboard-based with no need to move or click a mouse.
