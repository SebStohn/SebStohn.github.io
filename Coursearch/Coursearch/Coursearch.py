"""
Module Name: Coursearch.py
Description: This program contains a custom CSV Parser that parses academic
courses into a Binary Search Tree structure that contains a print function,
multiple search functions, and a statistics generator function.
Author: Sebastian Stohn
Date: 2026-08-03
CSV Paths Included: i1.csv, i2.csv
"""

# Parser is expected to reject:
# CS450 from CS403
# BIO450 from BIO402
# MAT450 from MAT402

from dataclasses import dataclass, field
from collections import Counter
import csv


# Dictionary of subjects
subjects = {
    "CS": "Computer Science", "IT": "Information Technology",
    "SE": "Software Engineering", "CE": "Computer Engineering",
    "EE": "Electrical Engineering", "ME": "Mechanical Engineering",
    "AE": "Aerospace Engineering", "CH": "Chemistry",
    "BIO": "Biology", "MAT": "Mathematics",
    "PHY": "Physics", "STA": "Statistics",
    "ECO": "Economics", "ACC": "Accounting",
    "FIN": "Finance", "MKT": "Marketing",
    "MGT": "Management", "ENG": "English",
    "HIS": "History", "PSY": "Psychology",
    "SOC": "Sociology", "ART": "Art",
    "MUS": "Music", "NUR": "Nursing",
    "BUS": "Business"
}


@dataclass
class Course:
    """Course object structure"""
    num: str = ""
    name: str = ""
    pre: list = field(default_factory=list)


class Node:
    """Node object structure"""
    def __init__(self, course):
        """Initialize node with a course and left & right child nodes"""
        self.course = course
        self.left = None
        self.right = None


class BinarySearchTree:
    """Data structure object"""
    def __init__(self):
        """Initialize tree with empty root node"""
        self.root = None

    def insert_course(self, course):
        """Insert course at root or call add_course"""
        if self.root is None:
            self.root = Node(course)
        else:
            self.add_course(self.root, course)

    def add_course(self, node, course):
        """Recursively traverse tree and insert course"""
        if course.num < node.course.num:
            if node.left is None:
                # Add course to left child if empty
                node.left = Node(course)
            else:
                # Recursive call on left child
                self.add_course(node.left, course)
        else:
            if node.right is None:
                # Add course to right child if empty
                node.right = Node(course)
            else:
                # Recursive call on left child
                self.add_course(node.right, course)

    def search_course(self, course_number):
        """Search tree for match using course_number"""
        current = self.root

        # Traverse tree until match is found
        while current is not None:
            if course_number == current.course.num:
                # Return matching course
                return current.course
            elif course_number < current.course.num:
                # Move to left child
                current = current.left
            else:
                # Move to right child
                current = current.right

        # Return empty course if not found
        return Course()

    def print_courses(self):
        """Print header and call print_bst"""
        print("\n| COURSE", " " * 40, "| PREREQUISITES")
        self.print_bst(self.root)

    def print_bst(self, node):
        """Recurse to start of tree and print all courses"""
        if node is not None:
            # Recursive call on left child
            self.print_bst(node.left)

            # Print course aligned with header
            spaces = " " * (44 - len(node.course.num) - len(node.course.name))
            print(f"| {node.course.num} - {node.course.name}{spaces} |", end="")

            # Print prerequisites or "None"
            if node.course.pre:
                for pre in node.course.pre:
                    print(f" {pre.num}", end="")
                print()
            else:
                print(" None")

            # Recursive call on right child
            self.print_bst(node.right)

    def search_subject(self, subj_abv):
        """Print subj_abv and call print_subject"""
        print(f"\n   {subj_abv} Courses:")
        self.print_subject(self.root, subj_abv)

    def print_subject(self, node, subj_abv):
        """Traverse tree for match using subj_abv"""
        if node is None:
            return

        # Recursive call on left child
        self.print_subject(node.left, subj_abv)

        # Print course if subject matches
        if node.course.num.startswith(subj_abv):
            print(f"   {node.course.num} - {node.course.name}")

        # Recursive call on right child
        self.print_subject(node.right, subj_abv)

    def gen_stats(self):
        """Generate statistics from tree courses"""
        courses = [] # Empty list to store all courses
        prerequisites = [] # Empty list to store all prerequisites

        # Call custom counter method with both lists
        self.counter(self.root, courses, prerequisites)

        # Count items in prerequisites list
        pre_nums = Counter(prerequisites)

        print(f"\nTOTAL COURSES: {len(courses)}")
        print("\nSUBJECT FREQUENCY")

        # For each key-value pair in subjects dict
        for abv, subj in subjects.items():
            # If any course in courses contains a matching subject abbreviation
            if any(abv in item for item in courses):
                spaces = " " * (25 - len(subj))
                # Print subject name
                print(f"{subj}{spaces}", end="")

                # Print "*" for each course in current subject
                for course in courses:
                    if course.startswith(abv):
                        print("*", end="")
                print()

        print("\nCOMMON PREREQUISITES")

        # For each key-value pair in Counter result
        for num, total in pre_nums.items():
            # If more than one occurrence print course number and total
            if total > 1:
                print(f"{num}: {total}")

    def counter(self, node, courses, prerequisites):
        """Traverse tree to create lists of courses and prerequisites"""
        if node is None:
            return

        # Recursive call on left child
        self.counter(node.left, courses, prerequisites)

        # Add course number to course list
        courses.append(node.course.num)
        # Add each prerequisite number to prerequisite list
        for pre in node.course.pre:
            prerequisites.append(pre.num)

        # Recursive call on right child
        self.counter(node.right, courses, prerequisites)


