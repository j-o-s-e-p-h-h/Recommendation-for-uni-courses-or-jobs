from difflib import get_close_matches

from bfs import breadth_first_search
from careertree import *


BANNER = r"""
========================================================================
   _______        _      _____                           _______
  |__   __|      | |    / ____|                         |__   __|
     | | ___  ___| |__ | |     __ _ _ __ ___  ___ _ __    | |_ __ ___  ___
     | |/ _ \/ __| '_ \| |    / _` | '__/ _ \/ _ \ '__|   | | '__/ _ \/ _ \
     | |  __/ (__| | | | |___| (_| | | |  __/  __/ |      | | | |  __/  __/
     |_|\___|\___|_| |_|\_____\__,_|_|  \___|\___|_|      |_|_|  \___|\___|

                             /\
                            /**\
                           /****\
                          /******\
                             ||

                    Tech Career Recommendation Tree
========================================================================
"""


def print_banner():
    print(BANNER)
    print("Browse a category, open its jobs, and inspect the career details.\n")


def print_section(title):
    print("\n" + "=" * 72)
    print(" " + title)
    print("=" * 72)


def print_numbered_list(options):
    for index, option in enumerate(options, start=1):
        print(f" {index}. {option}")


def prompt_with_autocomplete(prompt, options, item_label):
    current_options = list(options)
    base_options = list(options)
    current_prompt = prompt

    while True:
        user_input = input(current_prompt).strip()

        if not user_input:
            print(f"Please enter a {item_label} number or name.")
            continue

        if user_input.isdigit():
            selected_index = int(user_input) - 1
            if 0 <= selected_index < len(current_options):
                return current_options[selected_index]

            print(f"That {item_label} number is not in the list shown.")
            continue

        lowered_input = user_input.lower()
        exact_matches = {
            option.lower(): option
            for option in current_options
        }
        if lowered_input in exact_matches:
            return exact_matches[lowered_input]

        prefix_matches = [
            option
            for option in current_options
            if option.lower().startswith(lowered_input)
        ]
        if len(prefix_matches) == 1:
            print(f"Auto-selected {item_label}: {prefix_matches[0]}")
            return prefix_matches[0]

        if len(prefix_matches) > 1:
            print_section(f"Matching {item_label.title()}s")
            print_numbered_list(prefix_matches)
            print(f"Type the number shown or more letters to narrow the {item_label}.")
            current_options = prefix_matches
            current_prompt = f"Refine {item_label}: "
            continue

        close_matches = get_close_matches(
            user_input,
            current_options,
            n=min(5, len(current_options)),
            cutoff=0.35,
        )
        if close_matches:
            print_section(f"Closest {item_label.title()} Matches")
            print_numbered_list(close_matches)
            print(f"Type the number shown or more letters to narrow the {item_label}.")
            current_options = close_matches
            current_prompt = f"Refine {item_label}: "
            continue

        print(f"No matching {item_label} found. Please try again.")
        current_options = base_options
        current_prompt = prompt


def main():
    root = build_career_tree()
    print_banner()

    while True:
        category_names = get_category_names(root)
        print_section("Available Categories")
        print_numbered_list(category_names)
        print("Tip: enter the category number or type its name.")

        chosen_category = prompt_with_autocomplete(
            "Choose a category: ",
            category_names,
            "category",
        )

        category_node = breadth_first_search(root, chosen_category)

        if category_node is None:
            print("Category not found. Try again.")
            continue

        job_names = get_job_names(category_node)
        print_section("Jobs In " + category_node.name)
        print_numbered_list(job_names)
        print("Tip: enter the job number or the first few letters of the title.")

        chosen_job = prompt_with_autocomplete(
            "Choose a job: ",
            job_names,
            "job",
        )

        job_node = breadth_first_search(category_node, chosen_job)

        if job_node is None:
            print("Job not found in that category. Try again.")
            continue

        display_job_details(job_node)

        answer = input("\nSearch again? (yes/no): ").strip().lower()

        if answer not in {"yes", "y"}:
            print("\nThanks for using the Tech Career Recommendation Tree.")
            break


if __name__ == "__main__":
    main()


