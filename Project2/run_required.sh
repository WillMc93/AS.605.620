#! /usr/bin/bash

python3 main.py ./input.txt ./outputs/output1.out class 120 1 linear
python3 main.py ./input.txt ./outputs/output2.out class 120 1 quadratic [0,1]
python3 main.py ./input.txt ./outputs/output3.out class 120 1 chaining
python3 main.py ./input.txt ./outputs/output4.out class 113 1 linear
python3 main.py ./input.txt ./outputs/output5.out class 113 1 quadratic [0,1]
python3 main.py ./input.txt ./outputs/output6.out class 113 1 chaining
python3 main.py ./input.txt ./outputs/output7.out class 120 3 linear
python3 main.py ./input.txt ./outputs/output8.out class 120 3 quadratic [0,1]