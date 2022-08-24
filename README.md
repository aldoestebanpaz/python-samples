## How to run the tests

**Run all tests**

Run the following command in this top directory (where the /src directory is located):

```sh
pipenv run python -m pytest
```

NOTE: use `pipenv run python -m pytest` instead of `pipenv run pytest`, because it will add the current directory to 'sys.path' (which is standard python behavior) while `pipenv run pytest` don't (and will fail trying to find the modules in the src/ directory).

**Run single test file**

Run the following command in this top directory (where the /src directory is located):

```sh
pipenv run python -m pytest <TEST_FILE>
```

Example:

```sh
pipenv run python -m pytest tests/api/test_todos_api.py
```

**Run single test case**

Run the following command in this top directory (where the /src directory is located):

```sh
pipenv run python -m pytest <TEST_FILE>::<TEST_FUNC_NAME>
```

Example:

```sh
pipenv run python -m pytest tests/api/test_todos_api.py::test_fetch_todo_returns_successful_response
```

**Run single test case using custom markers**

You could add custom mark metadata like the following:

```python
@pytest.mark.my_custom_mark
def test_send_email():
  # ...
```

Then you can run:

```sh
pipenv run python -m pytest -m my_custom_mark
```

NOTE: Unregistered marks applied with the @pytest.mark.name_of_the_mark decorator will always emit a warning in order to avoid silently doing something surprising due to mistyped names. See [How to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html) for details.

## Key concepts to understand unit testing using pytest

TODO

### The rule of thumb for mocking

```
Mock where it is used, and not where it’s defined (source).
```

## Tests with stub objects

TODO

## Tests with mock objects

TODO

**test_todos_api.py**

This file contains examples of how to mock functions of libraries like 'requests'. Additionally it contains the different options of mocking functions and objects using either unittest.mock or either the 'mocker' object from 'pytest-mock'.

## Tests with spy objects

TODO
