# Norman PD Incidents Parser (Project 0)
Norman PD Incidents Parser is a python based utillity tool used to extract incidents data from a provided incident PDF file URL.

> The project's python code follows PEP8 Style Guide

## Run on local system
1. Clone this repository and move into the folder.
    ```sh
    $ git clone https://github.com/Biswas-N/cs5293sp22-project0.git
    $ cd cs5293sp22-project0
    ```
2. Install dependencies using [Pipenv](https://github.com/pypa/pipenv).
    ```sh
    $ pipenv install
    ``` 
3. Run the utility tool
    ```sh
    $ make
    ```
   > Note: Project includes a `Makefile` which has commonly used commands. By running `make` the following command `pipenv run python main.py --incidents <Sample URL>'` is executed.

## Documentation

The documentation about code structure and extraction algorithm can be found [here](./docs/Index.md).

## Testing

This utility is tested using [pytest](https://github.com/pytest-dev/pytest). Follow the below commands to run tests on your local system.
1. Install dev-dependencies.
    ```sh
    $ pipenv install --dev
    ```
2. Run tests using `Makefile`.
    ```sh
    $ make test
    ```
3. Run test coverage.
    ```sh
    $ make cov
    ```