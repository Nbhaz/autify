from src.domain.dumper import Dumper


class FileDumper(Dumper):

    def save(self, key, content):
        with open(key, 'w') as file:
            file.write(content)
        return

    def fetch(self, key):
        with open(key, 'r') as file:
            data = file.read()
            return data
