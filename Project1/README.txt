project1.py located in the root of the folder is the driver for this program
	(a copy can also be found in ./code).  
It was written under Xubuntu 19.04 and interpreted using Python 3.7.3

In *nix systems with Python 3 installed, it can be executed
	from this directory via the console command:

			python3 project1.py [path to input] [path to output]


For Windows, I'd highly recommend opening the project file from IDLE and
	using the Run Customized command (Shift + F5) to enter the paths.

NOTE: It does expect the output directory to exist. 
	I didn't want to go poking around in the file system for this project.

-----------------------------------------------------------------------------

Additionally, I've included two bash scripts (run_all.sh and run_valid.sh) to
	run all the inputs and all the valid (read: not purposely misformatted) inputs.

-----------------------------------------------------------------------------

The ./inputs contains inputs for the project (no duh, right?).

The following are VALID inputs:
	classinput.dat - provided by class
	myinput.dat - self-made for verification of code. Outputs cubes

The follwing are TEST inputs:
	lettersize.dat - non-numeric where size should be
	lettermat.dat - non-numeric in matrix
	toosmall.dat - size is too small
	toobig.dat - size is too big
	badmat.dat - just stupid

-----------------------------------------------------------------------------

The outputs for the inputs are in ./outputs. Valid inputs produce good results, and 
	test inputs will give a nice message and the exception that was generated from
	the improperly formatted data.
