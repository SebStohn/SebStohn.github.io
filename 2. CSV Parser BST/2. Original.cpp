#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

////SEBASTIAN STOHN////

using namespace std;


/**
 * Course structure
 */
struct Course {
    string num;
    string name;
    vector<Course> prereqs;
};


/**
 * Tree node structure
 */
struct Node {
    Course course;
    Node* left;
    Node* right;

    // default constructor
    Node() {
        left = nullptr;
        right = nullptr;
    }
    // constructor with course
    Node(Course aCourse) :
        Node() {
        course = aCourse;
    }
};


/**
 * Binary search tree class with members and methods to implement the BST
 */
class BinarySearchTree {
private:
    Node* root;
    void printBST(Node* node);
    void addCourse(Node* node, Course course);

public:
    BinarySearchTree();
    virtual ~BinarySearchTree();
    void printCourses();
    void insertCourse(Course course);
    Course searchCourse(string courseNumber);
};


/**
 * Default constructor
 */
BinarySearchTree::BinarySearchTree() {
    root = nullptr;
}


/**
 * Destructor
 */
BinarySearchTree::~BinarySearchTree() {
    // build destructor
    struct Destructor {

        // build delete function
        static void Delete(Node* node) {

            // if node is not null then post-order delete tree
            if (node != nullptr) {
                Delete(node->left);
                Delete(node->right);
                delete node;
            }
        }
    };
    // recurse from root deleting every node
    Destructor::Delete(root);
}


/**
 * Calls print function with root
 */
void BinarySearchTree::printCourses() {
    this->printBST(root);
}


/**
 * Traverse and print tree in order
 * 
 * @param current node pointer
 */
void BinarySearchTree::printBST(Node* node) {
    if (node != nullptr) {

        // recursive call on left child
        printBST(node->left);

        // print course
        cout << node->course.num << ", " << node->course.name;

        // print prerequisites at set distance
        if (node->course.prereqs.size() > 0) {
            int spaces = 45 - node->course.num.length() - node->course.name.length();
            if (spaces >= 0) {
                cout << string(spaces, '.');
            }
            cout << "Prerequisites|";

            for (int i = 0; i < node->course.prereqs.size(); ++i) {
                cout << node->course.prereqs.at(i).num << "|";
            }
        }
        cout << endl;

        // recursive call on right child
        printBST(node->right);
    }
}


/**
 * Inserts new course as root or calls addCourse
 * 
 * @param course to insert
 */
void BinarySearchTree::insertCourse(Course course) {
    // if root is empty set root to new course
    if (root == nullptr) {
        root = new Node(course);
    }
    // otherwise send new course to addCourse
    else {
        this->addCourse(root, course);
    }
}


/**
 * Add a course to a node
 *
 * @param current node pointer
 * @param course to insert
 */
void BinarySearchTree::addCourse(Node* node, Course course) {
    // if course is less than node make course left child of node
    if (course.num < node->course.num) {
        if (node->left == nullptr) {
            node->left = new Node(course);
        }
        // if left child already exists recurse left
        else {
            addCourse(node->left, course);
        }
    }
    // otherwise make course right child of node
    else {
        if (node->right == nullptr) {
            node->right = new Node(course);
        }
        // if right child already exists recurse right
        else {
            addCourse(node->right, course);
        }
    }
}


/**
 * Searches for and displays a course
 * 
 * @param courseNumber
 * @return corresponding course if found
 */
Course BinarySearchTree::searchCourse(string courseNumber) {
    Node* curNode = root;

    // loop down tree until bottom reached or matching course found
    while (curNode != nullptr) {
        if (courseNumber == curNode->course.num) {
            return curNode->course;
        }
        // if course is smaller than curNode traverse left
        else if (courseNumber < curNode->course.num) {
            curNode = curNode->left;
        }
        // otherwise traverse left
        else {
            curNode = curNode->right;
        }
    }
    // if not found return empty course
    Course course;
    return course;
}


/**
 * Parses a CSV file into a 2D vector
 *
 * @param filePath the file to parse
 * @return a 2D vector with the parsed file
 */
