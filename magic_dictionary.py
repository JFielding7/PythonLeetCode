class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        return any(len(word) == len(searchWord) and sum(word[i] != searchWord[i] for i in range(len(word))) == 1 for word in self.words)