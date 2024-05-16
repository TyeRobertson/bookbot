def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        content = f.read()
    count = word_count(content)
    print(f"{count} words found in the document")

def word_count(content):
    string_list = content.split()
    length = len(string_list)
    return length

main()