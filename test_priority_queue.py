import unittest
import priority_queue as pq

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):

        ''' Set up an instance and priority list to test. '''

        self.example = pq.PriorityQueue()
        self.example.push(5,'homework')
        self.example.push(6, 'class')
        self.example.push(2, 'work')
        self.example.push(7, 'hoop')
        self.example.push(3, 'chores')

    def test_init(self):

        ''' Tests whether the init method sets up an empty dictionary and instance '''

        self.assertIsInstance(self.example, pq.PriorityQueue)
        self.assertIsInstance(self.example.queue, dict)

    def test_push(self):

        ''' Tests if the push method adds values and keys to the dictionary '''

        self.assertEqual(self.example.queue[5],['homework'])
        self.assertEqual(self.example.queue[6],['class'])
        self.assertEqual(self.example.queue[2],['work'])
        self.assertEqual(self.example.queue[7],['hoop'])
        self.assertEqual(self.example.queue[3],['chores'])
    
    def test_maxpriority(self):

        ''' Tests if the max priority method returns the highest priority '''

        self.assertEqual(self.example.max_priority(), 7)
    
    def test_pop(self):

        ''' Tests if the pop method removes the highest priority and object
            from the dictionary '''

        self.assertEqual(self.example.pop(), (7, 'hoop'))

    def test_peek(self):

        ''' Tests if the peek method returns the highest priority along with
            its object. '''

        self.assertEqual(self.example.peek()[0], 7)
        self.assertEqual(self.example.peek()[1],'hoop')

    def test_len(self):

        ''' Tests if the __len__ method returns the number of priorities in the
            queue. '''

        self.assertEqual(self.example.__len__(), 5)


if __name__ == "__main__":
    unittest.main()