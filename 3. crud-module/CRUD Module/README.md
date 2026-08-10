# National Parks CRUD Dashboard

## Overview

The National Parks CRUD Dashboard is a Python web application that allows users to browse and manage information about U.S. National Parks stored in MongoDB. The dashboard provides interactive data visualization and supports updating park visit status.

## Features

- View all national parks
- Interactive data table
- Sort park information
- Update visited status
- Interactive map visualization
- Pie chart showing park counts by state
- State selection using a dropdown menu
- MongoDB integration

## Technologies

- Python
- MongoDB
- Dash
- Plotly
- Pandas

## Running the Application

### Prerequisites

- Python 3.x
- MongoDB
- PyCharm (recommended)

### Setup

1. Open the project in PyCharm.
2. Configure the Python interpreter.
3. Install all required dependencies.

### Database Setup

Open the MongoDB shell:

```
mongosh
```

Create or switch to the database:

```
use national_parks
```

Run the commands contained in:

```
seed.md
```

to populate the database.

### Launch the Dashboard

Run:

```
Dashboard.py
```

Then open:

```
http://127.0.0.1:8050/
```