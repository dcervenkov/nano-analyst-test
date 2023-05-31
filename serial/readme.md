## Exercise 4 - JSON (de)serialization

Here you will demonstrate active knowledge of (JSON) serialization and de-serialization in Python.

There are two tasks:
1. Implement data model `ServiceRequest` in submodule `datamodels` with fields indicated
by the parameterization of the unit test `test_serial`. Use either Python dataclass or pydantic BaseModel.
2. Complete the unit test `test_serial` that verifies the correct function of helper utils
needed for (de)serialization of objects with `datetime.datetime` fields. You are expected to use
`json` module of standard Python library.

You can test validity of your implementation by runing the test suite (`pipenv run tests -s serial`).