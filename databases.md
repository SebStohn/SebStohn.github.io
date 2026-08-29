## Portfolio Links

[Home](./index.html) |
[Contact.io](./softwaredesignengineering.html) |
[Coursearch](./algorithmsdatastructures.html) |
[National Park Explorer](./databases.html)

# National Park Explorer

### [National Park Explorer Repository (download, explore, etc.)](https://github.com/SebStohn/SebStohn.github.io/tree/main/3.%20CRUD%20Module)

<img src="./assets/images/3.4.png" style="width: 650px;" alt="Figure 1">

National Park Explorer incorporates Python, Dash, and MongoDB. The dashboard is a Python application that displays U.S. National Park information including a sortable data table, state-based filtering, and an "Update Visited" feature that allows users to track which parks they've been to.

The application includes an interactive geolocation map and a pie chart that displays the distribution of National Parks by state along with a MongoDB database populated with data.

# Technical Specifications

National Park Explorer consists of a Python CRUD module, a Dash dashboard, and a MongoDB connection. It uses a data frame with a dropdown menu that dynamically filters parks by state. An “Update Visited” button was also added which toggles the "visited" field of the currently selected park using the CRUD Module’s “update” functionality.

<img src="./assets/images/3.2.png" style="width: 650px;" alt="Figure 2">

The pie graph (pictured above) displays the number of national parks by state while the geolocation map centers on the selected park. The data frame also supports table sorting and functional hyperlinks. The MongoDB database was also populated with records (pictured below) for all 63 U.S. national parks.

<img src="./assets/images/3.3.png" style="width: 650px;" alt="Figure 3">
