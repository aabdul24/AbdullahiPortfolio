""" Module for modeling social networks (individuals and connections
between them). """

class Person:
    """ Models a person in a social network.
    
    Attributes:
        name (str): the person's name.
        connections (set of Person): the people connected to this
            person.
    """
    def __init__(self, name):
        """ Initialize the name and connections of a new Person object.
        
        Args:
            name (str): the name of the person.
        
        Side effects:
            Sets the object's name and connections attributes.
        """
        self.name = name
        self.connections = set()
    
    def add_connection(self, other):
        """ Create symmetric connections between self and other.
        
        Args:
            other (Person): another Person object.
        
        Side effects:
            Modifies the connections attributes of self and other.
            
        Raises:
            ValueError: self and other are the same object.
        """
        if other is self:
            raise ValueError("can't connect to self")
        if other not in self.connections:
            self.connections.add(other)
            other.add_connection(self)
    
    def get_second_connections(self):
        """ Return a set of all Person objects that are not self or
        connections of self, but that are connections of connections of
        self.
        
        Returns:
            set of Person: the second connections of self.
        """
        second_connections = set()
        for person in self.connections:
            second_connections |= person.connections
        second_connections -= self.connections
        second_connections.discard(self)
        return second_connections

def build_network(pairs):
    """ Build a network where each pair of names in pairs is a
    connection in the network.
    
    Args:
        pairs (list of sequence of str): a list containing two-item
            sequences (lists or tuples) where each item is a string
            representing the name of a person in the network. Each two-
            item sequence represents one connection in the network.
    
    Returns:
        (dict of str: Person): a dictionary where the keys are names of
        people in the network and each corresponding value is a Person
        object for the person with that name.
    """
    people = dict()
    for pair in pairs:
        for name in pair:
            if name not in people:
                people[name] = Person(name)
        people[pair[0]].add_connection(people[pair[1]])
    return people


def read_pairs(path, delim):
    """ Read pairs of names from a file. The file should consist of one
    pair of names per line. Each line should use the same delimiter to
    delimit the names.
    
    Args:
        path (str): path to the file containing pairs of names.
        delim (str): delimiter between each name in a pair.
    
    Returns:
        (list of (tuple of str, str)): a list of tuples. Each item in
        the list is a pair; each tuple consists of two strings
        corresponding to the two names in a pair.
    """
    pairs = list()
    with open(path, 'r', encoding='utf-8') as f:
        for line in path:
            pairs.append(line.strip().split(delim))
    return pairs


def load_network(path, delim):
    """ Read pairs of names from a file and build a social network. See
    read_pairs() for a description of the file format.
    
    Args:
        path (str): path to the file containing pairs of names.
        delim (str): delimiter between each name in a pair.

    Returns:
        (dict of str: Person): a dictionary where the keys are names of
        people in the network and each corresponding value is a Person
        object for the person with that name.
    """
    pairs = read_pairs(path, delim)
    network = build_network(pairs)
    return network
