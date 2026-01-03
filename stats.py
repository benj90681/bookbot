def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_num_characters(text):
	lower_text = text.lower()
	raw = list(lower_text)
	set_list =set(raw)
	char_dict = {}
	for char in set_list:
		char_dict[char] = raw.count(char)
	return char_dict
	
def get_sorted_dictionaries(text):
	sort_dict = get_num_characters(text)
	sorted_dict = []
	for char, count in sort_dict.items():
		tard_dict = {"char": char, "count": count}
		sorted_dict.append(tard_dict)	
	sorted_dict.sort(reverse=True, key=sort_on)
	return sorted_dict

def sort_on(items):
    return items["count"]

