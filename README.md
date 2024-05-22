# Conway's Game of Life

## a. Steps to Run the Code
1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_GITHUB_NAME/YOUR_PROJECT_NAME.git
    cd YOUR_PROJECT_NAME
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv game_of_life_env
    source game_of_life_env/bin/activate  # On Windows: game_of_life_env\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the game:
    ```bash
    python main.py
    ```

## b. Configuration File Description
Create a `config.cfg` file with the following structure:
```ini
[GAME]
height = 10
width = 10
iterations = 10
ruleset = 23/3
p_cell_alive = 0.3

[VISUAL]
char_alive = *
char_dead = .
wait_time = 0.5
```

## c. Run test cases

```bash
pytest
```
## d. Test Coverage

Run tests with coverage:
```bash
coverage run -m pytest
```
Generate coverage report
```bash
coverage report -m
```

## e. What I learned
In this project, I learned how to structure a Python project using classes and modules. 
I also learned how to validate inputs and write comprehensive tests to ensure high test coverage. 
The most challenging part was managing the interactions between different classes and ensuring thorough testing.