vector<vector<string>> csvParser(string filePath) {
    vector<vector<string>> file;
    string line;

    // open input file and validate
    ifstream inputFile(filePath);
    if (!inputFile.is_open()) {
        cerr << "Error opening file." << endl;
        return file;
    }
    // read csv line into row
    while (getline(inputFile, line)) {
        stringstream ss(line);
        vector<string> row;
        string cell;
        while (getline(ss, cell, ',')) {
            row.push_back(cell);
        }
        // validate sufficient information
        if (row.size() < 2) {
            continue;
        }
        // add row to row vector
        file.push_back(row);
    }
    inputFile.close();

    // search prerequisites for corresponding course
    for (int i = 0; i < file.size(); ++i) {
        if (file.at(i).size() > 2) {
            for (int j = 2; j < file.at(i).size(); ++j) {
                bool prereqFound = false;
                for (int k = 0; k < file.size(); ++k) {
                    if (file.at(i).at(j) == file.at(k).at(0)) {
                        prereqFound = true;
                        break;
                    }
                }
                // delete hanging prerequisites
                if (!prereqFound) {
                    file.at(i).erase(file.at(i).begin() + j);
                    --j;
                }
            }
        }
    }
    return file;
}


/**
 * Loads a CSV file containing courses into a BST
 *
 * @param csvPath the path to the CSV file to load
 * @param bst to load courses into
 */
void loadCourses(string csvPath, BinarySearchTree* bst) {
    cout << "Loading CSV file " << csvPath << endl;

    // get parsed file from csvParser
    vector<vector<string>> csvFile = csvParser(csvPath);

    // create course with prerequisites from 2D vector
    for (int i = 0; i < csvFile.size(); ++i) {
        Course newCourse;
        newCourse.num = csvFile.at(i).at(0);
        newCourse.name = csvFile.at(i).at(1);
        for (int j = 2; j < csvFile.at(i).size(); ++j) {
            Course newPrereq;
            newPrereq.num = csvFile.at(i).at(j);
            newCourse.prereqs.push_back(newPrereq);
        }
        // send course to bst
        bst->insertCourse(newCourse);
    }
    cout << "Done." << endl;
}


/**
 * The one and only main method
 */
int main() {
    // create empty binary search tree
    BinarySearchTree* bst = new BinarySearchTree();
    Course course;
    string csvPath;
    string courseNum;

    int choice = 0;
    while (choice != 9) {
        cout << "Menu:" << endl;
        cout << "   1. Load Courses" << endl;
        cout << "   2. Display All Courses" << endl;
        cout << "   3. Find A Course" << endl;
        cout << "   9. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            //ABCU_Advising_Program_Input.csv
            cout << endl << "Enter CSV file path: ";
            cin >> csvPath;
            cin.clear();

            // send csv and empty tree to loadCourses
            loadCourses(csvPath, bst);
            cout << endl;
            break;

        case 2:
            cout << endl;
            // print bst already in order
            bst->printCourses();
            cout << endl;
            break;

        case 3:
            cout << endl << "Enter course number: ";
            cin >> courseNum;

            // convert to uppercase
            for (char& c : courseNum) {
                c = toupper(c);
            }

            // send course number to Search function
            course = bst->searchCourse(courseNum);

            // display search results
            if (!course.num.empty()) {
                cout << course.num << ", " << course.name;
                if (course.prereqs.size() > 0) {
                    int spaces = 45 - course.num.length() - course.name.length();
                    if (spaces >= 0) {
                        cout << string(spaces, '.');
                    }
                    cout << "Prerequisites|";

                    for (int i = 0; i < course.prereqs.size(); ++i) {
                        cout << course.prereqs.at(i).num << "|";
                    }
                }
                cout << endl;
            }
            else {
                cout << "Course " << courseNum << " not found." << endl;
            }
            cout << endl;
            break;

        case 9:
            cout << endl;
            break;

        default:
            cout << endl << "Not a valid choice, try again." << endl << endl;
        }
    }
    cout << "Shutting down." << endl;
    return 0;
}