from stats import num_count , alpha_count , sorted_list_of_dict
import sys

def get_book_test (open_file_path):
    with open (open_file_path , encoding="utf-8-sig") as f :
        return f.read()
    




def main():
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    f = get_book_test(f'{sys.argv[1]}')
    number = num_count(f)
    print(alpha_count(f))
    alpha_dict = alpha_count(f)
    summary = sorted_list_of_dict(alpha_dict)
    print(summary)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {number} total words\n--------- Character Count -------\n")
    for letter_dict in summary:       
        print(f"{ letter_dict['char'] }: {letter_dict['num']}")

    print("============= END ===============")    


    return 0
main()