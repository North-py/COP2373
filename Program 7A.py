def main():
    sentences = []

    print("Enter sentences (type 'exit' to finish):")
    while True:
        sentence = input()
        if sentence.lower() == 'exit':
            break
        sentences.append(sentence)

    # Display sentences and count
    print("\nYou entered the following sentences:")
    for idx, sentence in enumerate(sentences, start=1):
        print(f"{idx}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()
