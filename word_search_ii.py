from typing import List


DELTA = ((0, -1), (0, 1), (-1, 0), (1, 0))

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

def search_words(board, r, c, curr_word, curr_node, words_found):
    char = board[r][c]
    board[r][c] = ''

    if "" in curr_node:
        words_found.add(curr_word)

    for dr, dc in DELTA:
        i = r + dr
        j = c + dc

        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            curr_char = board[i][j]
            if curr_char != '' and curr_char in curr_node:
                search_words(board, i, j, curr_word + curr_char, curr_node[curr_char], words_found)

    board[r][c] = char

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = construct_trie(words)
        words_found = set()

        for i in range(len(board)):
            for j, char in enumerate(board[i]):
                if char in trie:
                    search_words(board, i, j, char, trie[char], words_found)

        return [*words_found]

