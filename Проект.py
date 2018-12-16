import sys, datetime
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QMessageBox, QApplication, QLabel, QSpinBox, QPushButton, QMainWindow, QRadioButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDate, Qt, pyqtSignal, QObject
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Проект2.ui',self)
        
        self.knife = False
        self.symbol = False
        self.laibrarycan = True
        self.y = 650
        self.stairs = False
        self.antipoision = False
        self.n = 1        
        
        self.start()              
    
    def start(self):
        self.label.setText("Вы очнулись в слабоосвещенной комнате. Вы сидите в самом углу на холодном каменном полу. Вы\nрешаете осмотреться. Слева от себя вы видите металлическую дверь. Ваш взгляд скользит по\nвлажным стенам, в темноте плохо видно, но вы замечаете какие-то очертания на потолке\nв противоположном углу. Обстановка очень угнетающая. То что вы хотите выбраться от сюда не\nвызывает сомнения. Но для начала попытайтесь вспомнить, как вас зовут\n\n\nВас зовут:")
        
        self.lineEdit.move(65, 250)        
        
        self.pushButton.clicked.connect(self.FirstRoom)
        self.pushButton_2.clicked.connect(self.FirstRoom)
        self.pushButton_3.clicked.connect(self.FirstRoom)
    
    def FirstRoom(self):
        self.lineEdit.move(120, 700)  
        
        self.label.setText("Вы решаете проверить...")
        self.pushButton.setText('...дверь')
        self.pushButton_2.setText('...стены')
        self.pushButton_3.setText('...очертания на потолке')
        
        self.pushButton.clicked.connect(self.metallDoor)
        self.pushButton_3.clicked.connect(self.strangeShapes)
        self.pushButton_2.clicked.connect(self.Wall)
        
        self.spinBox.move(25, 650)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(9)
        
        self.spinBox_2.move(75, 650)
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(9)
        
        self.spinBox_3.move(125, 650)
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(9)
        
        self.spinBox_4.move(175, 650)
        self.spinBox_4.setAlignment(Qt.AlignCenter)
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(9)
        
        self.lcdNumber.move(50, 600)
        self.y = 600
    
    def metallDoor(self):
        self.label.setText("Вы подошли к двери. Она оказалась больше, чем вы ожидали, и она вся была покрыта мхом.\nЭто оказалась вакуумная дверь. Дверь достаточно хороша, но что же делать дальше?")
        
        self.pushButton.setText('Вернуться обратно')
        self.pushButton_2.setText('Попробовать открыть')
        self.pushButton_3.setText('Отчистить дверь')
        
        self.pushButton.clicked.connect(self.FirstRoom)
        self.pushButton_2.clicked.connect(self.tryOpen)
        self.pushButton_3.clicked.connect(self.tearOffMoss)
    
    def strangeShapes(self):
        if not self.stairs:
            self.label.setText("Вы решили узнать, что это за странные очертания на потолке. Когда вы подошли к противополож-\nному углу, то вы увидели, что это был обычный люк. Но он был очень высоко, вы не сможете до\nнего достать как бы вам не хотелось.")
            
            self.pushButton.setText('Вернуться обратно')
            self.pushButton_2.setText('Вернуться обратно')
            self.pushButton_3.setText('Вернуться обратно')
            
            self.pushButton.clicked.connect(self.FirstRoom)
            self.pushButton_2.clicked.connect(self.FirstRoom)
            self.pushButton_3.clicked.connect(self.FirstRoom)
        else:
            self.label.setText("Вы начали взбираться по лестнице. К счастью, люк не был закрыт. Открыв его, вы увидели\nмаленькую комнатку. Она была настолько маленькой, что вы не можете в нее забраться. Но на\nстене вы увидели экранчик с цифрами на нем.")
            
            self.lcdNumber.move(50, 300)
            self.lcdNumber.display(8576)
            
            self.pushButton.setText('Вернуться обратно')
            self.pushButton_2.setText('Вернуться обратно')
            self.pushButton_3.setText('Вернуться обратно')
            
            self.pushButton.clicked.connect(self.FirstRoom)
            self.pushButton_2.clicked.connect(self.FirstRoom)
            self.pushButton_3.clicked.connect(self.FirstRoom)
        
    def Wall(self):
        self.label.setText("Вы решили проверить стену. Она тоже вся была покрыта мхом. Вы решили осмотреть стену\nвнимательней. И ваше чутье вас не подвело. Осмотрев стыки более внимательно, вы увидели,\nчто некоторые каменные блоки стоят неплотно. Вы попробовали потянуть за один из таких\nблоков, и из стены вышла огромная плита. За этой плитой был проход, а за ним тусклое свечение.")
        
        self.pushButton.setText('Вернуться обратно')
        self.pushButton_2.setText('Зайти в проход')
        self.pushButton_3.setText('Вернуться обратно')
        
        self.pushButton.clicked.connect(self.FirstRoom)
        self.pushButton_3.clicked.connect(self.FirstRoom)
        if self.laibrarycan:
            self.pushButton_2.clicked.connect(self.Passage)
    
    def tryOpen(self):
        self.label.setText("Вы решили потянуть за ручку. Но дверь либо была очень прочная, либо ее заклинило. В конце\nконцов вы оставили эту затею и решаете снова осмотреть дверь.")
        
        self.pushButton.setText('Осмотреть дверь')
        self.pushButton_2.setText('Осмотреть дверь')
        self.pushButton_3.setText('Осмотреть дверь')
        
        self.pushButton.clicked.connect(self.metallDoor)
        self.pushButton_2.clicked.connect(self.metallDoor)
        self.pushButton_3.clicked.connect(self.metallDoor)
    
    def tearOffMoss(self):
        self.label.setText("Этого мха было так много, но вы наконец-то смогли очистить от него дверь. Но пока вы это\nделали, возможно, прошел целый час. Хотя, вы уже не знаете, сколько времени прошло.\nВозможно прошло всего пол часа, а возможно уже прошел целый день. После того, как вы убрали\nвесь мох, у вас сильно ныли руки. Можно было бы предположить, что они болят от тяжелой\nработы, но, когда вы осмотрели их внимательно, вы заметили, что они покрылись сыпью.\n\n(Чешется, неправда ли? Я польщена, это моя специальная разработка. Этот мох выделяет сок\nядовитый для человека, но он действует медленно.)\n\nЧательно осмотрев руки, вы снова решаете осмотреть дверь. В центре двери вы обнаруживаете\nкодовый замок. Но этот мох растет слишком быстро. Дверь начала снова покрываться мхом.")
        
        self.spinBox.move(25, 350)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(9)
        
        self.spinBox_2.move(75, 350)
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(9)
        
        self.spinBox_3.move(125, 350)
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(9)
        
        self.spinBox_4.move(175, 350)
        self.spinBox_4.setAlignment(Qt.AlignCenter)
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(9)        
        
        self.pushButton.setText('Ввести пароль')
        self.pushButton_2.setText('Вернуться обратно')
        self.pushButton_3.setText('Вернуться обратно')
        
        self.pushButton.clicked.connect(self.enterPassword)
        self.pushButton_2.clicked.connect(self.FirstRoom)
        self.pushButton_3.clicked.connect(self.FirstRoom)
        
        self.lcdNumber.move(50, 600)
    
    def Passage(self):
        self.label.setText("Вы начинаете протискиваться в проход, но где-то после середины он начал сужаться.\n\n (А вы меньше, чем я предполагала.) \n\n Наконец вы смогли протиснуться. Вы ввалилсь из прохода в просторную комату. Обставлена\nкомната как библиотека или кабинет. Стены были увешаны картинами, а в углу стоял стол с\nлампой на нем. Но это не единственное, что было в этой комнате. В ней было очень много книг.\nОни были везде: на столе, у стен стояли два огромных шкафа, польностью заполненных книгами,\nдаже на полу были стопки книг.")
        
        self.pushButton.setText("Далее")
        self.pushButton_2.setText('Далее')
        self.pushButton_3.setText('Далее')
        
        self.pushButton_2.clicked.connect(self.libruary)
        self.pushButton.clicked.connect(self.libruary)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def libruary(self):
        self.label.setText("Вы решили исследовать комнату, но с чего бы начать?")
        
        self.y = 650
        
        self.pushButton.setText('Начать с книг')
        self.pushButton_2.setText('Осмотреть стол')
        self.pushButton_3.setText('Присмотреться к картинам')
        
        self.pushButton.clicked.connect(self.checkBooks)
        self.pushButton_2.clicked.connect(self.tableCheck)
        self.pushButton_3.clicked.connect(self.checkPictures)
        
    def tableCheck(self):
        self.label.setText("Подойдя ближе к столу, вы поняли, что на нем лежит пара листков и книги, но из-за большой\nвлажности надписи на них превратились в разплывчатые, серые линии. Но у стола были ящики,\nтолько там могли остаться нетронутые записи.\nВ большинстве ящиков ничего не было, но в одном ящике вы нашли книжку с золотой эмблемой\nна обложке. Пролистав несколько страниц, вы увидели, что все записи имеют дату, поэтому\nможно было предположить, что это был дневник. Все страницы были запачканы всеразличными\nжидкостями. Ближе к концу тетради стали появляться бардовые капли, а последняя страница\nполностью была залита этой бардовой жидкостью. Из-за этих пятен почти ничего нельзя было\nпрочитать. Что делать дальше?")
        
        self.lineEdit.move(65, 650)
        
        self.pushButton.setText('Вернуться к осмотру комнаты')
        self.pushButton_2.setText('Попытаться прочитать записи')
        self.pushButton_3.setText('Рассмотреть эмблему')
        
        self.pushButton.clicked.connect(self.libruary)
        self.pushButton_2.clicked.connect(self.checkText)
        self.pushButton_3.clicked.connect(self.checkSymbol)
    
    def checkSymbol(self):
        self.label.setText("Эмблема была странной. Это был круг разделенный на четыре части. Она была выпуклой,\nпозолоченной и обложка с эмблемой была достаточно толстой.")
        
        self.spinBox.move(25, 650)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(9)
        
        self.spinBox_2.move(75, 650)
        self.spinBox_2.setAlignment(Qt.AlignCenter)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(9)
        
        self.spinBox_3.move(125, 650)
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(9)
        
        self.spinBox_4.move(175, 650)
        self.spinBox_4.setAlignment(Qt.AlignCenter)
        self.spinBox_4.setMinimum(0)
        self.spinBox_4.setMaximum(9)        
        
        self.pushButton.setText('Пытаться разобрать записи')
        self.pushButton_2.setText('Попытаться оторвать эмблему')
        self.pushButton_3.setText('Вернуться к осмотру комнаты')
        
        self.pushButton.clicked.connect(self.checkText)
        self.pushButton_2.clicked.connect(self.Symbol)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def checkText(self):
        self.label.setText("Я не могу поверить... предатель... наши разработки... все пропало. Зачем я ему поверила?...\nубить меня... А мы ведь раньше были напарниками...\n*следующая страница*\nИдея! Я построю ему ловушку. Это будет... ГЕНИАЛЬНО!! Он никогда не сможет выбраться от туда...\n*следующая страница*\nЕму удалось... Марк, если ты это читаешь, то знай... Зря ты покусился на мою жизнь. Теперь ты\nсгинешь здесь!*конец записей*\n\nИз-за пятен вам больше ничего не удается прочитать.\n\n(Вау, ты нашел мой дневник. Я удивлена. Но тебе это не поможет, ты умрешь раньше.)")
        
        self.pushButton.setText('Вернуться к осмотру комнаты')
        self.pushButton_2.setText('Рассмотреть эмблему')
        self.pushButton_3.setText('Вернуться к осмотру комнаты')
        
        self.pushButton.clicked.connect(self.libruary)
        self.pushButton_2.clicked.connect(self.Symbol)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def Symbol(self):
        self.y = 650
        if not self.knife:
            self.label.setText("Сама эмблема была металлической, но когда вы ее попытались оторвать,\nничего не получилось. Возможно эта эмблема вам бы и пригодилась, но тогда вам пришлось бы\nразрезать обложку.")
        else:
            self.label.setText("Сама эмблема была металлической, но когда вы ее попытались оторвать,\nничего не получилось. Возможно эта эмблема вам бы и пригодилась, но тогда вам пришлось бы\nразрезать обложку. К счастью у вас был нож, и вы разрезали обложку. Под обложкой оказалас\nметаллическая пластина с отверстиями в ней. Она была соединенна с эмблемой. Вы положили эту\nпластину к себе в карман.")
        
            self.symbol = True
        
        self.pushButton.setText('Вернуться к осмотру комнаты')
        self.pushButton_2.setText('Вернуться к осмотру комнаты')
        self.pushButton_3.setText('Вернуться к осмотру комнаты')
        
        self.pushButton.clicked.connect(self.libruary)
        self.pushButton_2.clicked.connect(self.libruary)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def checkBooks(self):
        self.label.setText("Вы начали осмотр книг. Это были в основном научные книги. Вы уже хотели было встать, но\nслучайно уронили стоящую стопку книг. Они все рассыпались по полу, вдруг раздался\nметаллический звук. Вы принялись искать этот металлический предмет, вы поднимали книгу одну\nза другой, и вот под одной из них лежал нож для вскрытия писем. Вы подняли его. Больше книги\nвам не были интересны. Что делать дальше?")
        
        self.knife = True
        
        self.pushButton.setText('Вернуться к столу')
        self.pushButton_2.setText('Вернуться к осмотру комнаты')
        self.pushButton_3.setText('Начать осматривать картины')
        
        self.pushButton.clicked.connect(self.tableCheck)
        self.pushButton_2.clicked.connect(self.libruary)
        self.pushButton_3.clicked.connect(self.checkPictures)
    
    def checkPictures(self):
        self.label.setText("Подойдя к картинам, вы не увидели ничего необычного во всех картинах кроме одной. На стене\nбыла елевидная стрелка, указывающая на эту картину. Что вы предпримете?")
        
        self.spinBox.move(25, 650)
        self.spinBox_2.move(75, 650)
        self.spinBox_3.move(125, 650)
        self.spinBox_4.move(175, 650)        
        
        self.pushButton.setText('Осмотреть полотно')
        self.pushButton_2.setText('Снять картину')
        self.pushButton_3.setText('Вернуться к осмотру комнаты')
        
        self.pushButton.clicked.connect(self.checkImage)
        self.pushButton_2.clicked.connect(self.removePicture)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def checkImage(self):
        self.label.setText("Полотно было очень странным. Точнее оно не было \"проффесиональным\". Но в нем не было\nничего необычного.")
        
        self.knife = False

        self.pushButton.setText('Вернуться к осмотру комнаты')
        self.pushButton_2.setText('Снять картину')
        self.pushButton_3.setText('Вернуться к осмотру комнаты')
        
        self.pushButton.clicked.connect(self.libruary)
        self.pushButton_2.clicked.connect(self.removePicture)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def removePicture(self):
        self.label.setText("Вы сняли полотно и под ним оказался трехцветный флаг. И слева от каждого цвета были цифры.\nСверху вниз были написаны цифры 1, 2, 3. Но также там была кнопка.")
        
        self.y = 300
        
        self.spinBox.move(25, 650)
        self.spinBox_2.move(75, 650)
        self.spinBox_3.move(125, 650)
        self.spinBox_4.move(175, 650)
        
        self.pushButton.setText('Вернуться к осмотру комнаты')
        self.pushButton_2.setText('Нажать на кнопку')
        self.pushButton_3.setText('Вернуться в осмотру комнаты')
        
        self.pushButton.clicked.connect(self.libruary)
        self.pushButton_2.clicked.connect(self.buttonPressed)
        self.pushButton_3.clicked.connect(self.libruary)
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()
 
    def drawFlag(self,qp):
        qp.setBrush(QColor(0, 0, 0))
        qp.drawRect(30, self.y, 120, 30)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawRect(30, self.y+30, 120, 30)
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(30, self.y+60, 120, 30)
    
    def buttonPressed(self):
        if self.knife:
            self.label.setText("Вы решили нажать кнопку. Она оказалась размером с вашу ладонь. Но не смотря на то, что она\nбыла каменная, нажалась она очень легко.\nТемно. Пол дрожит. Нет. Не только пол. Дрожит все. Скрежет камня по камню.\nСвет снова включился. Вы огляделись, в стене открылся проход.\n\n(Молодец, ты его выпустил.)\n\nНо почему скрежет все еще продолжается? Нет это не скрежет. Это ВИЗГ. Вы оборачиваетесь в\nсторону открывшегося прохода. Как раз вовремя. Вы увидели сидящее там существо. Это был\nчеловек, но он был какой-то... изуродованный. Он стоял сразу на руках и ногах, как ящерица. А\nна лице был только один глаз и рот. Рот был просто огромен. Он занимал, наверное, больше\nполовины оставшегося лица. Скорее всего он не сможет быстро передвигаться в таком положении.\nИ оно прыгнуло на вас. К счастью, у вас был нож. С размаху вы воткнули его в это чудовище и\nпринялись бежать. Вы залезли в проход и принялись протискиваться вперед.\n\n(Жаль. Оно не сможет пролезть в проход, но теперь вы не сможете попасть в библиотеку)\n\nВы вышли в ту комнату, где вы очнулись в самом начале. Посмотрев, вы увидели, что под люком\nиз стены появилась каменная лестница.")
            
            self.stairs = True
            
            self.pushButton.setText('Далее')
            self.pushButton_2.setText('Далее')
            self.pushButton_3.setText('Далее')
            
            self.pushButton.clicked.connect(self.FirstRoom)
            self.pushButton_2.clicked.connect(self.FirstRoom)
            self.pushButton_3.clicked.connect(self.FirstRoom)
        else:
            self.label.setText("Вы решили нажать книопку. Она оказалась размером с вашу ладонь. Но не смотря на то, что она\nбыла каменная, нажалась она очень легко.\nТемно. Пол дрожит. Нет. Не только пол. Дрожит все. Скрежет камня по камню.\nСвет снова включился. Вы огляделись, в стене открылся проход.\n\n (Молодец, ты его выпустил.)\n\n Но почему скрежет все еще продолжается? Нет это не скрежет. Это ВИЗГ. Вы оборачиваетесь в\nсторону открывшегося прохода. Как раз вовремя. Вы увидели сидящее там существо. Это был\nчеловек, но он был какой-то... изуродованный. Он стоял сразу на руках и ногах, как ящерица. А\nна лице был только один глаз и рот. Рот был просто огромен. Он занимал, наверное, больше\nполовины оставшегося лица. Скорее всего он не сможет быстро передвигаться в таком положении.\nИ оно прыгнуло на вас. Вы не смогли защититься, поэтому оно повалило вас и содрало кожу с\nвашего лица. Из-за его веса вы не можете подняться. Еще долго оно раздирало вас.\nНачать игру заново?")
            
            self.pushButton.setText('Да')
            self.pushButton_2.setText('Да')
            self.pushButton_3.setText('Да')
            
            self.pushButton.clicked.connect(self.start)
            self.pushButton_2.clicked.connect(self.start)
            self.pushButton_3.clicked.connect(self.start)
    
    def enterPassword(self):
        self.pushButton.setText('Далее')
        self.pushButton_2.setText('Далее')
        self.pushButton_3.setText('Далее')
        
        if self.spinBox.value() == 8 and self.spinBox_2.value() == 5 and self.spinBox_3.value() == 7 and self.spinBox_4.value() == 6:
            self.label.setText("Пароль верен.")
            
            self.pushButton.clicked.connect(self.SecondRoom)
            self.pushButton_2.clicked.connect(self.SecondRoom)
            self.pushButton_3.clicked.connect(self.SecondRoom)             
        else:
            self.label.setText("Пароль неверен.")
            
            self.pushButton.clicked.connect(self.FirstRoom)
            self.pushButton_2.clicked.connect(self.FirstRoom)
            self.pushButton_3.clicked.connect(self.FirstRoom)
        
    def SecondRoom(self):
        self.label.setText("Дверь открылась и вы вошли в комнату. Напротив вас расположена дверь, а справа от вас\nрасположен проход. Что делать дальше?")
        
        self.y = 650
        self.lineEdit.move(65, 650)
        
        self.pushButton.setText('Вернуться обратно')
        self.pushButton_2.setText('Подойти к двери')
        self.pushButton_3.setText('Подойти к проходу')
        
        self.pushButton.clicked.connect(self.FirstRoom)
        self.pushButton_2.clicked.connect(self.door1)
        self.pushButton_3.clicked.connect(self.walkWay)
    
    def walkWay(self):
        self.label.setText("Вы решили подойти к проходу. Как только вы это сделали, вы услышали чей-то слабый голос:\n-Помогите.\n-Кто это?\n-А ты кто?\n-Я? Я... Я {}\n-А я Марк.Спаси меня!Пожалуйста... Мне плохо\n\nЧто вы будете делать?".format(self.lineEdit.text()))
        
        self.spinBox.move(25, 650)
        self.spinBox_2.move(75, 650)
        self.spinBox_3.move(125, 650)
        self.spinBox_4.move(175, 650)        
        
        self.pushButton.setText('Помочь')
        self.pushButton_2.setText('Вернуться обратно')
        self.pushButton_3.setText('Подойти к двери')
        
        self.pushButton.clicked.connect(self.helpMark)
        self.pushButton_2.clicked.connect(self.SecondRoom)
        self.pushButton_3.clicked.connect(self.door1)
    
    def helpMark(self):
        self.label.setText("-Я помогу тебе. Что мне сделать?\n-Около прохода должен лежать мой рюкзак. Там лежит зажигалка. Найди ее и иди ко мне.\n-Хорошо.\nВы нашли портфель у самого входа. В нем не было ничего полезного кроме зажигалки. Вы взяли\nее и пошли в центр комнаты. Вскоре вы нашли человека лежащего на боку, спиной к вам. Но\nкогда вы повернули его лицом к себе, вы поняли, что внутри него ничего нет. Кто-то вытащил все\nвнутренности из него, разорвав живот и лицо. Обернувшись, вы бросились к выходу, но вам его\nзаслонило что-то непонятное. Оно бросилось на вас.\n\n(Нравится моя колекция?)\n\nВы умерли.\n\nНачать заново?")
        
        self.pushButton.setText('Да')
        self.pushButton_2.setText('Да')
        self.pushButton_3.setText('Да')
        
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.start)
        self.pushButton_3.clicked.connect(self.start)
    
    def door1(self):
        self.label.setText("Вы подошли к двери. На ней была нацарапана цифра 1, и под ней был список кнопок. Стерев с\nних пыль, вы увидели, что это был список цветов.")
        
        self.radioButton.move(25, 250)
        self.radioButton_2.move(25, 275)
        self.radioButton_3.move(25, 300)
        self.radioButton_4.move(25, 325)
        self.radioButton_5.move(25, 350)
        self.radioButton_6.move(25, 375)
        
        self.pushButton.setText('Ввести цвет')
        self.pushButton_2.setText('Вернуться обратно')
        self.pushButton_3.setText('Вернуться обратно')
        
        self.pushButton.clicked.connect(self.colorCheck1)
        self.pushButton_2.clicked.connect(self.SecondRoom)
        self.pushButton_3.clicked.connect(self.SecondRoom)
    
    def colorCheck1(self):
        if self.radioButton.isChecked():
            self.label.setText("Цвет был выбран правильно.")
            
            self.radioButton.move(25, 650)
            self.radioButton_2.move(25, 650)
            self.radioButton_3.move(25, 650)
            self.radioButton_4.move(25, 650)
            self.radioButton_5.move(25, 650)
            self.radioButton_6.move(25, 650)            
            
            self.pushButton.setText('Дальше')
            self.pushButton_2.setText('Дальше')
            self.pushButton_3.setText('Дальше')
            
            self.pushButton.clicked.connect(self.door2)
            self.pushButton_2.clicked.connect(self.door2)
            self.pushButton_3.clicked.connect(self.door2)
        else:
            self.label.setText("Цвет был выбран неправильно.")
            
            self.radioButton.move(25, 650)
            self.radioButton_2.move(25, 650)
            self.radioButton_3.move(25, 650)
            self.radioButton_4.move(25, 650)
            self.radioButton_5.move(25, 650)
            self.radioButton_6.move(25, 650)             
            
            self.pushButton.setText('Вернуться обратно')
            self.pushButton_2.setText('Вернуться обратно')
            self.pushButton_3.setText('Вернуться обратно')
            
            self.pushButton.clicked.connect(self.door1)
            self.pushButton_2.clicked.connect(self.door1)
            self.pushButton_3.clicked.connect(self.door1)
    
    def door2(self):
        self.label.setText("Вы открыли дверь, и через пару метров за ней была точно такая же только, на ней была\nнацарапана цифра 3")
        
        self.radioButton.move(25, 250)
        self.radioButton_2.move(25, 275)
        self.radioButton_3.move(25, 300)
        self.radioButton_4.move(25, 325)
        self.radioButton_5.move(25, 350)
        self.radioButton_6.move(25, 375)
        
        self.pushButton.setText('Ввести цвет')
        self.pushButton_2.setText('Вернуться обратно')
        self.pushButton_3.setText('Вернуться обратно')
        
        self.pushButton.clicked.connect(self.colorCheck2)
        self.pushButton_2.clicked.connect(self.SecondRoom)
        self.pushButton_3.clicked.connect(self.SecondRoom)

    def colorCheck2(self):
        if self.radioButton_5.isChecked():
            self.label.setText("Цвет был выбран правильно.")
            
            self.radioButton.move(25, 650)
            self.radioButton_2.move(25, 650)
            self.radioButton_3.move(25, 650)
            self.radioButton_4.move(25, 650)
            self.radioButton_5.move(25, 650)
            self.radioButton_6.move(25, 650)            
            
            self.pushButton.setText('Дальше')
            self.pushButton_2.setText('Дальше')
            self.pushButton_3.setText('Дальше')
            
            self.pushButton.clicked.connect(self.door3)
            self.pushButton_2.clicked.connect(self.door3)
            self.pushButton_3.clicked.connect(self.door3)
        else:
            self.label.setText("Цвет был выбран неправильно.")
            
            self.radioButton.move(25, 650)
            self.radioButton_2.move(25, 650)
            self.radioButton_3.move(25, 650)
            self.radioButton_4.move(25, 650)
            self.radioButton_5.move(25, 650)
            self.radioButton_6.move(25, 650)             
            
            self.pushButton.setText('Вернуться обратно')
            self.pushButton_2.setText('Вернуться обратно')
            self.pushButton_3.setText('Вернуться обратно')
            
            self.pushButton.clicked.connect(self.door2)
            self.pushButton_2.clicked.connect(self.door2)
            self.pushButton_3.clicked.connect(self.door2)
    
    def door3(self):
        self.label.setText("Вы открыли дверь, и через пару метров за ней была точно такая же только на ней была\nнацарапана цифра 2")
        
        self.radioButton.move(25, 250)
        self.radioButton_2.move(25, 275)
        self.radioButton_3.move(25, 300)
        self.radioButton_4.move(25, 325)
        self.radioButton_5.move(25, 350)
        self.radioButton_6.move(25, 375)
        
        self.pushButton.setText('Ввести цвет')
        self.pushButton_2.setText('Вернуться обратно')
        self.pushButton_3.setText('Вернуться обратно')
        
        self.pushButton.clicked.connect(self.colorCheck3)
        self.pushButton_2.clicked.connect(self.SecondRoom)
        self.pushButton_3.clicked.connect(self.SecondRoom) 
        
    def colorCheck3(self):
        if self.radioButton_4.isChecked():
            self.label.setText("Цвет был выбран правильно.")
            
            self.radioButton.move(25, 650)
            self.radioButton_2.move(25, 650)
            self.radioButton_3.move(25, 650)
            self.radioButton_4.move(25, 650)
            self.radioButton_5.move(25, 650)
            self.radioButton_6.move(25, 650)            
            
            self.pushButton.setText('Дальше')
            self.pushButton_2.setText('Дальше')
            self.pushButton_3.setText('Дальше')
            
            self.pushButton.clicked.connect(self.ThirdRoom)
            self.pushButton_2.clicked.connect(self.ThirdRoom)
            self.pushButton_3.clicked.connect(self.ThirdRoom)
        else:
            self.label.setText("Цвет был выбран неправильно.")
            
            self.radioButton.move(25, 650)
            self.radioButton_2.move(25, 650)
            self.radioButton_3.move(25, 650)
            self.radioButton_4.move(25, 650)
            self.radioButton_5.move(25, 650)
            self.radioButton_6.move(25, 650)             
            
            self.pushButton.setText('Вернуться обратно')
            self.pushButton_2.setText('Вернуться обратно')
            self.pushButton_3.setText('Вернуться обратно')
            
            self.pushButton.clicked.connect(self.door3)
            self.pushButton_2.clicked.connect(self.door3)
            self.pushButton_3.clicked.connect(self.door3)
    
    def ThirdRoom(self):
        self.label.setText("Наконец-то вы вышли из этого длинного коридора в комнату. Она была завалена обломками\nмебели. Но на противополовной стене висела картина. Когда вы подошли ближе, разгребая груды\nобломков, вы увидели, что это была не картина. Это была фотография. На ней стояло двое\nмужчин, они оба были в лабораторных халатах. Один был меньше другого, и он счастливо улыбался. А лицо второго было прожжено и в этом месте стекло было треснуто. Это все, конечно, интересно, но нужно поскорее выбираться. Что делать дальше?")
        
        self.pushButton.setText('Снять фотографию')
        self.pushButton_2.setText('Посмотреть обломки')
        self.pushButton_3.setText('Вернуться обратно')
        
        self.pushButton.clicked.connect(self.checkFoto)
        self.pushButton_2.clicked.connect(self.checkTrash)
        self.pushButton_3.clicked.connect(self.SecondRoom)
    
    def checkFoto(self):
        if self.symbol and not self.antipoision:
            self.label.setText("Как только вы дотронулись до рамки, ваши руки пронзило острой болью. Посмотрев на них, вы увидели, что запястья покрылись коркой и начали кровоточить, а вся остальная рука покрылась сыпью. Вы вспомнили про яд. Превозмагая боль вы сняли картинку, при этом корка на пальцах треснула, и на пол начала капать кровь. Под картинкой вы обнаружили отверстие в форме круга разделенного на четыре части. Вы вспомнили пластину в вашем кармане. В начали вынимать из кармана пластину. Но вдруг все потемнело. Вы почувствовали, что начинаете падать.\n\n(Наконец-то яд подействовал, а то я уже заждалась.)\n\nВы умерли раньше, чем упали на пол.\n\nНачать игру заново?")
            
            self.pushButton.setText('Да')
            self.pushButton_2.setText('Да')
            self.pushButton_3.setText('Да')
            
            self.pushButton.clicked.connect(self.start)
            self.pushButton_2.clicked.connect(self.start)
            self.pushButton_3.clicked.connect(self.start)
        elif not self.symbol and not self.antipoision:
            self.label.setText("Как только вы дотронулись до рамки, ваши руки пронзило острой болью. Посмотрев на них, вы увидели, что запястья покрылись коркой и начали кровоточить, а вся остальная рука покрылась сыпью. Вы вспомнили про яд. Превозмагая боль вы сняли картинку, при этом корка на пальцах треснула, и на пол начала капать кровь. Под картинкой вы обнаружили отверстие в форме круга разделенного на четыре части. Вы вспомнили эмблему на дневнике. Значит она все таки была нужна. Вы уже собирались возвращаться, но вдруг все потемнело. Вы почувствовали, что начинаете падать.\n\n(Наконец-то яд подействовал, а то я уже заждалась.)\n\nВы умерли раньше, чем упали на пол.\n\nНачать игру заново?")
            
            self.pushButton.setText('Да')
            self.pushButton_2.setText('Да')
            self.pushButton_3.setText('Да')
            
            self.pushButton.clicked.connect(self.start)
            self.pushButton_2.clicked.connect(self.start)
            self.pushButton_3.clicked.connect(self.start)
        elif self.antipoision and not self.symbol and (not self.laibrarycan or self.knife):
            self.label.setText("Как только вы дотронулись до рамки, ваши руки пронзило острой болью. Посмотрев на них, вы увидели, что запястья покрылись коркой и начали кровоточить, а вся остальная рука покрылась сыпью. Вы вспомнили про яд. Превозмагая боль вы сняли картинку, при этом корка на пальцах треснула, и на пол начала капать кровь. Под картинкой вы обнаружили отверстие в форме круга разделенного на четыре части. Вы вспомнили эмблему на дневнике. Значит она все таки была нужна. Но у вас уже нет возможности ее достать. Вы умерли через какое-то время от голода и жажды.\n\nНачать игру заново?")
            
            self.pushButton.setText('Да')
            self.pushButton_2.setText('Да')
            self.pushButton_3.setText('Да')
            
            self.pushButton.clicked.connect(self.start)
            self.pushButton_2.clicked.connect(self.start)
            self.pushButton_3.clicked.connect(self.start)
        elif self.antipoision and self.symbol:
            self.label.setText("Не смотря на боль в руках, вы смогли снять фотографию. Под ней вы увидели выемку. Она была в форме круга разделенного на четыре части. Такой же формы была и эмблема на дневнике. Вы вспомнили про пластину в вашем кармане. Вы достали ее и вставили в углубление. В этот момент одна из стен начала уходить вниз, и за ней оказалась лестница ведущая вверх. Вы стали подниматься вверх. Надеюсь вы сможете вернуться домой. Если вспомните, где он.")
            
            self.pushButton.setText('Закончить игру')
            self.pushButton_2.setText('Закончить игру')
            self.pushButton_3.setText('Закончить игру')
            
            self.pushButton.clicked.connect(self.start)
            self.pushButton_2.clicked.connect(self.start)
            self.pushButton_3.clicked.connect(self.start)
        
        def checkTrash(self):
            self.label.setText("Обломки были просто повсюду. Когда вы дотронулись до обломка доски, с вашего пальца сошла вся кожа\n\n(Это действие яда. Скоро ты умрешь. Наверное адреналин, который ты испытывал до этого, заглушал всю боль.)\n\nВы решили поднять еще несколько досок. Под ними оказалось несколько книг и склянок. Возможно это противоядие. В любом случае у вас два выбора: либо умереть от яда мха, либо умереть от яда в склянке. Вы выбрали второй вариант. Выпив содержимое бутылей, вам стало легче. Не зная сколько этот эффект продержится, вы решаете скорей осмотреть фотографию")
            
            self.antipoision = True
            
            self.pushButton.setText('Дальше')
            self.pushButton_2.setText('Дальше')
            self.pushButton_3.setText('Дальше')
            
            self.pushButton.clicked.connect(self.checkFoto)
            self.pushButton_2.clicked.connect(self.checkFoto)
            self.pushButton_3.clicked.connect(self.checkFoto)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())