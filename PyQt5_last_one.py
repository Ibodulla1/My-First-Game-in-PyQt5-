from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QGroupBox, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from random import shuffle
import sys


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.Group_Box = QGroupBox("NUMBERS")
        
        self.QGrid_Layout = QGridLayout()

        self.V_Layout = QVBoxLayout()

        self.H_Layout = QHBoxLayout()

        self.Buttons1 = QPushButton("1")
        self.Buttons2 = QPushButton("2")
        self.Buttons3 = QPushButton("3")
        self.Buttons4 = QPushButton("4")
        self.Buttons5 = QPushButton("5")
        self.Buttons6 = QPushButton("6")
        self.Buttons7 = QPushButton("7")
        self.Buttons8 = QPushButton("8")
        self.Buttons9 = QPushButton("9")
        self.Buttons10 = QPushButton("10")
        self.Buttons11 = QPushButton("11")
        self.Buttons12 = QPushButton("12")
        self.Buttons13 = QPushButton("13")
        self.Buttons14 = QPushButton("14")
        self.Buttons15 = QPushButton("15")
        self.Buttons_ = QPushButton(" ")


        self.Buttons1.clicked.connect(self.BTN1)
        self.Buttons2.clicked.connect(self.BTN2)
        self.Buttons3.clicked.connect(self.BTN3)
        self.Buttons4.clicked.connect(self.BTN4)
        self.Buttons5.clicked.connect(self.BTN5)
        self.Buttons6.clicked.connect(self.BTN6)
        self.Buttons7.clicked.connect(self.BTN7)
        self.Buttons8.clicked.connect(self.BTN8)
        self.Buttons9.clicked.connect(self.BTN9)
        self.Buttons10.clicked.connect(self.BTN10)
        self.Buttons11.clicked.connect(self.BTN11)
        self.Buttons12.clicked.connect(self.BTN12)
        self.Buttons13.clicked.connect(self.BTN13)
        self.Buttons14.clicked.connect(self.BTN14)
        self.Buttons15.clicked.connect(self.BTN15)
        self.Buttons_.clicked.connect(self.BTN16)

        self.Buttons_Lst = [self.Buttons1, self.Buttons2, self.Buttons3, self.Buttons4, self.Buttons5, self.Buttons6, self.Buttons7, self.Buttons8, self.Buttons9, self.Buttons10, self.Buttons11, self.Buttons12, self.Buttons13, self.Buttons14, self.Buttons15, self.Buttons_]
        for i in self.Buttons_Lst:
            i.setDisabled(True)
        self.numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]
        self.numbers_shuffle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]


        self.index = 0


        for i in range(4):
            for j in range(4):
                self.QGrid_Layout.addWidget(self.Buttons_Lst[self.index], i, j)
                self.index += 1

        self.Cancel_Button = QPushButton("CANCEL")
        self.Cancel_Button.clicked.connect(self.close)
        self.Reset_Button = QPushButton("RESTART")
        self.Reset_Button.clicked.connect(self.restart)
        self.Start_Button = QPushButton("START") 
        self.Start_Button.clicked.connect(self.start)

        self.H_Layout.addWidget(self.Cancel_Button)
        self.H_Layout.addWidget(self.Reset_Button)
        self.H_Layout.addWidget(self.Start_Button)       

        self.Group_Box.setLayout(self.QGrid_Layout)

        self.V_Layout.addWidget(self.Group_Box)
        self.V_Layout.addLayout(self.H_Layout)

        self.setLayout(self.V_Layout)


    def UI(self):
        return """
Game {
    background-color: #477eec;
}        

QPushButton {
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 20px Nunito Sans Light;
    min-width: 10em;
    padding: 6px;
    background-color: #477eec;
}  

QGroupBox {
    font: 20px Nunito Sans Light;
    background-color: #477eec;

}

QPushButton::hover {
    background-color: #f7f7f7;
}

QLabel#psuedolabel1 {
    qproperty-alignment: AlignCenter;
    font: bold 20px Nunito Sans Light;
}
        """

    def restart(self):
        for i in self.Buttons_Lst:
            i.setDisabled(True)

        for i in range(len(self.Buttons_Lst)):
            self.Buttons_Lst[i].setText(f"{self.numbers[i]}")

    def start(self):
        for i in self.Buttons_Lst:
            i.setEnabled(True)
        shuffle(self.numbers_shuffle)

        for i in range(len(self.Buttons_Lst)):
            self.Buttons_Lst[i].setText(f"{self.numbers_shuffle[i]}")


    

    def check(self):
        lst_for_check = []
        for i in self.Buttons_Lst:

            if i.text() == ' ':
                    lst_for_check.append(' ')
            else:    
                lst_for_check.append(int(i.text()))        


        if lst_for_check == self.numbers:
             Message_Box = QMessageBox()
             Message_Box.setIcon(QMessageBox.information)
             Message_Box.setText("You are the WINNER")
             Message_Box.setStyleSheet("background-color : green; color:white")
             Message_Box.exec_()



    def BTN1(self):
        if self.Buttons2.text() == ' ':
            hold = self.Buttons1.text()
            self.Buttons1.setText(' ')
            self.Buttons2.setText(hold)

        if self.Buttons5.text() == ' ':
            hold = self.Buttons1.text()
            self.Buttons5.setText(hold)
            self.Buttons1.setText(' ')

        self.check()
    

    def BTN2(self):
        if self.Buttons1.text() == ' ':
            hold = self.Buttons2.text()
            self.Buttons1.setText(hold)
            self.Buttons2.setText(' ')

        if self.Buttons3.text() == ' ':
            hold = self.Buttons2.text() 
            self.Buttons2.setText(' ')
            self.Buttons3.setText(hold)

        if self.Buttons6.text() == ' ':
            hold = self.Buttons2.text()
            self.Buttons6.setText(hold)
            self.Buttons2.setText(' ')

        self.check()


    def BTN3(self):
        if self.Buttons2.text() == ' ':
            hold = self.Buttons3.text()
            self.Buttons2.setText(hold)
            self.Buttons3.setText(' ')

        if self.Buttons4.text() == ' ':
            hold = self.Buttons3.text()
            self.Buttons4.setText(hold)
            self.Buttons3.setText(' ')

        if self.Buttons7.text() == ' ':
            hold = self.Buttons3.text()
            self.Buttons7.setText(hold)
            self.Buttons3.setText(' ')

        self.check()


    def BTN4(self):
        if self.Buttons3.text() == ' ':
            hold = self.Buttons4.text()
            self.Buttons3.setText(hold)
            self.Buttons4.setText(' ')

        if self.Buttons8.text() == ' ':
            hold = self.Buttons4.text()
            self.Buttons8.setText(hold)
            self.Buttons4.setText(' ')

        self.check()


    def BTN5(self):
        if self.Buttons1.text() == ' ':
            hold = self.Buttons5.text()
            self.Buttons1.setText(hold)
            self.Buttons5.setText(' ')

        if self.Buttons6.text() == ' ':
            hold = self.Buttons5.text()
            self.Buttons6.setText(hold)
            self.Buttons5.setText(' ')

        if self.Buttons9.text() == ' ':
            hold = self.Buttons5.text()
            self.Buttons5.setText(' ')
            self.Buttons9.setText(hold)

        self.check()


    def BTN6(self):
        if self.Buttons5.text() == ' ':
            hold = self.Buttons6.text()
            self.Buttons6.setText(' ')
            self.Buttons5.setText(hold)

        if self.Buttons2.text() == ' ':
            hold = self.Buttons6.text()
            self.Buttons2.setText(hold)
            self.Buttons6.setText(' ')

        if self.Buttons7.text() == ' ':
            hold = self.Buttons6.text()
            self.Buttons7.setText(hold)
            self.Buttons6.setText(' ')

        if self.Buttons10.text() == ' ':
            hold = self.Buttons6.text()
            self.Buttons10.setText(hold)
            self.Buttons6.setText(' ')

        self.check()



    def BTN7(self):
        if self.Buttons6.text() == ' ':
            hold = self.Buttons7.text()
            self.Buttons7.setText(' ')
            self.Buttons6.setText(hold)

        if self.Buttons3.text() == ' ':
            hold = self.Buttons7.text()
            self.Buttons3.setText(hold)
            self.Buttons7.setText(' ')

        if self.Buttons8.text() == ' ':
            hold = self.Buttons7.text()
            self.Buttons8.setText(hold)
            self.Buttons7.setText(' ')

        if self.Buttons11.text() == ' ':
            hold = self.Buttons7.text()
            self.Buttons11.setText(hold)
            self.Buttons7.setText(' ')

        self.check()





    def BTN8(self):
        if self.Buttons7.text() == ' ':
            hold = self.Buttons8.text()
            self.Buttons8.setText(' ')
            self.Buttons7.setText(hold)

        if self.Buttons12.text() == ' ':
            hold = self.Buttons8.text()
            self.Buttons12.setText(hold)
            self.Buttons8.setText(' ')

        if self.Buttons4.text() == ' ':
            hold = self.Buttons8.text()
            self.Buttons4.setText(hold)
            self.Buttons8.setText(' ')

        self.check()



    def BTN9(self):
        if self.Buttons5.text() == ' ':
            hold = self.Buttons9.text()
            self.Buttons9.setText(' ')
            self.Buttons5.setText(hold)

        if self.Buttons10.text() == ' ':
            hold = self.Buttons9.text()
            self.Buttons10.setText(hold)
            self.Buttons9.setText(' ')

        if self.Buttons13.text() == ' ':
            hold = self.Buttons9.text()
            self.Buttons13.setText(hold)
            self.Buttons9.setText(' ')

        self.check()



    def BTN10(self):
        if self.Buttons9.text() == ' ':
            hold = self.Buttons10.text()
            self.Buttons10.setText(' ')
            self.Buttons9.setText(hold)

        if self.Buttons6.text() == ' ':
            hold = self.Buttons10.text()
            self.Buttons6.setText(hold)
            self.Buttons10.setText(' ')

        if self.Buttons11.text() == ' ':
            hold = self.Buttons10.text()
            self.Buttons11.setText(hold)
            self.Buttons10.setText(' ')

        if self.Buttons14.text() == ' ':
            hold = self.Buttons10.text()
            self.Buttons14.setText(hold)
            self.Buttons10.setText(' ')

        self.check()




    def BTN11(self):
        if self.Buttons10.text() == ' ':
            hold = self.Buttons11.text()
            self.Buttons11.setText(' ')
            self.Buttons10.setText(hold)

        if self.Buttons7.text() == ' ':
            hold = self.Buttons11.text()
            self.Buttons7.setText(hold)
            self.Buttons11.setText(' ')

        if self.Buttons12.text() == ' ':
            hold = self.Buttons11.text()
            self.Buttons12.setText(hold)
            self.Buttons11.setText(' ')

        if self.Buttons15.text() == ' ':
            hold = self.Buttons11.text()
            self.Buttons15.setText(hold)
            self.Buttons11.setText(' ')

        self.check()

            

    def BTN12(self):
        if self.Buttons11.text() == ' ':
            hold = self.Buttons12.text()
            self.Buttons12.setText(' ')
            self.Buttons11.setText(hold)

        if self.Buttons8.text() == ' ':
            hold = self.Buttons12.text()
            self.Buttons8.setText(hold)
            self.Buttons12.setText(' ')

        if self.Buttons_.text() == ' ':
            hold = self.Buttons12.text()
            self.Buttons_.setText(hold)
            self.Buttons12.setText(' ') 

        self.check()



      

    def BTN13(self):
        if self.Buttons9.text() == ' ':
            hold = self.Buttons13.text()
            self.Buttons13.setText(' ')
            self.Buttons9.setText(hold)

        if self.Buttons14.text() == ' ':
            hold = self.Buttons13.text()
            self.Buttons14.setText(hold)
            self.Buttons13.setText(' ')

        self.check()



    def BTN14(self):
        if self.Buttons13.text() == ' ':
            hold = self.Buttons14.text()
            self.Buttons14.setText(' ')
            self.Buttons13.setText(hold)

        if self.Buttons10.text() == ' ':
            hold = self.Buttons14.text()
            self.Buttons10.setText(hold)
            self.Buttons14.setText(' ')

        if self.Buttons15.text() == ' ':
            hold = self.Buttons14.text()
            self.Buttons15.setText(hold)
            self.Buttons14.setText(' ')

        self.check()



    def BTN15(self):
        if self.Buttons14.text() == ' ':
            hold = self.Buttons15.text()
            self.Buttons15.setText(' ')
            self.Buttons14.setText(hold)

        if self.Buttons11.text() == ' ':
            hold = self.Buttons15.text()
            self.Buttons11.setText(hold)
            self.Buttons15.setText(' ')

        if self.Buttons_.text() == ' ':
            hold = self.Buttons15.text()
            self.Buttons_.setText(hold)
            self.Buttons15.setText(' ')

        self.check()



    def BTN16(self):
        if self.Buttons_.text() != ' ':

            if self.Buttons15.text() == ' ':
                hold = self.Buttons_.text()
                self.Buttons15.setText(hold)
                self.Buttons_.setText(' ')

            if self.Buttons12.text() == ' ':
                hold = self.Buttons_.text()
                self.Buttons12.setText(hold)
                self.Buttons_.setText(' ')

            self.check()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    app.setStyleSheet(game.UI())
    game.setWindowTitle("GAME")
    game.setWindowIcon(QIcon("C:\\Users\\Ibodulla Jumaniyozov\\Downloads\\gameIcon.png"))
    game.setGeometry(500,300,500,500)
    game.show()
    app.exec_()