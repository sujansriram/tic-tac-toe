
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QMenuBar, QHBoxLayout, QVBoxLayout


class TicTacToeWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.clickCounter = 0
        self.resetCounter = 0
        self.player1score = 0
        self.player2score = 0

        def onButtonClicked(x,y):
            self.clickCounter += 1
            button2 = self.buttonMatrix[x][y]
            button2.setText(str(self.getTurn()))
            button2.setEnabled(False)
            if button2.text() == 'X':
                button2.setStyleSheet("background-color: orange; border-radius : 10; border : 0.5px solid black; "
                                      "font: bold; font-size: 60px")
            if button2.text() == 'O':
                button2.setStyleSheet("background-color: lightGreen; border-radius : 10; border : 0.5px solid black; "
                                      "font: bold; font-size: 60px")

        def scoreChanger():
            if self.label.text() == 'Player 1 wins!':
                self.player1score += 1
                self.score1.setText('player 1 score:' + str(self.player1score))
            if self.label.text() == 'Player 2 wins!':
                self.player2score += 1
                self.score2.setText('player 2 score:' + str(self.player2score))

        def resetChecker():
            if (self.label.text() == 'Player 1 wins!') or (self.label.text() == 'Player 2 wins!') or (self.label.text() == 'Draw!'):
                self.buttonReset.setEnabled(True)
                self.resetCounter += 1
                self.buttonReset.clicked.connect(gameReset)

        def gameReset():
            for x in range(3):
                for y in range(3):
                    self.buttonMatrix[x][y].setText(' ')
                    self.buttonMatrix[x][y].setEnabled(True)
                    self.buttonMatrix[x][y].setStyleSheet("background-color: white; border-radius : 10; border : "
                                                          "0.5px solid black")
                    self.label.setText('')
                    self.buttonReset.setEnabled(False)
                    self.clickCounter = 0

        def gameWinChecker():
            if self.buttonMatrix[0][0].text() == 'X' and self.buttonMatrix[0][1].text() == 'X' and self.buttonMatrix[0][2].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[1][0].text() == 'X' and self.buttonMatrix[1][1].text() == 'X' and self.buttonMatrix[1][2].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[2][0].text() == 'X' and self.buttonMatrix[2][1].text() == 'X' and self.buttonMatrix[2][2].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[0][0].text() == 'X' and self.buttonMatrix[1][0].text() == 'X' and self.buttonMatrix[2][0].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[0][1].text() == 'X' and self.buttonMatrix[1][1].text() == 'X' and self.buttonMatrix[2][1].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[0][2].text() == 'X' and self.buttonMatrix[1][2].text() == 'X' and self.buttonMatrix[2][2].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[0][0].text() == 'X' and self.buttonMatrix[1][1].text() == 'X' and self.buttonMatrix[2][2].text() == 'X':
                self.label.setText('Player 2 wins!')
            if self.buttonMatrix[0][2].text() == 'X' and self.buttonMatrix[1][1].text() == 'X' and self.buttonMatrix[2][0].text() == 'X':
                self.label.setText('Player 2 wins!')

            if self.buttonMatrix[0][0].text() == 'O' and self.buttonMatrix[0][1].text() == 'O' and self.buttonMatrix[0][2].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[1][0].text() == 'O' and self.buttonMatrix[1][1].text() == 'O' and self.buttonMatrix[1][2].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[2][0].text() == 'O' and self.buttonMatrix[2][1].text() == 'O' and self.buttonMatrix[2][2].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[0][0].text() == 'O' and self.buttonMatrix[1][0].text() == 'O' and self.buttonMatrix[2][0].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[0][1].text() == 'O' and self.buttonMatrix[1][1].text() == 'O' and self.buttonMatrix[2][1].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[0][2].text() == 'O' and self.buttonMatrix[1][2].text() == 'O' and self.buttonMatrix[2][2].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[0][0].text() == 'O' and self.buttonMatrix[1][1].text() == 'O' and self.buttonMatrix[2][2].text() == 'O':
                self.label.setText('Player 1 wins!')
            if self.buttonMatrix[0][2].text() == 'O' and self.buttonMatrix[1][1].text() == 'O' and self.buttonMatrix[2][0].text() == 'O':
                self.label.setText('Player 1 wins!')

            if self.clickCounter == 9 and self.label.text() == '':
                self.label.setText('Draw!')

            if self.label.text() != '':
                for x in range(3):
                    for y in range(3):
                        self.buttonMatrix[x][y].setEnabled(False)

        layout = QGridLayout()

        # self.label1 = QLabel('Player 1 Wins:')
        # self.label2 = QLabel('Player 2 Wins:')
        #
        # layout.addWidget(self.label1)
        # layout.addWidget(self.label2)

        self.buttonMatrix = []
        for i in range(3):
            self.buttonMatrix.append([])
            for j in range(3):
                button = QPushButton(' ')
                button.clicked.connect(lambda _, x=i, y=j: onButtonClicked(x, y))
                button.clicked.connect(gameWinChecker)
                button.clicked.connect(resetChecker)
                button.clicked.connect(scoreChanger)
                self.buttonMatrix[i].append(button)
                button.setStyleSheet("background-color: white; border-radius : 10; border : 0.5px solid black;")
                button.setMinimumWidth(100)
                button.setMinimumHeight(100)
                layout.addWidget(button, i, j)

        self.label = QLabel('')
        layout.addWidget(self.label)
        self.label.setStyleSheet("font: bold")

        self.buttonReset = QPushButton('Reset')
        self.buttonReset.setMinimumHeight(40)
        layout.addWidget(self.buttonReset)
        self.buttonReset.setStyleSheet("background-color: white; border-radius : 10; border : 0.5px solid black;")
        self.buttonReset.setEnabled(False)

        layout2 = QHBoxLayout()
        self.score1 = QLabel('player 1 score:' + str(self.player1score))
        layout2.addWidget(self.score1)
        self.blankLabel = QLabel('     ')
        layout2.addWidget(self.blankLabel)
        self.score2 = QLabel('player 2 score:' + str(self.player2score))
        layout2.addWidget(self.score2)

        layout3 = QVBoxLayout()
        layout3.addLayout(layout2)
        layout3.addLayout(layout)

        self.setLayout(layout3)

    def getTurn(self):
        if self.resetCounter % 2 == 0:
            return str(self.player1starts())
        else:
            return str(self.player2starts())

    def player1starts(self):
        if self.clickCounter % 2 == 0:
            return 'X'
        else:
            return 'O'

    def player2starts(self):
        if self.clickCounter % 2 == 0:
            return 'O'
        else:
            return 'X'


app = QApplication([])
app.setStyle('Macintosh')

window = TicTacToeWindow()
window.show()

app.exec()










