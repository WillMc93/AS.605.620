# Run test files
# 	file that contains letters and symbols (should get ignored w/ 12345 on table)
python3 project2.py ./inputs/bad_input.txt ./outputs/bad_output.out

# 	file that contains the same number multiple times
# 	do it for all probe types so we see the different methods work
python3 project2.py ./inputs/repeated_input.txt ./outputs/repeated_output_quad.out
python3 project2.py ./inputs/repeated_input.txt ./outputs/repeated_output_linear.out class 120 1 linear
python3 project2.py ./inputs/repeated_input.txt ./outputs/repeated_output_chain.out class 120  1 chaining


#	run a couple tests with too big a mod value
python3 project2.py input=./inputs/class_input.txt output=./outputs/toobig1.out mod=220
python3 project2.py input=./inputs/class_input.txt output=./outputs/toobig2.out mod=220 collision=linear



# Run all required with class input
python3 project2.py ./inputs/class_input.txt ./outputs/output1.out class 120 1 linear
python3 project2.py ./inputs/class_input.txt ./outputs/output2.out class 120 1 quadratic [0.5,0.5]
python3 project2.py ./inputs/class_input.txt ./outputs/output3.out class 120 1 chaining
python3 project2.py ./inputs/class_input.txt ./outputs/output4.out class 113 1 linear
python3 project2.py ./inputs/class_input.txt ./outputs/output5.out class 113 1 quadratic [0.5,0.5]
python3 project2.py ./inputs/class_input.txt ./outputs/output6.out class 113 1 chaining
python3 project2.py ./inputs/class_input.txt ./outputs/output7.out class 41 3 linear
python3 project2.py ./inputs/class_input.txt ./outputs/output8.out class 41 3 quadratic [0.5,0.5]
python3 project2.py input=./inputs/class_input.txt output=./outputs/output9.out hash_func=student bucket_size=1 collision=linear
python3 project2.py input=./inputs/class_input.txt output=./outputs/output10.out hash_func=student bucket_size=1 collision=quadratic c=[0.5,0.5]
python3 project2.py input=./inputs/class_input.txt output=./outputs/output11.out hash_func=student bucket_size=1 collision=chaining

# Run all required with my input
python3 project2.py ./inputs/student_input.txt ./outputs/student_output1.out class 120 1 linear
python3 project2.py ./inputs/student_input.txt ./outputs/student_output2.out class 120 1 quadratic [0.5,0.5]
python3 project2.py ./inputs/student_input.txt ./outputs/student_output3.out class 120 1 chaining
python3 project2.py ./inputs/student_input.txt ./outputs/student_output4.out class 113 1 linear
python3 project2.py ./inputs/student_input.txt ./outputs/student_output5.out class 113 1 quadratic [0.5,0.5]
python3 project2.py ./inputs/student_input.txt ./outputs/student_output6.out class 113 1 chaining
python3 project2.py ./inputs/student_input.txt ./outputs/student_output7.out class 41 3 linear
python3 project2.py ./inputs/student_input.txt ./outputs/student_output8.out class 41 3 quadratic [0.5,0.5]
python3 project2.py input=./inputs/student_input.txt output=./outputs/student_output9.out hash_func=student bucket_size=1 collision=linear
python3 project2.py input=./inputs/student_input.txt output=./outputs/student_output10.out hash_func=student bucket_size=1 collision=quadratic c=[0.5,0.5]
python3 project2.py input=./inputs/student_input.txt output=./outputs/student_output11.out hash_func=student bucket_size=1 collision=chaining



# Vary c values for quad with class input for schema 2,5,8,10
python3 project2.py ./inputs/class_input.txt ./outputs/output2_c1.out class 120 1 quadratic [0,1]
python3 project2.py ./inputs/class_input.txt ./outputs/output2_c2.out class 120 1 quadratic [1,0]
python3 project2.py ./inputs/class_input.txt ./outputs/output5_c1.out class 113 1 quadratic [0,1]
python3 project2.py ./inputs/class_input.txt ./outputs/output5_c2.out class 113 1 quadratic [1,0]
python3 project2.py ./inputs/class_input.txt ./outputs/output8_c1.out class 41 3 quadratic [0,1]
python3 project2.py ./inputs/class_input.txt ./outputs/output8_c2.out class 41 3 quadratic [1,0]
python3 project2.py input=./inputs/class_input.txt output=./outputs/output10_c1.out hash_func=student bucket_size=1 collision=quadratic c=[0,1]
python3 project2.py input=./inputs/class_input.txt output=./outputs/output10_c2.out hash_func=student bucket_size=1 collision=quadratic c=[1,0]