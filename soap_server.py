from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class MediaService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def calcular_media(ctx, *numeros):
        media = sum(numeros) / len(numeros)
        return f'A média é: {media}'

application = Application([MediaService], 'urn:media', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)

    print("Servidor SOAP iniciado. Aguardando requisições...")
    server.serve_forever()
