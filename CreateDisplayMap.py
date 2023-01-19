import folium
import io
from PyQt5.QtWidgets import QWidget, QVBoxLayout
# from PyQt5.QtWebEngineWidgets import QWebEngineView
from Classes import Potty
from Mappings import mapStartPoint, markerColors
import webbrowser

#youtube tutorials that helped: https://www.youtube.com/watch?v=FdqDgoG-SFM&t=20s <-How to use folium to display markers and colors                            



#Below is code to get the map to open in the default web browser instead of a PyQt5 window.  This is more reliable, so I switched the whole application to use this method
# https://stackoverflow.com/questions/36969991/folium-map-not-displaying
class MapWebBrowser:
    def __init__(self, title: str, potties: list[Potty]):
        '''Just takes in a title and list of potties, creates class with showMap function to show the folium map on the default web browser'''
        self.title = title
        self.startLocation = [42.5236449, -77.2890644] #just set to PCS school right now
        self.zoom_start = 13
        self.potties = potties
        return
    
    def showMap(self):
        #Create the map
        my_map = folium.Map(title=self.title, location = self.startLocation, zoom_start = self.zoom_start)
        
        #potties is a 1d list now, instead of the 2d list it was in the previous version
        for potty in self.potties:
                if potty.badAddress or (potty.longitude == None or  potty.latitude == None): continue
                # print(f'{potty.name} {potty.latitude} {potty.longitude}' )
                coordinates = [potty.latitude, potty.longitude] 
                popupString = str(potty.number) + ' ' + potty.name
                Markercolor = markerColors[potty.cleanDayInt]
                folium.Marker(location=coordinates,
                              popup=popupString,
                            tooltip=popupString,
                            icon=folium.Icon(color=Markercolor, icon='usd')
                            ).add_to(my_map)

        #Display the map
        my_map.save(self.title + '.html')
        webbrowser.open(self.title + '.html')
        return




# class MapWindow(object):
#     def setupUi(self, SecondWindow, potties):
#         widget = MyApp(potties)
#         SecondWindow.setCentralWidget(widget)
#         return

# class MyApp(QWidget):
#     def __init__(self, potties):
#         super().__init__()
#         self.setWindowTitle('Folium in PyQt Example')
#         self.window_width, self.window_height = 100, 100
#         self.setMinimumSize(self.window_width, self.window_height)
        
#         layout = QVBoxLayout()
#         self.setLayout(layout)
        
#         m = folium.Map(
#             title = 'My House',
#             zoom_start=13,
#             location=mapStartPoint
#         )
#         for cluster in potties:
#             for potty in cluster:
#                 if potty.longitude == None or  potty.latitude == None: continue
#                 print(f'{potty.name} {potty.latitude} {potty.longitude}' )
#                 # coordinates = [potty.longitude, potty.latitude] 
#                 coordinates = [potty.latitude, potty.longitude] 
#                 popupString = str(potty.number) + ' ' + potty.name
#                 Markercolor = markerColors[potty.cleanDayInt]
#                 folium.Marker(location=coordinates,
#                               popup=popupString,
#                             tooltip=popupString,
#                             icon=folium.Icon(color=Markercolor, icon='usd')
#                             ).add_to(m)
        
#         #save map data to data object
#         data = io.BytesIO()
#         m.save(data, close_file=False)
        
#         webView = QWebEngineView()
#         webView.setHtml(data.getvalue().decode())
#         layout.addWidget(webView)
#         return


#Testing code
#Define coordinates of where we want to center our map
# potties = [Potty(1, 'Enoch', None, 1, -78.7769027, 43.0330453,   None, False), Potty(1, 'Sariah', None, 1, -77.6600776, 42.3329526,  None, False), Potty(1, 'David', None, 1, -77.1098983, 42.5567795, None, False)]
# map = MapWebBrowser('Testing Title', potties)
# map.showMap()
# print(
#     'done'
# )