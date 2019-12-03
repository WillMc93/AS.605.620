project3.py located in this same folder is the driver for this program
	(a copy can also be found in ./code).

It was written under Xubuntu 19.10 and interpreted using Python 3.7.3

In *nix systems with Python 3 installed, it can be executed from this directory via the console command:

	python3 project3.py [input path] [output path]


For Windows, I'd highly recommend opening the project file from IDLE and
	using the "Run Customized" command (Shift + F5) to enter the parameters.

NOTE: It does expect the output directory to exist. 
	I didn't want to go poking around in the file system for this project.

-----------------------------------------------------------------------------

Additionally, I've included two bash scripts (run_all.sh and run_required.sh) to
	run all the inputs and all the required inputs.

-----------------------------------------------------------------------------

The ./inputs contains inputs for the project.

# Required inputs
class_input.txt - The input provided by the class prompt.
student_input.txt - The input I made		

# Verification inputs (links to websites in input files)
tushar.txt - Taken from the youtube video linked on the discussion board.
book.txt - Taken from 15.4 CLRS.
uci_edu.txt - Input taken from uci.edu
columbia.txt - Input taken from columbia.edu. They provide the wrong answer.

# Error inputs
error_check.txt - Checks that code successfully ignores input errors.
empty.txt - Checks that code successfully runs with no input data.

-----------------------------------------------------------------------------

The outputs for the inputs are in ./outputs. All inputs (including an empty file) will output something.
Names here just mirror the input name with .out instead of .txt

	