from sklearn.cluster import KMeans
import numpy as np
from Classes import Potty
from Mappings import daysOfWeek
# NPArray = np.array(Alldata) #put in a np array for KMeans
# kmeans = KMeans(n_clusters=K, random_state=0).fit(NPArray)
# Website for tutorial: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html


def clusterPotties(potties, numberOfClusters):
    #put data in a form that KMeans will use
    lnglatData= []
    for potty in potties:
        toadd = [potty.longitude, potty.latitude]
        lnglatData.append(toadd)
    lnglatData= np.array(lnglatData)
    kmeans = KMeans(n_clusters=numberOfClusters, random_state=0).fit(lnglatData)
    #organize the potties into their correct clusters
    newPottiesArray = [] #Here I are thinking memory usage is not as important as speed
    cluteredPotties = []
    for num in range(len(daysOfWeek)):
        cluteredPotties.append([])
    for i, potty in enumerate(potties):
        cluster = kmeans.labels_[i]
        newPotty = Potty(number=potty.number,
                         name= potty.name,
                         address= potty.address,
                         cleanDayInt= int(cluster),
                         longitude= potty.longitude,
                         latitude= potty.latitude,
                         notes= potty.notes,
                         badAddress= potty.badAddress)
        newPottiesArray.append(newPotty)
        cluteredPotties[cluster].append(newPotty)
    
    return cluteredPotties, newPottiesArray

def clusterPottiesNew(potties, numberOfClusters):
    #put data in a form that KMeans will use
    lnglatData= []
    for potty in potties:
        toadd = [potty.latitude, potty.longitude]
        lnglatData.append(toadd)
    lnglatData= np.array(lnglatData)
    kmeans = KMeans(n_clusters=numberOfClusters, random_state=0).fit(lnglatData)
    #organize the potties into their correct clusters
    newPottiesArray = [] #Here I are thinking memory usage is not as important as speed
    cluteredPotties = []
    for i, potty in enumerate(potties):
        cluster = kmeans.labels_[i]
        newPotty = Potty(number=potty.number,
                         name= potty.name,
                         address= potty.address,
                         cleanDayInt= int(cluster),
                         longitude= potty.longitude,
                         latitude= potty.latitude,
                         notes= potty.notes,
                         badAddress= potty.badAddress)
        cluteredPotties.append(newPotty)
    
    return cluteredPotties