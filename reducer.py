import sys


class reducer:
    '''Reduces'''

    def reduce(self, line):
        word, index = line.split("\t")
        return word, index

    def main(self, fin):
        current_word = None
        current_list = []
        for line in fin:
            line = line.rstrip()
            word, linenum = self.reduce(line)
            if current_word is None:
                current_word = word

            if word == current_word:
                current_list.append(linenum)
            else:
                outline = current_word + ":"
                for item in current_list:
                    outline += item + ", "
                print(outline)
                current_word = word
                current_list = [linenum]

    if __name__ == "__main__":
        main()
