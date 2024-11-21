# Discord Task Manager Bot

This is a simple task manager bot built using Python and SQLite. It allows users to add, list, delete, and mark tasks as complete directly from Discord using commands. The bot utilizes the `discord.py` library for interacting with Discord and `sqlite3` for storing task data.

## Features

- **Add a task**: Add new tasks to the database with a description.
- **Delete a task**: Remove tasks from the database using the task ID.
- **List all tasks**: View all tasks in the database along with their completion status.
- **Mark task as complete**: Mark tasks as complete using the task ID.

## Requirements

- Python 3.8+
- `discord.py` library
- `sqlite3` (included with Python standard library)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/umtcntp/lv3-dc-bot-task.git
    ```

2. Navigate into the project directory:

    ```bash
    cd lv3-dc-bot-task
    ```

3. Install the required dependencies using `Pipenv`:

    ```bash
    pip install pipenv
    pipenv install
    ```

    This will automatically create a virtual environment and install all the dependencies listed in the `Pipfile`.

4. Create a `bot_token.py` file in the root directory containing your Discord bot token:

    ```python
    token = 'YOUR_BOT_TOKEN'
    ```

5. Run the bot:

    ```bash
    pipenv run python bot.py
    ```

---

Make sure to use `pipenv run` to run any Python commands in the virtual environment, like starting the bot or running tests.


## Usage

Once the bot is running, you can use the following commands:

- **`!add_task <description>`**: Adds a new task to the database.
- **`!delete_task <task_id>`**: Deletes a task by its ID.
- **`!show_tasks`**: Lists all tasks in the database.
- **`!complete_task <task_id>`**: Marks a task as complete by its ID.

## Testing

This project uses `unittest` for testing the database operations. The tests check the functionality of task addition, listing, deletion, and marking tasks as complete.

### Running Tests

You can run all the tests at once using the `run_tests.py` script:

1. Ensure you are in the root directory of the project.

2. Run the `run_tests.py` script to execute all the individual tests:

    ```bash
    pipenv run python run_tests.py
    ```

The script will automatically run the following test files in order:

- `test_add_task.py`: Tests the task addition functionality.
- `test_delete_task.py`: Tests the task deletion functionality.
- `test_show_tasks.py`: Tests the task listing functionality.
- `test_complete_task.py`: Tests the task completion functionality.

Each test file will be executed sequentially, and the output will show whether the tests passed or failed.

### Running Individual Test Files

If you'd prefer to run the test files individually, you can do so with the following commands:

```bash
pipenv run python3 tests/test_add_task.py
pipenv run python3 tests/test_delete_task.py
pipenv run python3 tests/test_show_tasks.py
pipenv run python3 tests/test_complete_task.py
```

## Database Structure

The database is a SQLite file (`taskDB.db`) with a single table `tasks`, structured as follows:

| Column      | Type    | Description                    |
|-------------|---------|--------------------------------|
| `_id`       | INTEGER | Auto-incrementing primary key. |
| `task`      | TEXT    | Description of the task.       |
| `complete`  | BOOLEAN | Status of the task (0 for incomplete, 1 for complete). |



## File Structure

```javascript
discord-task-manager/
├── bot.py                      # Main bot file to run the task manager bot
├── bot_token.py                # Your bot token (keep this file private)
├── database.py                 # Contains the functions for interacting with the database
├── run_test.py                 # Script to run all the unit tests
├── Pipfile                     # Pipenv dependency management file
├── Pipfile.lock                # Lock file for Pipenv dependencies
├── tasksDB.db                  # SQLite database where tasks are stored
└── tests/                      # Folder containing unit tests
    ├── test_add_task.py        # Tests for adding tasks
    ├── test_complete_task.py   # Tests for marking tasks as complete
    ├── test_delete_task.py     # Tests for deleting tasks
    └── test_show_tasks.py      # Tests for showing tasks
```

## Contributing

Feel free to fork the repository and submit issues or pull requests. Any contributions are welcome!
