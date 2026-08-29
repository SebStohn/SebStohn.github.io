## Portfolio Links

[Home](./index.html) |
[Contact.io](./softwaredesignengineering.html) |
[Coursearch](./algorithmsdatastructures.html) |
[National Park Explorer](./databases.html)

# Coursearch

<img src="./assets/images/2.1.png" style="width: 600px;" alt="Figure 1">

Coursearch was originally developed in C++ but has been translated to Python. The application parses a CSV file containing academic course information and organizes it into a binary search tree (BST), allowing users to efficiently search and navigate the data. The Python version also features the ability to search courses by subject, browse courses within a subject, and access a statistics feature.

# Technical Specifications

<img src="./assets/images/2.2.png" style="width: 600px;" alt="Figure 2">

Coursearch features a CSV parser (pictured above) that creates a 2D vector of academic courses with prerequisites that can be searched efficiently using a binary search tree with various algorithms. The Course structure is a Python @dataclass The BST, node structure, insert, search, traverse, CSV parse, course load, and main menu logic were all rewritten to be as efficient as possible.

Features were added such as a Find-by-Subject option and Subject sub-menu that allows users to view courses within a selected subject using the new search_subject and print_subject BST methods. A Statistics feature was also introduced through the gen_stats and counter methods which print information such as the total number of courses, subject frequency, and most common prerequisites.

![Figure 3](./assets/images/2.3.png)

<img align="right" src="./assets/images/2.4.png" style="margin-left: 10px; margin-right: 10px;" alt="Figure 4">

# [Coursearch Repository](https://github.com/SebStohn/SebStohn.github.io/tree/main/2.%20CSV%20Parser%20BST)
