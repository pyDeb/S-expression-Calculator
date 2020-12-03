# S-expression-Calculator
It is a command-line program that acts as a simple calculator: it takes a single argument as an expression and prints out the integer result of evaluating it.

**Sample input and output:**
```
$ ./calc.py 123
123

$ ./calc.py "(add 12 12)"
24
```
**A function call takes the following form:**

(FUNCTION EXPR EXPR)

A function call is always delimited by parenthesis ( and ).

The FUNCTION is one of add or multiply.

The EXPR can be any arbitrary expression, i.e. it can be further function calls or integer expressions.

Exactly one space is used to separate each term.

For example:
```
(add 123 456)

(multiply (add 1 2) 3)
```

**The add function:**
```
(add 1 1)
2

(add 0 (add 3 4))
7

(add 3 (add (add 3 3) 3))
12
```
**The multiply function:**
```
(multiply 1 1)
1

(multiply 0 (multiply 3 4))
0

(multiply 2 (multiply 3 4))
24

(multiply 3 (multiply (multiply 3 3) 3))
81
```

**Combination of add and multiply:**
```
(add 1 (multiply 2 3))
7

(multiply 2 (add (multiply 2 3) 8))
28
```

