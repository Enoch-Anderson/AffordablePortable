from PyQt5.QtWidgets import * #(QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication, QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from Classes import Potty
from CreateDisplayMap import MapWebBrowser
from Mappings import daysOfWeek, leftSideButtons, selectedWeekdayButton, buttonBackgroundDefault, weekdayToIntDictionary, numerOfClusters, labelHeight, sArea
import sys
from excel import loadExcel, SaveAll
from ClusterData import clusterPottiesNew

# t1Potty = Potty(0, 'Enoch Anderson', None, 0, None, None, None, None)
# t2Potty = Potty(1, 'Johnney Depp', None, 1, None, None, None, None)
# testlist = [t1Potty,t2Potty]
# for i in range(2, 50):
#     p = Potty(i, str(i), None, 2, None, None, None, None)
#     testlist.append(p)




class MainWindow(QMainWindow):
    def __init__(self, potties: list[Potty]):
        super().__init__()
        #Inializing the arrays that will be used to keep track of when each potty will be cleanded
        self.potties = potties
        self.weekdayArrays = []
        self.newPotties = []
        self.badaddyarray = []
        
        #filling the array of bad addresses and removing them from potties
        i = 0
        while i < len(self.potties):
            p = potties[i]
            if p.badAddress:
                self.badaddyarray.append(p)
                self.potties.remove(p)
                continue
            i += 1
        
        #for displaying the maps
        self.weekWindow = QMainWindow()
        self.suggestedWindow = QMainWindow()
        self.weekdayWindow = [] #This will be an array of QMainWindows
        self.uiWeek = None #This will be the MapWindow class for the display week button
        self.uiSuggested = None #This will be the MapWindow class for when show suggested is clicked
        self.uiWeekday = [] #this will be an array of MapWidows for when each day of the week is clicked
        
        
        
        #initialize the weekdayWindow array and uiWeekday used to store all the week day windows and MapWindows
        for i in range(len(daysOfWeek)):
            self.weekdayWindow.append(QMainWindow())
            self.uiWeekday.append(None)
            self.weekdayArrays.append([])#initalizing the weekdayArray
        
        #initalizing the weekdayArray array used to store the list of potties for each weekday
        for potty in potties:
            dayInt = potty.cleanDayInt
            self.weekdayArrays[dayInt].append(potty)
        self.initUI(potties)
        return
    
    def initUI(self, potties: list[Potty]):
        self.hbox = QHBoxLayout()
        self.widget = QWidget()
        self.vbox = QVBoxLayout() #This will hold the PottyScrollWindow and the BadAddress scroll window and then be added the the hbox that is the central widget
        self.vboxWidget = QWidget() #this is the widget that will hold the things in the vbox above
        
        #setting up the vbox
        object = PottyScrollWindow(potties)
        self.vbox.addWidget(object)
        object = BadAddresses(self.badaddyarray)
        self.vbox.addWidget(object)
        self.vboxWidget.setLayout(self.vbox)
        
        #add the 2 elements to the hbox
        object = leftSideHBox()
        self.hbox.addWidget(object)
        self.hbox.addWidget(self.vboxWidget)
        
        #setting the layout of the main widget
        self.widget.setLayout(self.hbox)
        
        #set Central and display
        self.setCentralWidget(self.widget)

        self.setGeometry(600, 100, 1200, 900)
        self.setWindowTitle('Main Window Testing')
        self.show()
        return
    
    def showWeekClicked(self):
        self.weekMap = MapWebBrowser('Full Current Week', self.potties)
        self.weekMap.showMap()
        return
        
    
    def saveClicked(self):
        combined = self.potties + self.badaddyarray
        SaveAll(combined, self.weekdayArrays)
        return
    
    def showWeekdayClicked(self, weekday):
        title = weekday
        potties = self.weekdayArrays[weekdayToIntDictionary[weekday]]
        self.weekMap = MapWebBrowser(title, potties) #change weekMap to an array that has a new spot for each day of week if this crashes
        self.weekMap.showMap()
        return
        
    def showSuggestedClicked(self):
        self.newPotties = clusterPottiesNew(self.potties, numerOfClusters)
        self.suggestedMap = MapWebBrowser('Suggested Weekday', self.newPotties)
        self.suggestedMap.showMap()
        return
    
    def saveSuggestedClicked(self):
        if self.newPotties == []:
            self.newPotties = clusterPottiesNew(self.potties, numerOfClusters)
        #update button colors
        # vbox = self.hbox.itemAt(1).widget().vbox #navigate down from mainwindow to the vbox that contains all the horizontal boxes with the buttons in them
        vbox = self.vbox.itemAt(0).widget().vbox
        for i in range(len(self.newPotties)):
            pOld = self.potties[i]
            pNew = self.newPotties[i]
            hbox = vbox.itemAt(i).widget().hbox
            #set old selected button color to default
            button = hbox.itemAt(pOld.cleanDayInt+1).widget()
            button.setStyleSheet("background-color : " + buttonBackgroundDefault)
            #set new button selected color to selected
            button = hbox.itemAt(pNew.cleanDayInt+1).widget()
            button.setStyleSheet("background-color : " + selectedWeekdayButton)
        #update potties, they have to be in order based off of button
        self.potties = self.newPotties
        #update weekdayArrays
        self.weekdayArrays = []
        for day in daysOfWeek:
            self.weekdayArrays.append([])
        for potty in self.potties:
            dayInt = potty.cleanDayInt
            self.weekdayArrays[dayInt].append(potty)
        #Save to excel
        self.saveClicked()
        return