def csv_parser(file_path):
    """Open a CSV file and create a 2D list of it's contents"""
    file = [] # Empty 2D list

    # Attempt to open file
    try:
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)

            # If row contains number and name add to file
            for row in reader:
                if len(row) >= 2:
                    file.append(row)
    except FileNotFoundError:
        print("Error opening file...", end="")
        return[]

    # Collect course numbers from every row
    course_nums = {row[0] for row in file}

    # Check each row for prerequisites
    for row in file:
        if len(row) > 2:
            # Accept course number and name as good
            good_fields = row[:2]

            # Check if prerequisite exists in course number collection
            for pre in row[2:]:
                # If exists, accept prerequisite as good, otherwise reject
                if pre in course_nums:
                    good_fields.append(pre)

            # Update row
            row[:] = good_fields

    return file


def load_courses(csv_path, bst):
    """Create course objects from 2D list"""
    print("\nLoading CSV file...", end="")

    csv_file = csv_parser(csv_path)

    # Populate courses with corresponding fields
    for row in csv_file:
        course = Course()
        course.num = row[0]
        course.name = row[1]

        # Populate prerequisites as course objects
        for pre in row[2:]:
            course.pre.append(Course(num = pre))

        # Insert completed courses
        bst.insert_course(course)

    print("Done!")


def main():
    """Create bst and control menu flow"""
    bst = BinarySearchTree() # Official binary search tree object

    while True: # Infinite main menu loop
        print("\nMain Menu")
        print("1. Load Courses")
        print("2. Display All Courses")
        print("3. Find A Course")
        print("4. Find A Subject")
        print("5. Course Statistics")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1": # Load courses
            csv_path = input("Enter CSV filepath: ")
            load_courses(csv_path, bst)
        elif choice == "2": # Display all courses
            bst.print_courses()
        elif choice == "3": # Find a course
            course_num = input("Enter course number: ").upper()
            course = bst.search_course(course_num)

            # If course exists print header, course info, and prerequisites
            if course.num:
                spaces = " " * (44 - len(course.num) - len(course.name))
                print("\n| COURSE", " " * 40, "| PREREQUISITES")
                print(f"| {course.num} - {course.name}{spaces} |", end="")

                if course.pre:
                    for pre in course.pre:
                        print(f" {pre.num}", end="")
                    print()
                else:
                    print(" None")
            else:
                print("\nCourse not found")
        elif choice == "4": # Find a subject
            while True: # Infinite indented menu loop
                print("\n   Subject Menu")
                print("   1. Search Subject By Abbreviation")
                print("   2. Show Abbreviations")
                print("   3. Back")
                choice2 = input("   Enter choice: ")

                if choice2 == "1": # Search subject by abbreviation
                    subj_abv = input("   Enter subject abbreviation: ").upper()
                    bst.search_subject(subj_abv)
                elif choice2 == "2": # Show abbreviations
                    print()

                    # Print entire subjects dict
                    for abv, subj in subjects.items():
                        print(f"   {abv}: {subj}")
                elif choice2 == "3": # Break infinite loop
                    break
                else:
                    print("\n   Invalid menu selection")
        elif choice == "5": # Course statistics
            bst.gen_stats()
        elif choice == "6": # Break infinite loop
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid menu selection")


# Run main
if __name__ == "__main__":
    main()