import pytest

from typing import Optional


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self) -> Optional[dict]:
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def search(self, index):
        return self.queue[index]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue(
        {
            "nome_do_arquivo": "file_name1.txt",
            "linhas_do_arquivo": ["line_number_01", "line_number_02"],
            "qtd_linhas": 2,
        }
    )
    pq.enqueue(
        {
            "nome_do_arquivo": "file_name2.txt",
            "linhas_do_arquivo": ["line_number_02", "line_number_03"],
            "qtd_linhas": 2,
        }
    )

    pq.enqueue(
        {
            "nome_do_arquivo": "file_name3.txt",
            "linhas_do_arquivo": [
                "line_number_01",
                "line_number_02",
                "line_number_03",
                "line_number_04",
                "line_number_05",
            ],
            "qtd_linhas": 5,
        }
    )

    assert len(pq) == 3

    assert pq.dequeue() == {
        "nome_do_arquivo": "file_name1.txt",
        "linhas_do_arquivo": ["line_number_01", "line_number_02"],
        "qtd_linhas": 2,
    }
    assert pq.dequeue() == {
        "nome_do_arquivo": "file_name2.txt",
        "linhas_do_arquivo": ["line_number_02", "line_number_03"],
        "qtd_linhas": 2,
    }
    assert pq.dequeue() == {
        "nome_do_arquivo": "file_name3.txt",
        "linhas_do_arquivo": [
            "line_number_01",
            "line_number_02",
            "line_number_03",
            "line_number_04",
            "line_number_05",
        ],
        "qtd_linhas": 5,
    }

    assert len(pq) == 0

    pq.enqueue(
        {
            "nome_do_arquivo": "file_name4.txt",
            "linhas_do_arquivo": ["line_number_01", "line_number_02",
                                  "line_number_03", "line_number_04"],
            "qtd_linhas": 4,
        }
    )
    pq.enqueue(
        {
            "nome_do_arquivo": "file_name5.txt",
            "linhas_do_arquivo": [
                "line_number_01",
                "line_number_02",
                "line_number_03",
                "line_number_04",
                "line_number_05",
                "line_number_06",
            ],
            "qtd_linhas": 6,
        }
    )

    assert pq.search(0) == {
        "nome_do_arquivo": "file_name4.txt",
        "linhas_do_arquivo": ["line_number_01", "line_number_02",
                              "line_number_03", "line_number_04"],
        "qtd_linhas": 4,
    }
    assert pq.search(1) == {
        "nome_do_arquivo": "file_name5.txt",
        "linhas_do_arquivo": [
            "line_number_01",
            "line_number_02",
            "line_number_03",
            "line_number_04",
            "line_number_05",
            "line_number_06",
        ],
        "qtd_linhas": 6,
    }

    pq.enqueue(
        {
            "nome_do_arquivo": "file_name6.txt",
            "linhas_do_arquivo": ["line_number_01", "line_number_02",
                                  "line_number_03"],
            "qtd_linhas": 3,
        }
    )
    pq.enqueue(
        {
            "nome_do_arquivo": "file_name7.txt",
            "linhas_do_arquivo": ["line_number_01", "line_number_02",
                                  "line_number_03", "line_number_04"],
            "qtd_linhas": 4,
        }
    )

    pq.dequeue()
    assert pq.dequeue() == {
        "nome_do_arquivo": "file_name6.txt",
        "linhas_do_arquivo": ["line_number_01", "line_number_02",
                              "line_number_03"],
        "qtd_linhas": 3,
    }
    assert pq.dequeue() == {
        "nome_do_arquivo": "file_name7.txt",
        "linhas_do_arquivo": ["line_number_01", "line_number_02",
                              "line_number_03", "line_number_04"],
        "qtd_linhas": 4,
    }

    pq.enqueue(
        {
            "nome_do_arquivo": "file_name8.txt",
            "linhas_do_arquivo": ["line_number_01", "line_number_02"],
            "qtd_linhas": 2,
        }
    )
    pq.enqueue(
        {
            "nome_do_arquivo": "file_name9.txt",
            "linhas_do_arquivo": ["line_number_02", "line_number_03"],
            "qtd_linhas": 2,
        }
    )

    pq.dequeue()
    pq.dequeue()
    pq.dequeue()

    assert len(pq) == 0
    with pytest.raises(IndexError):
        pq.search(0)
