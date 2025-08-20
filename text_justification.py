class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        curr_width = 0
        curr_words = 0
        justified = []

        for i, word in enumerate(words):
            length = len(word)
            if length + curr_width <= max_width:
                curr_width += length + 1
                curr_words += 1
            else:
                if curr_words == 1:
                    justified.append(f"{words[i - 1]}{' ' * (max_width - curr_width + 1)}")
                else:
                    spaces = max_width - curr_width + curr_words
                    min_spaces = spaces // (curr_words - 1)
                    rem_spaces = spaces % (curr_words - 1)

                    curr_line = []

                    for j in range(i - curr_words, i):
                        curr_line.append(words[j])
                        if j != i - 1:
                            curr_line.append(" " * (min_spaces + (rem_spaces > 0)))
                            rem_spaces -= 1

                    justified.append("".join(curr_line))

                curr_width = length + 1
                curr_words = 1

        length = len(words)
        justified.append(f"{' '.join(words[length - curr_words:length])}{' ' * (max_width - curr_width + 1)}")

        return justified
