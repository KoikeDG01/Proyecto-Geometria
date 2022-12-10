import matplotlib.pyplot as plt
import numpy as np

x = ['EN21','FE21','MA21','AB21','MY21','JN21','JL21','AG21','SE21','OC21','NO21',
     'DI21','EN22','FE22','MA22','AB22','MY22','JN22','JL22','AG22','SE22','OC22','NO22']
y = [77658,67950,58095,64202,95155,44534,96442,90801,68210,81605,65863,88246,82321,
     105516,90639,80504,75194,230249,64127,65324,55312,59259,89616]#Datos Provenientes de https://twitchtracker.com/ibai/statistics
fig = plt.subplots(figsize=(14,8))
plt.title('Grafica visualizaciones Mensuales ibai')
plt.xlabel('Promedio de visulizaciones diarias por Mes')
plt.ylabel('Número de visualizaciones')
plt.plot(x,y,'r-o')
plt.show()