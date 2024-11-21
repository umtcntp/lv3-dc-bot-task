import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import  create_table, add_task_to_db, list_tasks, drop_table,mark_task_complete



class TestCompleteTask(unittest.TestCase):

    def setUp(self):
        drop_table()
        create_table()
        add_task_to_db("Test Task")

    def test_complete_task(self):
        mark_task_complete(1)
        task_list = list_tasks()
        self.assertEqual(len(task_list), 1)
        self.assertEqual(task_list[0][2], 1)
        print("Task marked as complete successfully")
        drop_table()
        
if __name__ == "__main__":
    unittest.main()