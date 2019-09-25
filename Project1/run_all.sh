# Invalid Data Tests
#   letters (I assume it holds for all non-numerics)
python3 project1.py ./inputs/lettersize.dat ./outputs/lettersize.out
python3 project1.py ./inputs/lettermat.dat ./outputs/lettermat.out

#   size doesn't match
python3 project1.py ./inputs/toosmall.dat ./outputs/toosmall.out
python3 project1.py ./inputs/toobig.dat ./outputs/toobig.out
python3 project1.py ./inputs/wrongsize.dat ./outputs/wrongsize.out

#   just generally wrong
python3 project1.py ./inputs/badmat.dat ./outputs/badmat.out


# Valid Data
#   Class Input
python3 project1.py ./inputs/classinput.dat ./outputs/classoutput.out

#   My Input
python3 project1.py ./inputs/myinput.dat ./outputs/myoutput.out
