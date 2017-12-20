import datetime

class Comentario():
    def __init__(self, texto):
        self.texto = texto
        self.data_coment = datetime.datetime.today()
