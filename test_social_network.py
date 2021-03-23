import unittest
import social_network

class TestPerson(unittest.TestCase):
    def setUp(self):
        """ Create some people for our tests. """
        self.p = social_network.Person("Bob")
        self.p2 = social_network.Person("Pat")
        self.p3 = social_network.Person("Dave")
        self.p4 = social_network.Person("Rose")
        self.p5 = social_network.Person("Kelly")
    
    def test_init(self):
        """ Test whether init method sets name and connections
        attributes correctly. """
        self.assertIsInstance(self.p, social_network.Person)
        self.assertEqual(self.p.name, "Bob")
        self.assertIsInstance(self.p.connections, set)
        self.assertFalse(self.p.connections)
        
    def test_add_conn(self):
        """ Test whether add_connection method creates symmetric
        connections between two people. """
        result = self.p.add_connection(self.p2)
        self.assertIsNone(result)
        self.assertEqual(self.p.connections, {self.p2})
        self.assertEqual(self.p2.connections, {self.p})
        # make sure we can't connect a person to themselves
        with self.assertRaises(ValueError):
            self.p.add_connection(self.p)
        # make sure that when we add additional connections, the old
        # ones don't go away
        self.p2.add_connection(self.p3)
        self.assertEqual(self.p2.connections, {self.p, self.p3})

    def test_second_connections(self):
        # if a person has no connections, they should have no second
        # connections either
        self.assertEqual(self.p.get_second_connections(), set())
        self.p.add_connection(self.p2)
        # if two people have no connections other than each other, they
        # should have no second connections
        self.assertEqual(self.p.get_second_connections(), set())
        # create and check for an actual second connection
        self.p2.add_connection(self.p3)
        self.assertEqual(self.p.get_second_connections(), {self.p3})
        # p2 has two first connections but still no second connections
        self.assertEqual(self.p2.get_second_connections(), set())
        self.p2.add_connection(self.p4)
        # p should now have two second connections
        self.assertEqual(self.p.get_second_connections(), {self.p3, self.p4})
        # p should now have a third connection; make sure the set of second
        # connections has not changed
        self.p5.add_connection(self.p4)
        self.assertEqual(self.p.get_second_connections(), {self.p3, self.p4})


class TestFunctions(unittest.TestCase):
    def test_build_network(self):
        pairs = [("Kurt", "Alex"),
                    ("Kurt", "John"),
                    ("Alex", "David"),
                    ("Alex", "John"),
                    ("John", "Steve"),
                    ("John", "Matt"),
                    ("Jamie", "Steve"),
                    ("Lisa", "Matt"),
                    ("David", "Joe")]
        people = social_network.build_network(pairs)
        self.assertIsInstance(people, dict)
        for person1, person2 in pairs:
            self.assertIn(person1, people)
            self.assertIn(person2, people)
            self.assertIsInstance(people[person1], social_network.Person)
            self.assertIsInstance(people[person2], social_network.Person)
            self.assertIn(people[person1], people[person2].connections)
            self.assertIn(people[person2], people[person1].connections)


if __name__ == "__main__":
    unittest.main()