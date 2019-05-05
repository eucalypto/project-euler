# Problem 1

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

## Solution

The solution is `233168`
and the code is in `"problem 1.py"`.


## Thougt process

The main problem is to find all multiples of 3 or 5 up to 1000. The sum is just a check ("hash") that all numbers were found.

The main trick is not to double count numbers that are multiples of both 3 and 5.

My solution is the most brute-force that I could think of: `"problem 1.py"`