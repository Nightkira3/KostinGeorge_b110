"""
Реализовать решение следующей задачи:
Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) пишут в одну книгу.
Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся,
чтобы прочитать новые записи из неё. Каждый читатель и писатель – отдельный поток.
Одновременно книгу может читать несколько читателей, но писать единовременно может только один писатель.
"""

import threading
import time


class Book:
    def __init__(self):
        self.content = ""
        self.writer = None

    def write(self, text, writer):
        self.writer = writer
        self.content += text

    def read(self):
        return self.content


class WriterCounter:
    def __init__(self, count):
        self.count = count

    def next(self):
        writer = self.count
        self.count = (self.count % 2) + 1
        return writer


class ReaderCounter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1


class EndOfWork:
    def __init__(self):
        self.flag = False

    def finish(self):
        self.flag = True

    def is_finished(self):
        return self.flag


book = Book()
writers_count = WriterCounter(1)
readers_count = ReaderCounter()
end_of_work = EndOfWork()

book_sem = threading.Semaphore(1)
writers_count_sem = threading.Semaphore(1)
readers_count_sem = threading.Semaphore(1)
end_of_work_sem = threading.Semaphore(1)


class WriterThread(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self, name=name)
        self.sleep_time = sleep_time

    def run(self):
        global book, writers_count, end_of_work

        while not end_of_work.is_finished():
            with writers_count_sem:
                writer = writers_count.next()

            with book_sem:
                while readers_count.count > 0:
                    time.sleep(0.1)

                book.write(f"\nПисатель {writer} пишет в книгу.\n", writer)
                time.sleep(self.sleep_time)

            time.sleep(1)