class BadAddresses(QScrollArea):
    def __init__(self, badaddyarray: list[Potty]): #This will take in a list of potties that will be added to the scroll window
        super().__init__()
        self.initUI(badaddyarray)
        return

    def initUI(self, badaddyarray: list[Potty]):
        # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of labels and buttons
        

        for potty in badaddyarray:
            object = QLabel(f'{potty.number} {potty.name} {potty.address}')
            object.setMaximumHeight(labelHeight)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setMaximumHeight(sArea)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        return

class PottyScrollWindow(QScrollArea):

    def __init__(self, potties: list[Potty]): #This will take in a list of potties that will be added to the scroll window
        super().__init__()
        self.initUI(potties)
        return

    def initUI(self, potties: list[Potty]):
        # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of labels and buttons
        

        for potty in potties:
            object = PottyWindowElement(potty)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)
        return

class PottyWindowElement(QWidget):
    def __init__(self, potty: Potty):
        super().__init__()
        self.initUI(potty)
        return
        
    def initUI(self, potty: Potty):
        self.hbox = QHBoxLayout()
        #adding the name label
        object = QLabel(f'{potty.number+2} {potty.name}', self) #added 2 to the potty number so the number in the label matches the row number in the excel file
        object.adjustSize()
        self.hbox.addWidget(object)
        self.setMinimumHeight(100)
        
        #adding the 7 buttons with days of week
        for i, weekday in enumerate(daysOfWeek):
            object = QPushButton(weekday, self)
            name = f'{weekday} {potty.number} {potty.name}'
            object.setObjectName(name)
            object.installEventFilter(self)
            object.move(i*80+100,0)
            #choosing the correct color for initially displaying the button
            if i == potty.cleanDayInt:
                object.setStyleSheet("background-color : " + selectedWeekdayButton)
            else:
                object.setStyleSheet("background-color : " + buttonBackgroundDefault)
            self.hbox.addWidget(object)
        
        self.setLayout(self.hbox)
        return

    def eventFilter(self, source, event): #Reminder button name is of format 'DayOfWeek PottyNumber PersonName'
        '''This eventFilter handles when a week day button is clicked in the scroll area'''
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # print(source.objectName())
            bName = source.objectName() #bName is a stirg 'DayOfWeek PottyNumber PersonName'
            bName = bName.split(' ') #split into array [DayofWeek PottyNumber]
            bName[1] = int(bName[1]) #make PottyNumber an int so it can be used to access array indecies

            #Go into potties, using potty number to get correct one: Call this potty p
            hbox = source.parent().hbox
            potties = source.parent().parent().parent().parent().parent().parent().parent().potties
            weekdayArrays = source.parent().parent().parent().parent().parent().parent().parent().weekdayArrays
            p = potties[bName[1]]
            
            #Use P.cleanDayInt (old value) to find correct weekdayArrays and remove P from that array
            weekdayArrays[p.cleanDayInt].remove(p)
            
            #Use P.cleanDayInt (old value) to change the button color or current day back to default
            button = hbox.itemAt(p.cleanDayInt+1).widget() #the +1 is there because the label is the first element in the hbox
            button.setStyleSheet("background-color : " + buttonBackgroundDefault)
            
            #update to P's cleanDayInt to be new value
            dayInt = weekdayToIntDictionary[ bName[0] ]
            p.cleanDayInt = dayInt
            
            #add P to new correct weekdayArray
            weekdayArrays[p.cleanDayInt].append(p)
            
            #update weekday button to correct button color
            source.setStyleSheet("background-color : " + selectedWeekdayButton)
        return super().eventFilter(source, event)

class leftSideHBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        return
    
    def initUI(self):
        self.vbox = QVBoxLayout()
        for i, button in enumerate(leftSideButtons):
            name = button
            object = QPushButton(button, self) #I just want the button text to say what button says
            object.setObjectName(name)
            object.installEventFilter(self)
            object.move(0, i*10)
            self.vbox.addWidget(object)
        self.setLayout(self.vbox)
        return
    
    def eventFilter(self, source, event):
        '''This eventFilter handles when a button in the left side box is clicked'''
        if event.type() == QtCore.QEvent.MouseButtonPress:
            # print(source.objectName())
            bName = source.objectName()
            bName = bName.split(' ')
            mainwindow = source.parent().parent().parent()
            
            if bName[0] == 'Save':
                if len(bName) == 1:
                    mainwindow.saveClicked()
                else:
                    mainwindow.saveSuggestedClicked()
            elif bName[0] == 'Show':
                if bName[1] == 'Suggested':
                    mainwindow.showSuggestedClicked()
                elif bName[1] == 'Week':
                    mainwindow.showWeekClicked()
                else:
                    weekday = bName[1]
                    mainwindow.showWeekdayClicked(weekday)
            
        return super().eventFilter(source, event)
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    #load in potties in excel
    potties = loadExcel()    
    mainUI = MainWindow(potties)
    if not app.exec_():
        mainUI.weekWindow.close()
        for w in mainUI.weekdayWindow:
            w.close()
    
    sys.exit()

if __name__ == '__main__':
    main()