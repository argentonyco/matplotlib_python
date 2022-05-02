import matplotlib.pyplot as plt
import csv

with open('ventas.csv', 'r') as csvfile:
    datos_ventas = list(csv.DictReader(csvfile)) 
    ventas_filtro_mes = [i for i in datos_ventas if i['Mes'] == '1']
    
    dias_x = [int(i['Dia']) for i in ventas_filtro_mes]
    ventas_y = [int(i['Alimentos']) for i in ventas_filtro_mes]
    # datos_x=int(dias_x)
    # datos_y=int(ventas_y)
    # dias_x =['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    # ventas_y=['1112', '789', '955', '1269', '671', '1197', '1582', '1719', '1912', '1968', '1076', '1052', '1617', '1328', '1505', '1936', '943', '1244', '948', '1151', '1453', '565', '1384', '1847', '1091', '1919', '1038', '1908', '1074', '1094']

    plt.plot(dias_x, ventas_y, color='red', marker='o')
    plt.title('Unemployment Rate Vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Unemployment Rate', fontsize=14)
    plt.grid(True)
    plt.show()