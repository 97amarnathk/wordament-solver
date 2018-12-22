from Trie import Trie

word_list = ["mello","hackathon", "hack", "hacker"]

trie = Trie()

#trie.add_word(w)
trie.add_word("hello")
trie.add_word("hackathon")

print(trie.find_prefix('hackathon'))
print(trie.find_prefix('hello'))
print(trie.find_prefix('world'))
print(trie.find_prefix('mayday'))