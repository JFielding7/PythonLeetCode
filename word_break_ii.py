from typing import List


def construct_trie(words):
    trie = {}

    for word in words:
        curr_node = trie

        for char in word:
            if char in curr_node:
                curr_node = curr_node[char]
            else:
                next_node = curr_node[char] = {}
                curr_node = next_node
        curr_node[""] = None

    return trie

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = construct_trie(wordDict)
        length = len(s)
        breaks = [[""]]

        for start in reversed(range(length)):
            curr_node = trie
            curr_breaks = []

            for i in range(start, length):
                char = s[i]
                if char not in curr_node:
                    break

                curr_node = curr_node[char]
                if "" in curr_node:
                    curr_word = s[start: i + 1]
                    for phrase in breaks[length - i - 1]:
                        curr_breaks.append(f"{curr_word} {phrase}".strip())

            breaks.append(curr_breaks)

        return breaks[-1]


s = "catsanddog"
d = ["cat","cats","and","sand","dog", "dotr"]
Solution().wordBreak(s, d)

