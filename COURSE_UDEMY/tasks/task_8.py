# перевести  значення температури в цельсіях в значення по фаренгейту

def convert_temperature(temp_celsius):
    if temp_celsius < -273.15 or temp_celsius > 6000:
        return False
    return temp_celsius*9/5 + 32
temp_f = round(convert_temperature(36.6), 1)
print(f'Fahrenheit: {temp_f}')
#  варіант з простим списком
temps_celsius = [- 1.5 , 0.2 , 2.8 , 5.6 , 8.4 , 11.2 ,
                14.7 , 17.0 , 18.3 , 19.1 , 19.4 , 18.8 ,
                17.0 , 14.5 , 11.2 , 7.8 , 4.0
                ]
temps_fahrenheit = []
for temp in temps_celsius:
    temp_f = convert_temperature(temp)
    if temp_f is not False:
        temps_fahrenheit.append(round(temp_f, 1))
print(temps_fahrenheit)
#  варіант зі складним списком
temps_celsius = [
    ["06:00", -1.5],
    ["07:00", 0.2],
    ["08:00", 2.8],
    ["09:00", 5.6],
    ["10:00", 8.4],
    ["11:00", 11.2],
    ["12:00", 14.7],
    ["13:00", 17.0],
    ["14:00", 18.3],
    ["15:00", 19.1],
    ["16:00", 19.4],
    ["17:00", 18.8],
    ["18:00", 17.0],
    ["19:00", 14.5],
    ["20:00", 11.2],
    ["21:00", 7.8],
    ["22:00", 4.0]
]
temps_fahrenheit = []
for time,temp in temps_celsius:
    temp_f = convert_temperature(temp)
    if temp_f is not False:
        temps_fahrenheit.append([time, round(temp_f, 1)])
print(temps_fahrenheit)
