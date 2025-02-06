
def main():
    print("Starting ...")

    lower_case_letters = []
    lc_range = range(ord('a'), ord('z'))
    print(lc_range)
    for num in lc_range:
        lower_case_letters.append(chr(num))

    # print(lower_case_letters)

    upper_case_letters = []
    uc_range = range(ord('A'), ord('Z'))
    for num in uc_range:
        upper_case_letters.append(chr(num))
    # print(upper_case_letters)

    all_chars = lower_case_letters + upper_case_letters
    print(all_chars)
    print("Done.")

if __name__ == "__main__":
    main()
