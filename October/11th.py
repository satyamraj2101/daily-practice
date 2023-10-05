# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
import builtins

functions = ["print", "len", "input"]

for function in functions:
  print(builtins.__dict__[function].__doc__)