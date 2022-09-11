from pyngrok        import ngrok
from http.server    import BaseHTTPRequestHandler, HTTPServer

import json
import logging
import os

from conexion_mesa import Interseccion

num_agentes = 20
num_peatones = 5
tiempo_maximo = 0.1

model = Interseccion(num_agentes, num_peatones)

def featuresC(data):
    features = []
    for elem in data:
        if(elem['tipo'] == 'Coche'):
            feature = {'tipo' : elem['tipo'],
                    'id': elem['id'],
                    'X': elem['X'],
                    'Y': elem['Y']
                }
            features.append(feature)
    return json.dumps(features)

def featuresS(data):
    features = []
    for elem in data:
        if(elem['tipo'] == 'Semaforo'):
            feature = {'tipo' : elem['tipo'],
                    'id': elem['id'],
                    'X': elem['X'],
                    'Y': elem['Y'],
                    'estado': elem['estado']
                }
            features.append(feature)
    return json.dumps(features)

def featuresA(data):
    features = []
    for elem in data:
        if(elem['tipo'] == 'Ambulancia'):
            feature = {'tipo' : elem['tipo'],
                    'id': elem['id'],
                    'X': elem['X'],
                    'Y': elem['Y']
                }
            features.append(feature)
    return json.dumps(features)

def featuresP(data):
    features = []
    for elem in data:
        if(elem['tipo'] == 'Peaton'):
            feature = {'tipo' : elem['tipo'],
                    'id': elem['id'],
                    'X': elem['X'],
                    'Y': elem['Y']
                }
            features.append(feature)
    return json.dumps(features)

class Server(BaseHTTPRequestHandler):
    
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", 
                     str(self.path), str(self.headers))
        self._set_response()
        model.step()
        data = model.status_agentes()

        resp = "{\"Coches\":" + featuresC(data) + ","
        resp = resp + "\"Semaforos\":" + featuresS(data) + ","
        resp = resp + "\"Ambulancias\":" + featuresA(data) + ","
        resp = resp + "\"Peatones\":" + featuresP(data) + "}"
        self.wfile.write(resp.encode('utf-8'))

    def do_POST(self):
        pass

def run(server_class=HTTPServer, handler_class=Server, port=8585):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    public_url = ngrok.connect(port).public_url
    logging.info(f"ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

    logging.info("Starting httpd...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == "__main__":
    run(HTTPServer, Server)