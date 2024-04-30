class Employee:
    def __init__(self, emp_id, name):
        if not isinstance(emp_id, int) or emp_id < 0:
            raise ValueError("Employee ID must be a positive integer.")
        self.emp_id = emp_id

        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Employee name must be a non-empty string.")
        self.name = name.strip()

        self.left = None
        self.right = None

class OrganizationChart:
    def __init__(self):
        self.root = None

    def insert_employee(self, emp_id, name):
        if not isinstance(emp_id, int) or emp_id < 0:
            raise ValueError("Employee ID must be a positive integer.")
        
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Employee name must be a non-empty string.")

        new_employee = Employee(emp_id, name)

        if self.root is None:
            self.root = new_employee
        else:
            current = self.root
            while True:
                if emp_id < current.emp_id:
                    if current.left is None:
                        current.left = new_employee
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_employee
                        break
                    current = current.right

    def search_employee(self, emp_id):
        if not isinstance(emp_id, int) or emp_id < 0:
            raise ValueError("Employee ID must be a positive integer.")

        current = self.root
        while current is not None:
            if emp_id == current.emp_id:
                return current.name
            elif emp_id < current.emp_id:
                current = current.left
            else:
                current = current.right
        return None

    def delete_employee(self, emp_id):
        if not isinstance(emp_id, int) or emp_id < 0:
            raise ValueError("Employee ID must be a positive integer.")

        def find_min_node(node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        def delete_node(root, emp_id):
            if root is None:
                return root
            if emp_id < root.emp_id:
                root.left = delete_node(root.left, emp_id)
            elif emp_id > root.emp_id:
                root.right = delete_node(root.right, emp_id)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    min_node = find_min_node(root.right)
                    root.emp_id = min_node.emp_id
                    root.name = min_node.name
                    root.right = delete_node(root.right, min_node.emp_id)
            return root

        self.root = delete_node(self.root, emp_id)

    def print_chart(self):
        def inorder_traversal(node):
            if node is not None:
                inorder_traversal(node.left)
                print(f"Employee ID: {node.emp_id}, Name: {node.name}")
                inorder_traversal(node.right)

        print("Organization Chart:")
        inorder_traversal(self.root)


# Sample usage
org_chart = OrganizationChart()

try:
    org_chart.insert_employee(15, "Ruto")
    org_chart.insert_employee(30, "RiggyG")
    org_chart.insert_employee(10, "Sonko")
    org_chart.insert_employee(33, "Zakayo")
    org_chart.insert_employee(20, "Daudi")
   

    org_chart.print_chart()

    org_chart.delete_employee(10)

    print("\nOrganization Chart after deletion:")
    org_chart.print_chart()

    print("\nSearching for employee with ID 33:")
    print(org_chart.search_employee(33))

except ValueError as e:
    print(f"Error: {e}")
