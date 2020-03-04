# lecture-20-unittests-review

Unit test review

## Run the tests (review)

Unlike last lecture, the tests are in a different directory (before, tests were simply in a different file). In
order to run them, tell Python to execute the `unit_tests` module inside `tests/` (or `tests.`):


```
vocstartsoft:~/environment $ cd lecture-20-unittests-review/
```
(for version python 2.7)
```
vocstartsoft:~/environment/lecture-20-unittests-review (master) $ python -m tests/unit_tests
```
or (for version python 3.6)
```
vocstartsoft:~/environment/lecture-20-unittests-review (master) $ python -m tests.unit_tests
```
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
vocstartsoft:~/workspace/lecture-19-unittests-review (master) $
```

## Write the remaining tests and fix the buggy code! (update!)

Look at function `get_chatbot_response` inside `functions.py`.

It's a buggy function! Given a particular
user input, it's intended to return what a chatbot would say.

There are four commands -- `hello`, `add`, `divide`, and `say`, and they should
all be usable like your chatbot would be!

(As an example, `get_chatbot_response("Hey <name>")` should return `"What's up!"`.)

Fix the rest of the `get_chatbot_response` function and update the unit tests. The first unit test has been done for you.

## Tips for getting started

Jot down some test cases (very similar to last lecture) to test ALL the functionality of the function.
Fix the rest of the `get_chatbot_response` function and update the unit tests. 
