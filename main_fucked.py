def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

#old print
#def main():
#	print(get_book_text("books/frankenstein.txt"))


#def text():
#	return get_book_text.split("frankenstein.txt")


def num_words(path):
	return len(get_book_text(path).split())

#new func accepts text from book as string and returns numb words
def main():
	path = "books/frankenstein.txt"
	print(f"Found {num_words(path)} total words")



main()
