
class Ballot:

    ''' This class will be used to parse through a text file with a list of 
        ballots containing candidates and their amount of votes, calculate a 
        winner of the votes, and find the preffered candidate. 

        Attributes: votes - a dictionary containing candidates and their vote
        values.
    '''

    def __init__(self, vote_str):

        self.votes = self.parse_votes(vote_str)

    def parse_votes(self, vote_str):

        ''' This method parses through the text file using the string provided
            from the vote_str argument, and creates a dictionary with the 
            candidates and their vote values.

            Args: vote_str - a string containing a list of candidates and values

            Returns: A dictionary with candidates set as keys and their values 
                     as number of votes
        '''

        if vote_str[-1] == '\n':
            vote_str = vote_str[:-1]

        votelist = vote_str.split(',')

        votes = {}

        for votedict in votelist:
            votedict = votedict.split(':')
            votes[votedict[0]] = int(votedict[1])
        return votes   
                        

    def preference(self, candidate1, candidate2):

        ''' This method finds the preferred candidate by finding out which 
            candidate has more votes and ballot wins

            Args: candidate1 - the first candidate from the dict
                  candidate2 - the second candidate from the dict
            
            Returns: the preferred candidate between the two, or None
        '''

        if self.votes[candidate1] > self.votes[candidate2]:
            return candidate1
        elif self.votes[candidate2] > self.votes[candidate1]:
            return candidate2
        else:
            return None


def read_ballots(fpath):

    ''' This function retrieves the data from the filepath provided, opens and
        reads the file, and creates a list for the ballots using an instance of
        the Ballot class.

        Args: fpath - the filepath of the file used for this script.

        Returns: A list of ballot objetcs from the instance of the Ballot class
    '''

    ballots = []
    with open (fpath, 'r') as f:
        for lines in f:
            ballot = Ballot(lines)
            ballots.append(ballot)
    return ballots 

def find_winner(ballots):

    ''' This function calculates the winner of the ballot list provided from
        the read_ballots function.

        Args: ballot - the ballot lists from the read_ballot function

        Returns: Winner of the ballot votes by preference and ballot list.
    '''

    total_scores = {key: 0 for key in ballots[0].votes}

    for ballot in ballots:
        for candidate in ballot.votes:
            total_scores[candidate] += ballot.votes[candidate]

    score = sorted(total_scores.items(), key=lambda x: x[1])

    first = score[-1][0]
    second = score[-2][0]

    prefcount1 = 0
    prefcount2 = 0

    for ballot in ballots:
        pref = ballot.preference(first, second)
        if pref == first:
            prefcount1 += 1
        elif pref == second:
            prefcount2 += 1

    if prefcount1 > prefcount2:
        return first
    else:
        return second

    return ballot

def main(fpath):

    votelist = read_ballots(fpath)
    print(find_winner(votelist))
    

if __name__ == "__main__":

    import sys

    print(main(sys.argv[1:]))
