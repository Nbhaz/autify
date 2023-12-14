from src.domain.dumper import Dumper


class FileDumper(Dumper):
    def save(self, key, content):
        with open(key, "w", encoding="utf-8") as file:
            file.write(content)

    def fetch(self, key):
        with open(key, "r", encoding="utf-8") as file:
            data = file.read()
            return data
