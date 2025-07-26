# demo.py
"""
Comprehensive Demo for Video Search Platform
Demonstrates all data structures and search capabilities
"""

from video_search_system import VideoSearchSystem, SearchResult
from hash_table import Video
import time
import json


class VideoSearchDemo:
    """Demo class for showcasing video search functionality"""
    
    def __init__(self):
        self.search_system = VideoSearchSystem()
        self.sample_videos = []
        
    def create_sample_data(self):
        """Create comprehensive sample video data for testing"""
        sample_videos_data = [
            {
                'video_id': 1,
                'title': 'The Shawshank Redemption',
                'year': 1994,
                'genre': ['Drama', 'Crime'],
                'actors': ['Tim Robbins', 'Morgan Freeman', 'Bob Gunton'],
                'directors': ['Frank Darabont'],
                'keywords': ['prison', 'hope', 'friendship', 'redemption'],
                'rating': 9.3,
                'description': 'Two imprisoned men bond over years, finding solace and redemption through acts of common decency.'
            },
            {
                'video_id': 2,
                'title': 'The Godfather',
                'year': 1972,
                'genre': ['Drama', 'Crime'],
                'actors': ['Marlon Brando', 'Al Pacino', 'James Caan'],
                'directors': ['Francis Ford Coppola'],
                'keywords': ['mafia', 'family', 'power', 'violence'],
                'rating': 9.2,
                'description': 'The aging patriarch of an organized crime dynasty transfers control to his reluctant son.'
            },
            {
                'video_id': 3,
                'title': 'The Dark Knight',
                'year': 2008,
                'genre': ['Action', 'Crime', 'Drama'],
                'actors': ['Christian Bale', 'Heath Ledger', 'Aaron Eckhart'],
                'directors': ['Christopher Nolan'],
                'keywords': ['superhero', 'batman', 'joker', 'justice'],
                'rating': 9.0,
                'description': 'Batman faces the Joker, a criminal mastermind who seeks to undermine the city\'s faith in its heroes.'
            },
            {
                'video_id': 4,
                'title': 'Forrest Gump',
                'year': 1994,
                'genre': ['Drama', 'Romance'],
                'actors': ['Tom Hanks', 'Robin Wright', 'Gary Sinise'],
                'directors': ['Robert Zemeckis'],
                'keywords': ['life', 'love', 'destiny', 'american history'],
                'rating': 8.8,
                'description': 'The life story of a man with a low IQ who achieves great things through kindness and determination.'
            },
            {
                'video_id': 5,
                'title': 'Inception',
                'year': 2010,
                'genre': ['Action', 'Sci-Fi', 'Thriller'],
                'actors': ['Leonardo DiCaprio', 'Marion Cotillard', 'Tom Hardy'],
                'directors': ['Christopher Nolan'],
                'keywords': ['dreams', 'reality', 'mind', 'heist'],
                'rating': 8.8,
                'description': 'A thief who enters people\'s dreams to steal secrets gets the inverse task of planting an idea.'
            },
            {
                'video_id': 6,
                'title': 'The Matrix',
                'year': 1999,
                'genre': ['Action', 'Sci-Fi'],
                'actors': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
                'directors': ['Lana Wachowski', 'Lilly Wachowski'],
                'keywords': ['virtual reality', 'philosophy', 'choice', 'rebellion'],
                'rating': 8.7,
                'description': 'A hacker discovers reality as he knows it is actually a computer simulation.'
            },
            {
                'video_id': 7,
                'title': 'Goodfellas',
                'year': 1990,
                'genre': ['Biography', 'Crime', 'Drama'],
                'actors': ['Robert De Niro', 'Ray Liotta', 'Joe Pesci'],
                'directors': ['Martin Scorsese'],
                'keywords': ['mafia', 'crime', 'loyalty', 'betrayal'],
                'rating': 8.7,
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen.'
            },
            {
                'video_id': 8,
                'title': 'Pulp Fiction',
                'year': 1994,
                'genre': ['Crime', 'Drama'],
                'actors': ['John Travolta', 'Samuel L. Jackson', 'Uma Thurman'],
                'directors': ['Quentin Tarantino'],
                'keywords': ['violence', 'redemption', 'dialogue', 'nonlinear'],
                'rating': 8.9,
                'description': 'The lives of two mob hitmen, a boxer, and others intertwine in four tales of violence and redemption.'
            },
            {
                'video_id': 9,
                'title': 'The Lord of the Rings: The Return of the King',
                'year': 2003,
                'genre': ['Adventure', 'Drama', 'Fantasy'],
                'actors': ['Elijah Wood', 'Viggo Mortensen', 'Ian McKellen'],
                'directors': ['Peter Jackson'],
                'keywords': ['fantasy', 'epic', 'friendship', 'good vs evil'],
                'rating': 8.9,
                'description': 'Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam.'
            },
            {
                'video_id': 10,
                'title': 'Fight Club',
                'year': 1999,
                'genre': ['Drama'],
                'actors': ['Brad Pitt', 'Edward Norton', 'Helena Bonham Carter'],
                'directors': ['David Fincher'],
                'keywords': ['society', 'identity', 'rebellion', 'consumerism'],
                'rating': 8.8,
                'description': 'An insomniac office worker forms an underground fight club that evolves into something much more.'
            },
            {
                'video_id': 11,
                'title': 'Interstellar',
                'year': 2014,
                'genre': ['Adventure', 'Drama', 'Sci-Fi'],
                'actors': ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain'],
                'directors': ['Christopher Nolan'],
                'keywords': ['space', 'time', 'love', 'survival'],
                'rating': 8.6,
                'description': 'A team of explorers travel through a wormhole in space in an attempt to save humanity.'
            },
            {
                'video_id': 12,
                'title': 'The Avengers',
                'year': 2012,
                'genre': ['Action', 'Adventure', 'Sci-Fi'],
                'actors': ['Robert Downey Jr.', 'Chris Evans', 'Scarlett Johansson'],
                'directors': ['Joss Whedon'],
                'keywords': ['superhero', 'team', 'action', 'marvel'],
                'rating': 8.0,
                'description': 'Earth\'s mightiest heroes must come together to stop an alien invasion.'
            }
        ]
        
        # Create Video objects from sample data
        for video_data in sample_videos_data:
            video = Video(**video_data)
            self.sample_videos.append(video)
        
        # Add all videos to the search system
        print("Adding sample videos to the search system...")
        results = self.search_system.bulk_add_videos(self.sample_videos)
        print(f"Successfully added {results['success']} videos, {results['failures']} failures")
    
    def demonstrate_basic_searches(self):
        """Demonstrate basic search functionality"""
        print("\n" + "="*70)
        print("BASIC SEARCH DEMONSTRATIONS")
        print("="*70)
        
        # Title search demonstrations
        print("\n1. TITLE SEARCH DEMONSTRATIONS")
        print("-" * 40)
        
        # Exact title search
        print("\n1.1 Exact Title Search: 'The Matrix'")
        results = self.search_system.search_by_title("The Matrix", "exact")
        self._display_results(results)
        
        # Prefix search
        print("\n1.2 Prefix Search: 'The'")
        results = self.search_system.search_by_title("The", "prefix", limit=5)
        self._display_results(results)
        
        # Fuzzy search (with typo)
        print("\n1.3 Fuzzy Search: 'Matriks' (typo for Matrix)")
        results = self.search_system.search_by_title("Matriks", "fuzzy")
        self._display_results(results)
        
        # Wildcard search
        print("\n1.4 Wildcard Search: 'The *night'")
        results = self.search_system.search_by_title("The *night", "wildcard")
        self._display_results(results)
        
        # Actor search demonstrations
        print("\n\n2. ACTOR SEARCH DEMONSTRATIONS")
        print("-" * 40)
        
        print("\n2.1 Search by Actor: 'Tom Hanks'")
        results = self.search_system.search_by_actor("Tom Hanks")
        self._display_results(results)
        
        print("\n2.2 Search by Actor with typo: 'Tom Hanx'")
        results = self.search_system.search_by_actor("Tom Hanx")
        self._display_results(results)
        
        # Genre search demonstrations
        print("\n\n3. GENRE SEARCH DEMONSTRATIONS")
        print("-" * 40)
        
        print("\n3.1 Search by Genre: 'Crime'")
        results = self.search_system.search_by_genre("Crime")
        self._display_results(results)
        
        print("\n3.2 Search by Genre: 'Sci-Fi'")
        results = self.search_system.search_by_genre("Sci-Fi")
        self._display_results(results)
        
        # Year search demonstrations
        print("\n\n4. YEAR SEARCH DEMONSTRATIONS")
        print("-" * 40)
        
        print("\n4.1 Search by Year: 1994")
        results = self.search_system.search_by_year(1994)
        self._display_results(results)
    
    def demonstrate_advanced_searches(self):
        """Demonstrate advanced search functionality"""
        print("\n" + "="*70)
        print("ADVANCED SEARCH DEMONSTRATIONS")
        print("="*70)
        
        # Complex multi-criteria search
        print("\n1. COMPLEX MULTI-CRITERIA SEARCH")
        print("-" * 40)
        
        criteria = {
            'genre': 'Drama',
            'year_range': (1990, 2000),
            'min_rating': 8.5
        }
        print(f"\n1.1 Search Criteria: {criteria}")
        results = self.search_system.complex_search(criteria)
        self._display_results(results)
        
        criteria2 = {
            'actor': 'Christopher',
            'genre': 'Action'
        }
        print(f"\n1.2 Search Criteria: {criteria2}")
        results = self.search_system.complex_search(criteria2)
        self._display_results(results)
        
        # Similar videos using graph analysis
        print("\n\n2. SIMILARITY SEARCH (GRAPH-BASED)")
        print("-" * 40)
        
        print("\n2.1 Find videos similar to 'The Matrix' (ID: 6)")
        results = self.search_system.get_similar_videos(6)
        self._display_results(results)
        
        print("\n2.2 Find videos similar to 'The Godfather' (ID: 2)")
        results = self.search_system.get_similar_videos(2)
        self._display_results(results)
        
        # Genre recommendations
        print("\n\n3. GENRE RECOMMENDATIONS")
        print("-" * 40)
        
        print("\n3.1 Top Crime movie recommendations")
        results = self.search_system.get_recommendations_by_genre("Crime")
        self._display_results(results)
    
    def demonstrate_special_features(self):
        """Demonstrate special features like auto-complete and collaborations"""
        print("\n" + "="*70)
        print("SPECIAL FEATURES DEMONSTRATIONS")
        print("="*70)
        
        # Auto-complete functionality
        print("\n1. AUTO-COMPLETE SUGGESTIONS")
        print("-" * 40)
        
        print("\n1.1 Auto-complete for 'The':")
        suggestions = self.search_system.get_auto_complete_suggestions("The", limit=8)
        for category, suggestion in suggestions:
            print(f"  [{category}] {suggestion}")
        
        print("\n1.2 Auto-complete for 'Cri' (genre focus):")
        suggestions = self.search_system.get_auto_complete_suggestions("Cri", "genre")
        for category, suggestion in suggestions:
            print(f"  [{category}] {suggestion}")
        
        # Actor collaborations
        print("\n\n2. ACTOR COLLABORATIONS")
        print("-" * 40)
        
        print("\n2.1 Actors who worked with 'Morgan Freeman':")
        collaborations = self.search_system.get_actor_collaborations("Morgan Freeman")
        for actor, depth in collaborations[:10]:
            print(f"  {actor} (connection depth: {depth})")
        
        # Spell correction
        print("\n\n3. SPELL CORRECTION")
        print("-" * 40)
        
        print("\n3.1 Search with spell correction: 'Godfathe' (missing r)")
        results = self.search_system.search_with_spell_correction("Godfathe", "title")
        self._display_results(results)
        
        print("\n3.2 Search with spell correction: 'Tomas Hanks' (wrong first name)")
        results = self.search_system.search_with_spell_correction("Tomas Hanks", "actor")
        self._display_results(results)
    
    def demonstrate_performance_analysis(self):
        """Demonstrate system performance and statistics"""
        print("\n" + "="*70)
        print("PERFORMANCE ANALYSIS & STATISTICS")
        print("="*70)
        
        # Perform various searches to generate statistics
        print("\nGenerating search statistics...")
        
        search_queries = [
            ("The", "title"),
            ("Action", "genre"),
            ("Tom Hanks", "actor"),
            ("Crime", "genre"),
            ("Fight", "title")
        ]
        
        for query, search_type in search_queries:
            if search_type == "title":
                self.search_system.search_by_title(query)
            elif search_type == "genre":
                self.search_system.search_by_genre(query)
            elif search_type == "actor":
                self.search_system.search_by_actor(query)
        
        # Get comprehensive system statistics
        stats = self.search_system.get_system_statistics()
        
        print("\n1. SYSTEM OVERVIEW")
        print("-" * 30)
        print(f"Total Videos: {stats['total_videos']}")
        print(f"Total Searches Performed: {stats['search_performance']['total_searches']}")
        print(f"Average Response Time: {stats['search_performance']['average_response_time']:.4f} seconds")
        
        print("\n2. SEARCH TYPE DISTRIBUTION")
        print("-" * 30)
        for search_type, count in stats['search_performance']['search_types'].items():
            print(f"  {search_type}: {count} searches")
        
        print("\n3. HASH TABLE PERFORMANCE")
        print("-" * 30)
        video_stats = stats['hash_table_stats']['videos']
        print(f"  Videos Table - Load Factor: {video_stats['load_factor']:.3f}")
        print(f"  Videos Table - Average Bucket Size: {video_stats['avg_bucket_size']:.2f}")
        print(f"  Actor Index - Items: {stats['hash_table_stats']['actor_index']['total_items']}")
        print(f"  Genre Index - Items: {stats['hash_table_stats']['genre_index']['total_items']}")
        
        print("\n4. TRIE SYSTEM EFFICIENCY")
        print("-" * 30)
        title_trie_stats = stats['trie_stats']['title_trie']
        print(f"  Title Trie - Words: {title_trie_stats['word_count']}")
        print(f"  Title Trie - Nodes: {title_trie_stats['node_count']}")
        print(f"  Title Trie - Memory Efficiency: {title_trie_stats['memory_efficiency']:.3f}")
        
        print("\n5. GRAPH ANALYSIS")
        print("-" * 30)
        graph_stats = stats['graph_stats']
        print(f"  Total Nodes: {graph_stats['total_nodes']}")
        print(f"  Total Edges: {graph_stats['total_edges']}")
        print(f"  Graph Density: {graph_stats['graph_density']:.4f}")
        print(f"  Average Degree: {graph_stats['average_degree']:.2f}")
        print(f"  Node Types:")
        for node_type, count in graph_stats['node_type_counts'].items():
            print(f"    {node_type}: {count}")
    
    def demonstrate_edge_cases(self):
        """Demonstrate edge cases and error handling"""
        print("\n" + "="*70)
        print("EDGE CASES & ERROR HANDLING")
        print("="*70)
        
        print("\n1. EMPTY QUERIES")
        print("-" * 20)
        print("1.1 Empty title search:")
        results = self.search_system.search_by_title("")
        print(f"  Results: {len(results)} (should be 0)")
        
        print("\n2. NON-EXISTENT SEARCHES")
        print("-" * 30)
        print("2.1 Search for non-existent actor:")
        results = self.search_system.search_by_actor("Non Existent Actor")
        print(f"  Results: {len(results)} (should be 0)")
        
        print("\n2.2 Search for non-existent genre:")
        results = self.search_system.search_by_genre("NonExistentGenre")
        print(f"  Results: {len(results)} (should be 0)")
        
        print("\n3. SIMILARITY WITH NON-EXISTENT VIDEO")
        print("-" * 40)
        print("3.1 Find similar videos for non-existent video ID:")
        results = self.search_system.get_similar_videos(999)
        print(f"  Results: {len(results)} (should be 0)")
        
        print("\n4. COMPLEX SEARCH WITH NO MATCHES")
        print("-" * 40)
        criteria = {
            'genre': 'NonExistentGenre',
            'year_range': (2030, 2040),
            'min_rating': 10.0
        }
        print(f"4.1 Impossible search criteria: {criteria}")
        results = self.search_system.complex_search(criteria)
        print(f"  Results: {len(results)} (should be 0)")
    
    def _display_results(self, results, max_display=5):
        """Helper method to display search results in a formatted way"""
        if not results:
            print("  No results found.")
            return
        
        print(f"  Found {len(results)} result(s):")
        for i, result in enumerate(results[:max_display]):
            print(f"    {i+1}. {result}")
        
        if len(results) > max_display:
            print(f"    ... and {len(results) - max_display} more results")
    
    def run_full_demo(self):
        """Run the complete demonstration"""
        print("="*70)
        print("VIDEO SEARCH PLATFORM - COMPREHENSIVE DEMO")
        print("Demonstrating Advanced Data Structures Integration")
        print("="*70)
        
        # Create and populate sample data
        start_time = time.time()
        self.create_sample_data()
        setup_time = time.time() - start_time
        print(f"Data setup completed in {setup_time:.4f} seconds\n")
        
        # Run all demonstrations
        self.demonstrate_basic_searches()
        self.demonstrate_advanced_searches()
        self.demonstrate_special_features()
        self.demonstrate_performance_analysis()
        self.demonstrate_edge_cases()
        
        print("\n" + "="*70)
        print("DEMO COMPLETED SUCCESSFULLY")
        print("="*70)
        print("\nKey Features Demonstrated:")
        print("✓ Hash Table-based metadata storage and indexing")
        print("✓ Trie-based prefix, fuzzy, and wildcard searching")
        print("✓ Graph-based similarity analysis and recommendations")
        print("✓ Complex multi-criteria search capabilities")
        print("✓ Auto-complete and spell correction")
        print("✓ Performance monitoring and statistics")
        print("✓ Robust error handling and edge cases")
        
        # Export system data
        print(f"\nTotal searches performed: {self.search_system.search_stats['total_searches']}")
        print(f"Average response time: {self.search_system.search_stats['average_response_time']:.4f} seconds")


if __name__ == "__main__":
    # Run the comprehensive demo
    demo = VideoSearchDemo()
    demo.run_full_demo()
