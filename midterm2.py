import eleven as el
import random

class HumanPlayer(el.Player):

    def __init__(self):
        super().__init__()

    def get_move(self):

        el.clear_screen()
        
        print(self.board)
        print(self.score)

        moves = ''
        while moves not in self.board.valid_moves():
            moves = input('')
            if moves not in self.board.valid_moves():
                print('',self.board.valid_moves())
        

    def play(self):
        dub = super().play()

        if dub == True:
            print("You Win!")
        else:
            print("Game Over.")


        
class ComputerPlayer(el.Player):

    def __init__(self):
        super().__init__()
    
    def play(self):
        super().play()

    def get_move(self):
        move = random.choice(self.board.valid_moves())
        return move

class ComputerPlayer2(ComputerPlayer):
    
    def __init__(self):
        super().__init__()

    def play(self):
        super().play()
    
    def get_move(self):    
    
        gm = super().get_move()
        for move in self.board.valid_moves():
            b,score = self.board.calculate_move(move)
            b = [0 if elem == None else elem for elem in b]
            bs = 0
            if score > bs:
                bs += score
                gm = move
        return gm

if __name__ == '__main__':
    print(el.test_player(ComputerPlayer2))