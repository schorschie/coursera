# Getting Started with your Lab Sandbox
VSCode Sandbox comes with Java, CPP, C,C#, Python, Node JS, Scala, Ruby, PHP and Go preinstalled. All basic packages including the I/O package, data structures, Math package etc., are available for all the languages.

## What extensions are already installed in this environment?
There are many extensions that come preinstalled which include compiler, runner, debugger, unit tester, browser preview etc., You can click on the extensions icon on the left panel of VSCode to see what extensions come with the sandbox instance. The starter code has been provided as a part of the course for C++, Java and Python. You may also choose to use any other language for the assignments. However you have to code from the scratch in such a case. 

## How can I compile the Code in my Terminal?
Open the terminal and navigate to the directory containing your file. 
```sh
cd /home/coder/project/<directory>
```
- Use `javac <filename>` to compile the java code. For example, if your code is HelloWorld.java, run the following command to compile.

```sh
javac HelloWorld.java
```
This will produce an output HelloWorld.class which is executable with JRE. To run the class, run the following command.

```sh
java HelloWorld
```

- Use `g++ <filename>` to compile the c++ code. For example, if your code is HelloWorld.cpp, run the following command to compile.

```sh
g++ HelloWorld.cpp -o HelloWorld
```
This will produce an output HelloWorld

```sh
./HelloWorld
```
- Use `python <filename>` to run the python code. For example, if your code is HelloWorld.py, run the following command.

```sh
python HelloWorld.py
```
As python is only compiled at runtime, any error in code will be thrown while running.

**To compile and run this file :**
1) Click on the ▶️ in the top right of the IDE to compile and run the code. You cannot use this option to run the programs which require user input. 

## Assignment Code
- You can use any of the languages that are mentioned above to complete the assignments. The [starter code](https://www.coursera.org/learn/algorithmic-toolbox/resources/3r3Mv) has been provided for all the weeks mainly in C++, Java, Python but for some of the assignments also in scala, Haskell script, kotlin, Node.js, csharp and ruby. You can also use the lab sandbox to try out solutions before you answer the quiz. 

- The course team mentions PyCharm as a potential IDE that you can use in this course for Python programming. If you're unable to install software locally or on your network,  or if you'd like to use other programming languages fully in-browser, you can use this Visual Studio Code Lab Sandbox as an alternative IDE to complete your coursework."

- In Week 2 there is an existing Lab called [Big-O Notation Plots](https://www.coursera.org/learn/algorithmic-toolbox/ungradedLab/Qmv41/big-o-notation-plots). We highly recommend that you use the existing Lab item the course team has created instead of using this Lab Sandbox to complete this activity. The Lab Sandbox will be most helpful for other follow along, practice, and assessment course work. 

## How can I Debug the code?
You can set break points by clicking to the left of line number where you want to break and investigate.
You can use the debugger in VSCode IDE using the icon on the left panel.