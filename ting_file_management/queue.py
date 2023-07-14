class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        value = self._data[0]
        self._data.remove(value)
        return value

    def search(self, index):
        data = self._data

        if index >= len(data) or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")

        return data[index]
