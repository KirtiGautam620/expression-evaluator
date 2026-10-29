# Expression Evaluator

A small command-line calculator in Python that evaluates math expressions without using `eval()` or any libraries.

## Features

- `+`, `-`, `*`, `/`
- Parentheses and decimal numbers
- Correct operator precedence (`2 + 3 * 4` is `14`)
- Negative numbers (`-5`, `3 * -2`, `-(2 + 3)`)
- Error messages for invalid expressions and division by zero

## How it works

1. **Tokenizer**: turns the input string into a list of numbers and symbols.
   `"2 + 3.5"` becomes `[2.0, '+', 3.5]`
2. **Parser**: a recursive descent parser that computes the result while reading the tokens. It follows this grammar:

```
expression -> term (('+' | '-') term)*
term       -> factor (('*' | '/') factor)*
factor     -> number | '(' expression ')' | '-' factor
```

Precedence comes from the structure: `term` handles `*` and `/` before `expression` gets to `+` and `-`. Parentheses and negative numbers are handled by recursion in `factor`.

## Usage

```
python3 evaluator.py
```

```
Simple Expression Evaluator
Type 'exit' to quit.
> 2 + 3 * (4 - 1)
11
> -2.5 * 4
-10
> 5 / 0
Error: division by zero
> exit
Bye!
```

## Tests

```
python3 test_evaluator.py
```
