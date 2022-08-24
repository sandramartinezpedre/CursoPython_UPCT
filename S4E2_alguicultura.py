import http.client
import json
import time




class Alguicultivo:
    cabecera = {
    'User-Agent': 'Python',
    'Accept': '*/*',
    'Content-Length': '0'
    }
    
    def __init__ (self, host:str, port:int=50600):
        self.(connection=http.client.HTTPConnection(host, port)
        
        
    def _request_route(self, ruta:str):
        self.connection.request('GET', ruta, headers=self.cabecera)
        respuesta= self.connection.getresponse()
        try:
            assert respuesta.code < 300
        except AssertionError:
            raise Exception (f'Error de llamada. Código: {respuesta.code}')   
        data=respuesta.read()
        data = data.decode('utf-8')
        return json.loads(data)
           
        
   
    def get_piscina (self, num: int):
        dic_datos = self._request_route(f'/explotacion/piscinas/{num}')
        return Piscina (dic_datos)
    
    
    def info (self):
        dic_datos= self._request_route('/explotacion')
        info_str= ' \n  ' + 'Company: ' + dic_datos['company'] + ' \n  ' + 'Localization: ' + dic_datos['localization'] + ' \n  ' + 'Area: ' + dic_datos['area'] + ' \n  ' + 'Foundation: ' + dic_datos['foundation'] +  ' \n  ' + 'Email: ' + ' \n  ' + dic_datos['contact']['email'] + '  \n  ' + 'Phone: ' + dic_datos['contact']['phone'] + '  \n  ' + 'Last check: ' + time.ctime(dic_datos['last_sys_check']) + '  \n  ' + 'Name: ' + dic_datos['checked_by']['name'] + '  \n  ' + dic_datos['checked_by']['id']
        return print (info_str)
        
    
    def load(self):
        return self._request_route('/explotacion/piscinas')
    
    
    def get_sensor(self, x_sensor:str):
        piscinas_lista = self.load()
        datos_lista=[]
        for piscina in piscinas_lista:
            datos_lista.append(piscina['sensors'][x_sensor])
        return datos_lista
    
    def cambio_datos(self, numero_piscina: int,  sensor:str, nuevo_valor: int):
               
        valor_actual={sensor:nuevo_valor}
        valor_actual_texto=json.dumps(valor_actual)
        ruta1=f'/set/piscinas/{numero_piscina}/{sensor}'
        self.connection.request('POST', ruta1 ,headers={'content-type': ' application/json'}, body= valor_actual_texto)
        respuesta_nueva=self.connection.getresponse()
        print (f'mensaje codigo: {respuesta_nueva.code}')
        try:
            assert respuesta_nueva.code < 300
        except AssertionError:
            raise Exception (f'Error de llamada. Código: {respuesta.code}')
        return 
    )
    def ver_datosconsigna (self, ruta:str):
        cabecera_consigna=self.cabecera.copy()
        cabecera_consigna['info']='false'
        self.connection.request('GET', ruta, headers=cabecera_consigna)
        respuesta_nueva=self.connection.getresponse()
        data_nueva=respuesta_nueva.read().decode('utf-8')
        return print(data_nueva)
        
          
 #connection.request('GET', '/set/piscinas/0/ph', headers=cabecera)

 #respuesta=connection.getresponse()

 #data= respuesta.read().decode('utf-8')

 #print (data)       
        
        
### connection.request('POST', '/set/piscinas/0/ph', headers={'content-type': ' application/json'}, body= valor_actual_texto)            
    
class Piscina:
    def __init__(self, pisci_datos):
        try:
            assert 'id' in pisci_datos
            assert 'sensors' in pisci_datos
            assert 'last_feeding' in pisci_datos
            assert 'release_date' in pisci_datos
            assert 'species' in pisci_datos
            assert 'capacity(L)' in pisci_datos
        except AssertionError:
            raise Exception['Faltan datos en pisci_datos']
        self.data=pisci_datos
    
    def get_pH(self):
        return self.data['sensors']['ph']
    def get_temp(self):
        return self.data['sensors']['temp']
    def get_salinidad(self):
        return self.data['sensors']['sali']
    def get_refr(self):
        return self.data['sensors']['refr']
     
    
    
    def __getitem__(self, item:str):
        return self.data['sensors'][item]
    
    def info (self):
        data= self.data
        infopisci_str= ' \n  ' + 'id: ' + str(data['id']) + ' \n  ' +'Last feeding: '+ time.ctime(data['last_feeding']) + ' \n  ' + 'Release date: ' + data['release_date'] + ' \n  ' + 'Species: ' + data['species'] +  ' \n  ' + 'Capacity: ' + str(data['capacity(L)']) 
        return print (infopisci_str)
                
    
    
    

        
  