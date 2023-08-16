# Python - if/else, loops, functions

## Concepts: 
Conditionals and loops in Python by using `if`,
`if ... else`, `break`, `continue`, `pass`, and `range` statements with `while` and
`for` loops. 

Python functions, variables, tracebacks, and arithmetic operators.

## Function Prototypes

Prototypes for functions written in this project:

| File                       | Prototype                                               |
| -------------------------- | ------------------------------------------------------- |
| `7-islower.py`             | `def islower(c):`                                       |
| `8-uppercase.py`           | `def uppercase(str):`                                   |
| `9-print_last_digit.py`    | `def print_last_digit(number):`                         |
| `10-add.py`                | `def add(a, b):`                                        |
| `11-pow.py`                | `def pow(a, b):`                                        |
| `12-fizzbuzz.py`           | `def fizzbuzz():`                                       |
| `13-insert_number.c`       | `listint_t *insert_node(listint_t **head, int number);` |
| `101-remove_char_at.py`    | `def remove_char_at(str, n):`                           |
| `102-magic_calculation.py` | `def magic_calculation(a, b, c):`                       |


### Task 0
  * [0-positive_or_negative.py](./0-positive_or_negative.py): Python program that assigns
  a random signed number to the variable `number` each time it is executed and
  prints whether `number` is positive or negative.
  * Prints the number followed by:
    * If the number is greater than 0: `is positive`
    * If the number is 0: `is zero`
    * If the number is less than 0: `is negative`
    * Followed by a new line.
  * Completion of [this source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py).

### Task 1
  * [1-last_digit.py](./1-last_digit.py): Python program that assigns a random signed number
  to the variable `number` each time it is executed and prints its last digit.
  * Prints the string `Last digit of [number] is [last_digit]` followed by:
    * If the number is greater than 5: `and is greater than 5`
    * If the number is 0: `and is 0`
    * If the number is less than 6 and not 0: `and is less than 6 and not 0`
    * Followed by a new line.
  * Completion of [this source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py).

### Task 2
  * [2-print_alphabet.py](./2-print_alphabet.py): Python program that prints the alphabet
  in lowercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.

### Task 3
  * [3-print_alphabt.py](./3-print_alphabt.py): Python program that prints the
  alphabet in lowercase, followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.
  * Prints every letter except for `q` and `e`.

### Task 4
  * [4-print_hexa.py](./4-print_hexa.py): Python program that prints all numbers from
  `0` to `98` in decimal and hexadecimal.
  * Using only one `print` and one loop.
  * Without storing numbers or strings in variables or importing modules.
  * Printing format: `[decimal] = [hexadecimal]`

### Task 5
  * [5-print_comb2.py](./5-print_comb2.py): Python program that prints numbers from `0`
  to `99` two digits each.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without storing numbers or strings in variables or importing modules.

### Task 6
  * [6-print_comb3.py](./6-print_comb3.py): Python program that prints all possible
  different combinations of two digits in ascending order.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * The two digits must be different - `01` and `10` are considered identical.
  * Using no more than three `print` functions and two loops.
  * Without storing numbers or strings in variables or importing modules.

### Task 7
  * [7-islower.py](./7-islower.py): Python function that checks for lowercase characters.
  * Returns `True` if `c` is lowercase, `False` otherwise.
  * Without importing modules or using `str.upper()` or `str.isupper()`.

### Task 8
* **8. To uppercase**
  * [8-uppercase.py](./8-uppercase.py): Python function that prints a string in
  uppercase followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without importing modules or using `str.upper()` or `str.isupper()`.

### Task 9
  * [9-print_last_digit.py](./9-print_last_digit.py): Python function that prints the last
  digit of a number.
  * Returns the value of the last digit.
  * Without importing modules.

### Task 10
  * [10-add.py](./10-add.py): Python function that returns the addition of two integers.
  * Without importing modules.

### Task 11
  * [11-pow.py](./11-pow.py): Python function that returns `a` to the power of `b`.
  * Without importing modules.

### Task 12
  * [12-fizzbuzz.py](./12-fizzbuzz.py): Python function that prints the numbers from
  `1` to `100` followed by a space.
  * For multiples of three, `Fizz` is printed instead of the number.
  * For multiples of five, `Buzz` is printed instead of the number.
  * For multiples of three and five, `FizzBuzz` is printed instead of the number.
  * Without importing modules.


