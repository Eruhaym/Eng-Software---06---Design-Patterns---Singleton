from collections import deque

class FilaDeImpressao:
    _instancia = None

    def __init__(self):
        self.fila = deque()

    @staticmethod
    def get_instancia():
        if FilaDeImpressao._instancia is None:
            FilaDeImpressao._instancia = FilaDeImpressao()
        return FilaDeImpressao._instancia

    def queue(self, documento):
        self.fila.append(documento)

    def print(self):
        while self.fila:
            print("Imprimindo documento:", self.fila.popleft())

    def remove(self, documento):
        try:
            self.fila.remove(documento)
        except ValueError:
            print("Documento não encontrado na fila.")

    def clear(self):
        self.fila.clear()