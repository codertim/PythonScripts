
import random


def main():
    print("Starting ...")
    potential_chars = get_potential_vals()
    print("potentail chars: ", potential_chars)
    print("Done.")


def get_potential_vals():
    # locer case letters
    lower_case_letters = []
    lc_range = range(ord('a'), ord('z'))
    print(lc_range)
    for num in lc_range:
        lower_case_letters.append(chr(num))

    # upper case letters
    upper_case_letters = []
    uc_range = range(ord('A'), ord('Z'))
    for num in uc_range:
        upper_case_letters.append(chr(num))

    # numbers
    nums = [x for x in range(10)]
    str_nums = []
    for num in nums:
        str_nums.append(str(num))

    all_chars = lower_case_letters + upper_case_letters + str_nums
    return all_chars



if __name__ == "__main__":
    main()
