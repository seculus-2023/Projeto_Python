from waitress import serve
from core.wsgi import application  # substitua 'seu_projeto' pelo nome da pasta do seu projeto

if __name__ == "__main__":
    serve(application, host='127.0.0.1', port=8000)
