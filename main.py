from careertree import *
from bfs import breadth_first_search

def main():
    
    root = build_career_tree()

    while True:
        print(" " * 56)
        print("Available Categories:")

        category_names = get_category_names(root)

        for name in category_names:
            print(name)

        print(" " * 56)
        chosen_category = input("Choose a category: ")

        category_node = breadth_first_search(root, chosen_category)

        if category_node is None:
            print("Category not found. Try again.")
            continue

        print(" " * 56)
        print("Jobs in " + category_node.name + ":")

        job_names = get_job_names(category_node)

        for name in job_names:
            print(name)
        
        print("=" * 56)
        chosen_job = input("Choose a job: ")

        job_node =breadth_first_search(category_node, chosen_job)

        if job_node is None:
            print("Job not found in that category. Try again.")
            continue

        display_job_details(job_node)


        print("=" * 56)
        answer = input("Do you want to search again? (yes/no)")

        if answer != "yes":
            break




