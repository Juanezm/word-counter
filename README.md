# Word Counter

## Requirements

Write a program in python which accepts a single list as a parameter.

This list consist of any number of list (1..n), and you can **assume** each list only contains words.

The program should print out the following:
- Words that appear in more than one list
- The total number of unique words across all lists
- Top five frequent words in all the lists

## Assumptions

- Since there are not user interface requirements, a simple CLI has been chosen for this.
- No mention of data persistence, a simple json file to store the words will be used for this.
- Each list can contain repeated words.

## Implementation

A simple *wordcounter* python package has been created to meet the requirements.

To structure the application, all is built around a **domain service** that represents the business logic as operations.
In order to decouple the domain service from the data layer, dependency inversion principle (**DIP**) has been used 
over data storage, by adding the **repository pattern** that hides details of data access by pretending that all our
data is in memory. Also simplifies the task of using a different storage method without disrupting the core application.

All the code has been written following Test Driven Development (**TDD**), to ensure the code meets the expected behaviour
without regression issues.

## Tests

To execute the different type of tests, a Makefile has been provided to simplify this.

- Run unit-tests ```make unit-tests```
- Run integration-tests ```make integration-tests```
- Run e2e-tests ```make e2e-tests```
- Run all tests ```make tests```


## Installation

The use of virtual environment to run the code is recommended. This can be easily done executing
```make install-package```. If you don't have access to make command, or want to do it manually:

```
> python3 -m venv venv
> source venv/bin/activate (venv\Scripts\activate.bat if you are on Windows)
> pip install .
```

## Usage
The CLI tool can be invoked using ```wordcounter-cli```:

```
> wordcounter-cli --help
Usage: wordcounter-cli [OPTIONS] JSON_FILE

Options:
  --input-list TEXT  This is the input list. Example: apple, mango, cherry
  --help             Show this message and exit.
```

An example of execution can be:

```
> wordcounter-cli --input-list 'apple, orange, grapes, apple, orange' data/words.json
```

The expected output, assuming it is the first list added:
```
Repeated words:
- apple
- orange

Unique words:
- grapes

Top five frequent words:
- apple
- orange
- None
- None
- None
```

Another way of introducing the list of words is:
```
> wordcounter-cli data/words.json
Enter the input list separated by comma: 
```

and after introducing them we get a similar output than before

```
> wordcounter-cli data/words.json
Enter the input list separated by comma: apple, orange, grapes, apple, orange
Repeated words:
- apple
- orange

Unique words:
- grapes

Top five frequent words:
- apple
- orange
- None
- None
- None
```
