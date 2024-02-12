import io
import time


def load_vectors(fname):
    fin = io.open(fname, "r", encoding="utf-8", newline="\n", errors="ignore")
    num_words, vec_size = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(" ")
        data[tokens[0]] = list(map(float, tokens[1:]))

    return data


#######################################################
# These 3 functions calculate the cosine similarity for
# any 2 word vectors
def dot_product(vec_a, vec_b):
    dot_prod = 0.0
    for i in range(len(vec_a)):
        dot_prod += vec_a[i] * vec_b[i]

    return dot_prod


import math


def magnitude(vector):
    return math.sqrt(dot_product(vector, vector))


# The entry point function
def cosine_similarity(vec_a, vec_b):
    dot_prod = dot_product(vec_a, vec_b)
    magnitude_a = magnitude(vec_a)
    magnitude_b = magnitude(vec_b)

    return dot_prod / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    start = True

    print(
        "\n╭─────────────────────────╮\n│  Word vector Loading... │\n╰─────────────────────────╯"
    )
    # store the start and end time the program uses to lead the vectors
    start_time = time.strftime("%H:%M:%S", time.localtime())
    vectors = load_vectors("FastText100K.txt")
    end_time = time.strftime("%H:%M:%S", time.localtime())

    print(
        f"╒═══════════════════════╕\n│Start time: {start_time}\t│\n│End time: {end_time}\t│\n╰───────────────────────╯"
    )

    print(
        "\t╭─────────────────────────╮\n\t│  Word vector loaded...  │\n\t╰─────────────────────────╯"
    )

    # my thought process was that after getting the cosine similarity for a particular word i will need to store those words and the cosine value
    # If the user input is in the dictionary, it calculates the cosine similarity for each word in the dictionary and stores the word and the corresponding cosine value
    # in a new 2 dimensional array called "cosine_results"
    # I then take all the cosine results and put in a new array called "cosine_vals"
    # I then sort "cosine_vals" in ascending order and read the array backwards and check if the last 5 items are in my "cosine_results"
    # and if it's there , it displays the associated cosine value and the word associated with that value

    while start == True:

        userInput = input("\nEnter search word <press [ENTER] to exit>: ")
        if userInput == "":
            print(
                "╭───────────────────────────────╮\n│   EXITING APPLICATION!!!\t│\n╰───────────────────────────────╯"
            )
            start = False

        if userInput in vectors:
            cosine_results = []
            cosine_vals = []
            input_vector = vectors[userInput]

            print(
                "\n╭──────────────────────────────╮\n│Finding Top 5 Similarities... │\n╰──────────────────────────────╯"
            )

            for item in vectors:
                if userInput != item:
                    cos_sim = cosine_similarity(input_vector, vectors[item])
                    cosine_results.append([item, cos_sim])
                    cosine_vals.append(cos_sim)
                    cosine_vals.sort()

            print(
                """\n╔═══════════════════════════════════════════════════════════════╗\n║ The words with the highest cosine similarity are:\t\t║\n╠═══════════════════════════════╤═══════════════════════════════╣"""
            )
            print(
                """║\tCOSINE SIMILARITY\t│ \tWORD\t\t\t║\n╚═══════════════════════════════╪═══════════════════════════════╝"""
            )
            for i in reversed(range(-5, 0)):
                for item in cosine_results:
                    if cosine_vals[i] in item:

                        print(
                            f"│\t{format(item[1],'.16f')}\t│\t{item[0]}\n├───────────────────────────────┼───────────────────────────────┤"
                        )

        elif userInput not in vectors and userInput != "":

            print(f"'{userInput}' is not in the Dictionary")
