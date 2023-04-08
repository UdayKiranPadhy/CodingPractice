# SRP
# Separation of concerns


# A class should have only one responsibility


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # breaks SRP
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # breaks SRP
    # def load(self, filename):
    #     pass

    # breaks SRP
    # def load_from_web(self, uri):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()
    
    @staticmethod
    def load_from_file(filename):
        pass

    @staticmethod
    def load_from_web(uri):
        pass

j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries: \n{j}")

file = r"journal.txt"
PersistenceManager.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
     