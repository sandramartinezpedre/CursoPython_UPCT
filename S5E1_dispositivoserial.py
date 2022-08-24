
import serial
import csv
port = serial.Serial('COM5', 115200, timeout=5) # Inicializamos con puerto y velocidad. Timeout:si tarda 5 segundos en mandar un dato, hace un break

last_value= 'read HEAD\n'
port.write(last_value.encode('utf8'))
last_value=port.readline().decode('utf8') #last_value_str
last_time=last_value.split(' ')[0] #tiempo(segundos) como str
last_time=int(last_time)  #Pasar last_time de str a numero entero
first_time= last_time - 90*24*3600 #90días, 24horas, 360 segundos por hora
mensaje = f'read {first_time}:{last_time}\n' #Leer datos desde la primer fecha hasta la ultima. f' y corchetes porque first_time y Last_time son variables
print(mensaje)
port.write(mensaje.encode('utf8'))
datos_str=''
while True:
    datos = port.readline() # Lee hasta que recibe '\n'
    datos_str+=datos.decode('utf8') #Añade lo leido
    print(datos)                 #Para observar los datos
    if len(datos)==0: #Si la longitud es 0, sale del bucle.
        break
datos_str=datos_str.split('\n')


with open('documento.csv', 'w') as csvfile:    #Crear documento csv
    fieldnames =['Time', 'Value']
    writer= csv.DictWriter (csvfile, fieldnames=fieldnames)
    writer.writeheader()
    datos_list=[]
    for x in datos_str:
        datos_list= x.split(' ')
        if len(datos_list)!= 2:
            break
        writer.writerow({'Time':datos_list[0], 'Value':datos_list[1]})
print ('ya está')
