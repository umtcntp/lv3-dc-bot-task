import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import  create_table, add_task_to_db, list_tasks, drop_table

class TestAddTask(unittest.TestCase):

    def setUp(self):
        drop_table()
        create_table()

    def test_add_task(self):
        add_task_to_db("Test Task")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test Task")
        print("Task added successfully")
        drop_table()


if __name__ == "__main__":
    unittest.main()





