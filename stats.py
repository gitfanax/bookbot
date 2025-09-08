def count_string_words(count_string):
    word_list = count_string.split()
    return len(word_list)

def char_counter(book):
    final_dict = {}
    for cr in book:
        if cr.isalpha():
            c = cr.lower()
            if c in final_dict:
                final_dict[c] += 1
            else:
                final_dict[c] = 1
    return final_dict

def get_key(dictionary):
    return dictionary["num"]

def sort_dict(dict_of_chars):
    sorted_list = []
    for ch, cnt in dict_of_chars:
        tmp_dict = {}
        tmp_dict["char"] = ch
        tmp_dict["num"] = cnt
        sorted_list.append(tmp_dict)
    sorted_list.sort(reverse=True, key = get_key)
    return sorted_list
