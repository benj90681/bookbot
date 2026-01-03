import sys
from stats import get_num_words, get_num_characters, get_sorted_dictionaries, sort_on
def main():
    if len(sys.argv) != 2:
    	print("Usage: python3 main.py <path_to_book>")
    	sys.exit(1)
    else:	 
    	book_path = sys.argv[1]
    	text = get_book_text(book_path)
    	num_words = get_num_words(text)
    	#print(f"Found {num_words} total words")
    	#print(get_num_characters(text))
    	#print(get_sorted_dictionaries(text))
    	print("============ BOOKBOT ============")
    	print(f"Analyzing book found at {book_path}...")
    	print("----------- Word Count -----------")
    	num_words = get_num_words(text)
    	print(f"Found {num_words} total words")
    	sorted_chars = get_sorted_dictionaries(text)   
    	print("--------- Character Count ---------")
    	for item in sorted_chars:
    		char = item["char"]
    		count = item["count"]
    		if char.isalpha():
    			print(f"{char}: {count}")
    	print("============ END ============")
    
   
   
def get_book_text(path):
    with open(path) as f:
        return f.read()





main()
