import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import  create_table, add_task_to_db, list_tasks, drop_table,mark_task_complete



class TestShowTask(unittest.TestCase):

    def setUp(self):
        drop_table()
        create_table()
        add_task_to_db("Test Task")

    def test_show_task(self):
        task_list = list_tasks()
        self.assertEqual(task_list[0][1], "Test Task")
        print("Task List: ", task_list)
        print("Tasks listed succesfully")
        drop_table()
        
if __name__ == "__main__":
    unittest.main()