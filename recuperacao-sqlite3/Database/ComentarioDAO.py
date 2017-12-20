import sqlite3
from Model.Comentario import Comentario

class ComentarioDAO():

    def postar_comentario(self, comentario: Comentario):

        conn = sqlite3.connect('Database\IFNetwork.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO tb_comentario(texto, data_coment)
                VALUES (?, ?);
                """, (comentario.texto, comentario.data_coment))

        conn.commit()
        conn.close()
