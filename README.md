# Assignment #4

This assignment evaluates the creation of iterables and iterator objects. It
consists of two parts, each worth 50%.

## Part 1 – Fibonacci Iterable `(/24)`

Write an iterable which produces an iterator of the Fibonacci series for a
given value.

Example:

```python
>>> [number for number in Fibonacci(10)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

### `(/3)` Structure & naming
- `(/1)` Write a test module called `test_fibonacci.py`
- `(/1)` Write a module called `fibonacci.py`
- `(/1)` Create an iterable class called `Fibonacci` which requires a single
  positional argument.


### Requirements & build steps
Using TDD methodology, develop an algorithm to assert the following test
cases.

Note: iterables return iterators and not lists, so to build a proper assertion,
cast the result as a list.

```python
assert list(Fibonacci(2)) == [0, 1, 1]
```

1. If constructed with a value other than an integer, the Fibonacci constructor
  should raise a ValueError.
1. Given a constructor value of 0, the iterator should produce the values `[0]`
   if cast as a list.
1. Given a constructor value of 1, the iterator should produce the values
`[0, 1]` if cast as a list.
1. Given a constructor value of 2, the iterator should produce the values
`[0, 1, 1]`.
1. Given a value of 4, the iterator should produce `[0, 1, 1, 2, 3]`
1. Given a value of 10, the iterator should produce
`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`
1. Given a negative value, the iterator should produce an empty list.

**Note:** Any integer must be accepted and calculate a correct Fibonacci
sequence. Building a function which only handles the above cases is
insufficient and will not be accepted.

### `(/21)` Development matrix
| Step | Test assertion | Code to pass | Commit Exists |
| ---- | ---- | ---- | ------ |
| **#1** | | | |
| **#2** | | | |
| **#3** | | | |
| **#4** | | | |
| **#5** | | | |
| **#6** | | | |
| **#7** | | | |


### Part 2 – Prime numbers (revisited) `(/27)`
This second part is a reimplementation of the prime numbers algorithm from
assignment #2, but this time as a generator function.


### `(/3)` Structure & naming
- `(/1)` Write a test module called `test_prime.py`
- `(/1)` Write a module called `prime.py`
- `(/1)` Create a generator function called `generate_prime_numbers` which
requires a single positional argument.


### Requirements & build steps
### Step 1:
Write a test that asserts that when `generate_prime_factors` is called with a
data type that is not an integer (e.g. a string or float), a ValueError is
raised. Write the appropriate code to solve this and then commit the changes.


### Step 2:
Write a test that asserts that when `generate_prime_factors` is called with
`1`, an empty list will be generated. Solve & commit.


### Step 3:
Write a test that asserts that when `generate_prime_factors` is called with
`2`, the list `[2]` will be generated. Solve & commit.


### Step 4:
Write a test that asserts that when `generate_prime_factors` is called with
`3`, the list `[3]` will be generated. Solve & commit.


### Step 5:
Write a test that asserts that when `generate_prime_factors` is called with
`4`, the list `[2, 2]` will be generated. Solve & commit.


### Step 6:
Write a test that asserts that when `generate_prime_factors` is called with
`6`, the list `[2, 3]` will be generated. Solve & commit.


### Step 7:
Write a test that asserts that when `generate_prime_factors` is called with
`8`, the list `[2, 2, 2]` will be generated. Solve & commit.


### Step 8:
Write a test that asserts that when `generate_prime_factors` is called with
`9`, the list `[3, 3]` will be generated. Solve & commit.


| Step | Test assertion | Code to pass | Commit Exists |
| ---- | ---- | ---- | ------ |
| **#1** | | | |
| **#2** | | | |
| **#3** | | | |
| **#4** | | | |
| **#5** | | | |
| **#6** | | | |
| **#7** | | | |
| **#8** | | | |
