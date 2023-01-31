# Boolean-Interpreter-in-Python
A description of how a boolean interpreter functions.
For the problem above i created two distinct intepreters. One which uses the common parentheses and the other that uses the operators and, or and not.

# Analysing example 1; 

The interpreter is tasked in predicting whether A which is 5 is less than 10 and what type of value the print is integer or boolean. The answer is True, A is less than 10 and the expression is a boolean. Boolean expressions contain either a true or false statement so our answer is definitive.

The next example the interpreter is given is to find out whether B, which states that A is greater than 10 is True or False. Upon printing the result is False as A which is 5 cannot be greater than 10. The interpreter also confirms once again that its type is a boolean expression.


# Analysing example 2;
In example 2 i used the operators 'and', 'or' and 'not' to determine whether the expressions generated where either true or false. In this example i used ChatGPT to create the 3 expressions while i personally coded the parameters X and y. Here is what they had to show:

 # The and operator:
  In this expression the interpreter is trying to find out whether X is greater than 0 and whether Y is greater than 0. Upon printing the result it gives a single True value, why is this? Well the 'and' operator gives a True value if both X and y are True and False otherwise. It combines both into one and gives a single answer on both.

 # The or operator:
  In this expression the interpreter is trying to find out whether X is greater than 0 or whether Y is greater than 0. Upon printing the result it gives a single True   value, why? Well the or operator gives a True value if either X or y is True, while giving a False value if otherwise. One of the parameters in the operator influences the outcome of the other. 
  
  # The not operator:
  In this expression the interpreter is logically reversing the sense of the parameters given. In our example we know X is greater than 0 however the 'not' operator reverses that and makes the output False upon printing our answer. 
  
  
  
  Hopefully i have explained and coded the interpreters well, I trust that this documentation helps when reading the code and both are easy to understand and reproduce.
