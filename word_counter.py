import re

def main():
  text = input("text: ")
  print(word_counter(text))


def word_counter(text):
    if not text:
        return 0

    text = text.replace("'", "")
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    print(text) 

    return len(text.split())

if __name__ == "__main__":
  main()