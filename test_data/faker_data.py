
from faker import Faker


class SearchBoxData:
    def __init__(self):
        self.__fake = Faker("pl_PL")
        self.SEARCH_BOX = self.__fake.word()

