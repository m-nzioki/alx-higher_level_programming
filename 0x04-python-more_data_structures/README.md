# 0x04. Python - More Data Structures: Set, Dictionary

## Concepts
  * Data Structures
  * Lamda, filter, reduce, map

| File  | Prototype  |
| ----- | -----      |
| `0-square_matrix_simple.py` | `def square_matrix_simple(matrix=[]):` |
| `1-search_replace.py` | `def search_replace(my_list, search, replace):` |
| `2-uniq_add.py` | `def uniq_add(my_list=[]):` |
| `3-common_elements.py` | `def common_elements(set_1, set_2):` |
| `4-only_diff_elements.py` | `def only_diff_elements(set_1, set_2):` |
| `5-number_keys.py` | `def number_keys(a_dictionary):` |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):` |
| `7-update_dictionary.py` | `def update_dictionary(a_dictionary, key, value):` |
| `8-simple_delete.py` | `def simple_delete(a_dictionary, key=""):` |
| `9-multiply_by_2.py` | `def multiply_by_2(a_dictionary):` |
| `10-best_score.py` | `def best_score(a_dictionary):` |
| `11-multiply_list_map.py` | `def multiply_list_map(my_list=[], number=0):` |
| `12-roman_to_int.py` | `def roman_to_int(roman_string):` |

### Task 0
* [0-square_matrix_simple.py](./0-square_matrix_simple.py) : Computes the square value of all integers of a matrix.
* `matrix` is a 2 dimensional array
* Returns a new matrix:
    * Same size as matrix
    * Each value should be the square of the value of the input
* Initial matrix should not be modified
* Not allowed to import any module
* Allowed to use regular loops, map, etc.

### Task 1
* [1-search_replace.py](./1-search_replace.py) : Replaces all occurrences of an element by another in a new list.
* `my_list` is the initial list
* `search` is the element to replace in the list
* `replace` is the new element

### Task 2
* [2-uniq_add.py](./2-uniq_add.py) : Adds all unique integers in a list (only once for each integer).

### Task 3
* [3-common_elements.py](./3-common_elements.py) : Returns a set of common elements in two sets.

### Task 4
* [4-only_diff_elements.py](./4-only_diff_elements.py) : Returns a set of all elements present in only one set.

### Task 5
* [5-number_keys.py](./5-number_keys.py) : Returns the number of keys in a dictionary.

### Task 6
* [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py) :  prints a dictionary by ordered keys.
* All keys are strings
* Keys to be sorted by alphabetic order
* Dictionary values can have any type

### Task 7
* [7-update_dictionary.py](./7-update_dictionary.py) : Replaces or adds key/value in a dictionary.
* `key` argument will be always a string
* `value` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created

### Task 8
* [8-simple_delete.py](./8-simple_delete.py) : Deletes a key in a dictionary.
* `key` argument will be always a string
* If a key doesn’t exist, the dictionary won’t change

### Task 9
* [9-multiply_by_2.py](./9-multiply_by_2.py) : Returns a new dictionary with all values multiplied by 2
* All values are only integers
* Returns a new dictionary

### Task 10
* [10-best_score.py](./10-best_score.py) : Returns a key with the biggest integer value.
* All values are only integers
* If no score found, return `None`
* All students have a different score

### Task 11
* [11-multiply_list_map.py](./11-multiply_list_map.py) : Returns a list with all values multiplied by a number without using any loops.
* Returns a new list
   * Same length as `my_list`
   * Each value should be multiplied by `number`
* Have to use `map`

### Task 12
* [12-roman_to_int.py](./12-roman_to_int.py) : Converts a Roman numeral to an integer.
* The  number will be between 1 to 3999.
* Returns an intrger.
* If the `roman_string` is not a string or `None`, returns 0
