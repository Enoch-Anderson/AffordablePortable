#Excel file column numbers
#Name	Address     Cleaning Day 	Longitude	Latitude    Notes  
name = 0
address = 1
cleaningDay = 2
notes = 3
latitude = 4
longitude = 5
GoodAddress = 6
headers = [] #This is an empty array because I pull the headers off the excel file and fill them up in loadExcel()


#colum numbers for FirstRead for customer list.xlsx
ship2addy = range(22,27)
bill2addy = range(17, 22)
cName = 2
headings = ['Name', 'Address', 'Cleaning Day', 'Notes', 'Latitude', 'Longitude', 'GoodAddress'] #just storing the headder row for the out file here to be easily modified later
firstFile = 'ExcelFiles/customer list.xlsx'
firstOutput = 'ExcelFiles/MainExcel.xlsx'

#input and output excel files
openfile = 'ExcelFiles/MainExcel.xlsx'
outputfiles = ['ExcelFiles/Monday.xlsx', 'ExcelFiles/Tueday.xlsx', 'ExcelFiles/Wednesday.xlsx', 'ExcelFiles/Thursday.xlsx', 'ExcelFiles/Friday.xlsx', 'ExcelFiles/Saturday.xlsx', 'ExcelFiles/Sunday.xlsx']

#for clustering
numerOfClusters = 4  

#Useful other mappings that are used
weekdayToIntDictionary = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
intToWeekday = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
leftSideButtons = ['Save', 'Save Suggested', 'Show Suggested', 'Show Week', 'Show Monday', 'Show Tuesday', 'Show Wednesday', 'Show Thursday', 'Show Friday', 'Show Saturday', 'Show Sunday']

#Folium map startpoint and marker colors
mapStartPoint = (42.520834, -77.288842)#Starting it out at Sariah and Ben's house
markerColors = ['red', 'blue', 'green', 'purple', 'orange', 'cadetblue', 'lightred', 'darkred', 'darkblue', 'darkgreen', 'beige', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray'] #list of all the possible maker colors for follium


#styling
    #Week day in HBox styling
selectedWeekdayButton = 'cyan'
buttonBackgroundDefault = 'lightGray'
hBoxMinimumHeight = 60

#for badAddresses scrollable area
labelHeight  = 20
sArea = 100