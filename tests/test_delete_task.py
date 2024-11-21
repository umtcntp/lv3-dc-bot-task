import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import  create_table, add_task_to_db, list_tasks, drop_table, delete_task_from_db

class TestDeleteTask(unittest.TestCase):

    def setUp(self):
        drop_table()
        create_table()
        add_task_to_db("Test Task")

    def test_delete_task(self):
        delete_task_from_db(1)
        task_list = list_tasks()
        self.assertEqual(len(task_list), 0)
        print("Task deleted successfully")
        drop_table()
        
if __name__ == "__main__":
    unittest.main()