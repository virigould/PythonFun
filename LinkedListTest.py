import unittest
from LinkedList import LinkedList


class TestStringMethods(unittest.TestCase):
    def test_constructor(self):
        test_list = LinkedList()
        self.assertTrue(isinstance(test_list, LinkedList))

    def test_add_and_get(self):
        test_list = LinkedList()
        test_list.add("This is a String")
        test_list.add("this is another test String")
        test_list.add("This is also a test string")
        test_list.add("I wonder if there is a limit on the amount of objects I can put in this list")
        # lets find out
        for i in range(0, 100):
            test_list.add("a{}".format(i))
        self.assertIsNotNone(test_list.get(64))
        self.assertEqual("This is a String", test_list.get(0))
        self.assertEqual("this is another test String", test_list.get(1))
        self.assertEqual(1, test_list.get_index_of("this is another test String"))
        self.assertEqual(43, test_list.get_index_of("a39"))

    def test_remove_and_size(self):
        test_list = LinkedList()
        test_list.add("This is a test String")
        test_list.add("This is another test String")
        self.assertTrue(2 == test_list.size())
        test_list.remove(0)
        self.assertTrue(1 == test_list.size())
        for i in range(0, 100):
            test_list.add("a{}".format(i))
        self.assertEqual(101, test_list.size())
