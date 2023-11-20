from spyne import Application, rpc, ServiceBase, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class MediaService(ServiceBase):
    @rpc(Float, Float, _returns=Float)
    def calcular_media(ctx, num1, num2):
        media = (num1 + num2) / 2
        return media

# Criação da aplicação SOAP
app = Application([MediaService], 'exemplo_soap',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

# Configuração do servidor WSGI
wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    # Inicializa o servidor na porta 8000
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
