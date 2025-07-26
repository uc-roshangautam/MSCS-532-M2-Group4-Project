# demo.py
from hash_table import HashTable
from trie import Trie
from graph import Graph

if __name__ == "__main__":
    # Hash Table Test
    print("=== Hash Table Test ===")
    videos = HashTable()
    videos.insert(101, "Romantic Comedy")
    videos.insert(102, "Action Thriller")
    print("Search Video 101:", videos.search(101))
    print("Search Video 999 (Not Found):", videos.search(999))

    # Trie Test
    print("\n=== Trie Test ===")
    trie = Trie()
    trie.insert("romantic")
    trie.insert("romania")
    trie.insert("romantic comedy")
    print("Prefix 'rom':", trie.search_prefix("rom"))
    print("Prefix 'acti':", trie.search_prefix("acti"))  # Should return []

    # Graph Test
    print("\n=== Graph Test ===")
    g = Graph()
    g.add_edge("Tom Hanks", "Movie A")
    g.add_edge("Movie A", "Meg Ryan")
    g.add_edge("Meg Ryan", "Movie B")
    print("Connections from Tom Hanks:", g.bfs("Tom Hanks"))
