from data import industry_tech_data
class TreeNode:
    def __init__(self):
        self.name = None
        self.children = []
        self.details = {}
        self.node_type = None

    def add_child(self, node):
        self.children.append(node)

def build_career_tree():
    root_node = TreeNode()
    root_node.name = "Tech Careers"
    root_node.node_type = "root"

    for category_name, category_data in industry_tech_data.items():
        category_node = TreeNode()
        category_node.name = category_name
        category_node.node_type = "category"

        careers_dict = category_data["careers"]

        for job_name, job_info in careers_dict.items():
            job_node = TreeNode()
            job_node.name = job_name
            job_node.node_type = "job"
            job_node.details = job_info 

            category_node.add_child(job_node)

        root_node.add_child(category_node)

    return root_node

def get_category_names(root_node):
    category_names = []
    
    for child in root_node.children:
        category_names.append(child.name)

    return category_names

def get_job_names(category_node):
    job_names = []

    for child in category_node.children:
        job_names.append(child.name)

    return job_names

def display_job_details(job_node):
    info = job_node.details

    print("\n" + "=" * 72)
    print(" Career Profile: " + job_node.name)
    print("=" * 72)
    print("Description:")
    print("  " + info["description"])

    print("\nRequirements:")
    for requirement in info["requirements"]:
        print("  - " + requirement)

    print("\nWhere To Work:")
    for place in info["where_to_work"]:
        print("  - " + place)

    print("\nAverage Monthly Salary (BWP):")
    print("  " + info["avg_monthly_salary_bwp"])
    print("=" * 72)

