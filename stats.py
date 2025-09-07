def count_string_words(count_string):
    word_list = count_string.split()
    return len(word_list)

def char_counter(book):
    final_dict = {}
    for cr in book:
        c = cr.lower()
        if c in final_dict:
            final_dict[c] += 1
        else:
            final_dict[c] = 1
    return final_dict

