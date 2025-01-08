'''
ESTE EJEMPLO FUNCION OK 
realizador con IDE CURSOR.COM
Este ejemplo es un web server con Flash que escucha el puerto 8002 y recibe parámetros POST json
los mismos se muestran en la consola y en la respuesta.

'''
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return f"""
<p>
Bienvenido a la API<br>
---------------------<br>

Descripción: Esta es una API que acepta peticiones POST con datos JSON<br>
Ruta API: /api<br>

Ejemplo de JSON para enviar:<br>
(<br>
"nombre": "valor", <br>
"edad": "valor",<br>
"Content-Type": "application/json"<br>
)<br><br>

<a href="https://rsuriani99.ngrok.app/api">Ir al/api es ruta fija</a><br><br>

<a href="https://reqbin.com/post-online">post tool reqbin.com</a><br><br>

<a href="chrome-extension://aejoelaoggembcahagimdiliamlcdmfm/index.html#requests">chrome extension Talent Api Tester</a><br><br>

Hora actual: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
</p>
"""


@app.route('/api', methods=['POST'])
def recibir_datos():
    # Verificar si hay datos JSON en la petición respondo con mensaje
    if not request.is_json:
        return {
            'error': 'Esta API espera datos en formato JSON',
            'ejemplo': {
                'nombre': 'valor',
                'edad': 'valor'
            },
            'metodo_esperado': 'POST',
            'hora_actual': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }, 400

    # Obtener los datos del cuerpo de la petición POST
    datos = request.get_json()
    
    # Verificar si el JSON está vacío
    if not datos:
        return {
            'error': 'El JSON recibido está vacío',
            'ejemplo': {
                'nombre': 'valor',
                'edad': 'valor'
            },
            'metodo_esperado': 'POST',
            'hora_actual': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }, 400

    # Imprimir los datos recibidos en la consola
    print("Datos recibidos:")
    print("-" * 30)
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
    print("-" * 30)
    
    # Crear lista de parámetros recibidos
    parametros_recibidos = [f"{clave}: {valor}" for clave, valor in datos.items()]
    
    # Devolver una respuesta
    return {
        'mensaje': 'Datos recibidos correctamente',
        'datos_recibidos': datos,        
        'lista_parametros': parametros_recibidos,
        'total_parametros': len(parametros_recibidos),
        'hora_actual': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }, 200

if __name__ == '__main__':
    app.run(debug=True, port=8002)
