project2.py located in this same folder is the driver for this program
	(a copy can also be found in ./code).

It was written under Xubuntu 19.04 and interpreted using Python 3.7.3

In *nix systems with Python 3 installed, it can be executed
	from this directory via either console command:

			python3 project2.py [input path] [output path] [hash function name] [mod] [bucket_size] [collision strat] [c]

			python3 project2.py input=[path] output=[path] hash_func=[func name] mod=[mod] bucket_size=[size] collision=[strategy] c=[[#,#]]

The second of these (non-positional) is better in general, as we don't have to fill in extra info not needed by the collision strategy.
For the student hash method, I highly recommend using the named parameter method.


For Windows, I'd highly recommend opening the project file from IDLE and
	using the "Run Customized" command (Shift + F5) to enter the parameters.

NOTE: It does expect the output directory to exist. 
	I didn't want to go poking around in the file system for this project.

-----------------------------------------------------------------------------

Additionally, I've included three bash scripts (run_all.sh, run_required.sh, and run_test.sh) to
	run all the inputs, all the required inputs, and all the test inputs.

-----------------------------------------------------------------------------

The ./inputs contains inputs for the project.

# Required inputs
	class_input.txt
	student_input.txt
	

# Test inputs
	bad_input.txt
	repeated_input.txt


-----------------------------------------------------------------------------

The outputs for the inputs are in ./outputs. All inputs will output a table to the best of hashing's ability.

# Test ouputs
bad_output.out should only have '12345' entered into the table.
repeated_output_linear.out should have '11' repeated 10 times, which allows us to check the linear probing.
repeated_output_quad.out should have '11' repeated 10 times, which allows us to check the quadratic probing.
repeated_output_quad.out should have '11' repeated 10 times, which allows us to check the chaining function.

# Required outputs
output[#].out corresponds to the schema from the project handout with the class/student hash function
student_output[#].out corresponds to the schema from the project handout with the class/student hash function with student_input.txt

# Extra outputs
output[#]_c1.out refers to the class input with the quadratic probing strategy with the c values changed to [0,1]
output[#]_c1 refers to the class input with the quadratic probing strategy with the c values changed to [1,0]


	