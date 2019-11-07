# Run test files
# 	file that contains letters and symbols (should get ignored w/ 12345 on table)
python3 project2.py ./inputs/bad_input.txt ./outputs/bad_output.out

# 	file that contains the same number multiple times
# 	do it for all probe types so we see the different methods work
python3 project2.py ./inputs/repeated_input.txt ./outputs/repeated_output_quad.out
python3 project2.py ./inputs/repeated_input.txt ./outputs/repeated_output_linear.out class 120 1 linear
python3 project2.py ./inputs/repeated_input.txt ./outputs/repeated_output_chain.out class 120  1 chaining


# run a couple tests with too big a mod value
python3 project2.py input=./inputs/class_input.txt output=./outputs/toobig1.out mod=220
python3 project2.py input=./inputs/class_input.txt output=./outputs/toobig2.out mod=220 collision=linear
