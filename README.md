# Hierarchical Data Treemap Visualizer [September 2023]

Welcome to my personal project, **Hierarchical Data Treemap Visualizer**, which is a tool designed to showcase and explore hierarchical data structures using a treemap visualization. This project allowed me to dive into some fundamental concepts of computer science, including tree data structures, recursion, and interactive visualizations. It was an exciting journey through data modeling and efficient rendering using Python and the `pygame` library.

## Project Overview

The main goal of this project is to create an interactive treemap visualizer that can display hierarchical data efficiently. The visualizer works with two different kinds of data:

1. **File System Visualization**: Visualizes the structure and size of files and folders on your computer.
2. **CS1 Paper Categorization**: Visualizes research paper data categorized into hierarchical topics related to computer science education.

This project incorporates key concepts like tree-based data modeling, recursive algorithms, and inheritance to handle different types of hierarchical data.

## Learning Goals

By working on this project, I've gained the ability to:
- Model real-world hierarchical data using trees.
- Implement both mutating and non-mutating recursive operations on tree data structures.
- Develop and refine an algorithm to generate geometric treemap visualizations.
- Use the `os` library to interact with and model my computer's file system.
- Apply inheritance to design classes that follow a common interface, making the codebase easily extensible.

## How It Works

The project is structured into several key components:

### 1. **Data Modeler**
The core part of the project is a tree-based data model. I created an abstract base class `TMTree` and implemented specific subclasses:
- **FileSystemTree**: Represents a computer's file system, where each internal node is a folder and each leaf is a file. The `data_size` attribute reflects the size of files in bytes.
- **PaperTree**: Represents a hierarchy of computer science education research papers, categorized into various subtopics. Optionally, it organizes papers by publication year before categorizing by topic.

### 2. **Treemap Algorithm**
The treemap algorithm generates a visual representation of hierarchical data:
- **Rectangles**: Each subtree in the hierarchical data is represented as a rectangle, scaled to reflect its `data_size`. The algorithm uses recursive partitioning to divide a 2D space into proportional rectangles, adjusting dynamically as the user interacts with the data.
- **Rounding and Precision**: Ensures accurate but efficient division of space by rounding rectangle dimensions, while preserving the total area proportion.

### 3. **Interactive Visualizer**
Using `pygame`, I created an interactive window that:
- **Displays the Treemap**: Shows colorful rectangles representing different nodes in the hierarchy.
- **Handles User Events**: Users can select, expand, collapse, move, or resize nodes interactively.
- **Visual Feedback**: Updates the display in real-time based on user input, providing a seamless and responsive experience.

## How to Get Started

### Setup
1. **Download and Extract**: Clone or download the project repository and extract the starter code.
2. **Install Dependencies**: 
   - Make sure to install `pygame` if you haven't already:
     ```bash
     pip install pygame
     ```
3. **Run the Visualizer**:
   - For the **File System Treemap**: Open `treemap_visualiser.py` and run `run_treemap_filesystem()` with a path from your computer.
   - For the **CS1 Paper Treemap**: Open `treemap_visualiser.py` and run `run_treemap_papers()`.

### Testing and Debugging
- Use the provided `a2_sample_test.py` to run tests and validate your implementation.
- Write additional doctests and pytests to cover edge cases and ensure robustness.

## Key Features

1. **Data Modeling with Trees**: 
   - Implements a recursive tree structure to represent hierarchical data.
   - Uses inheritance for flexibility and code reuse.
  
2. **Treemap Visualization**:
   - Dynamically generates and displays rectangles based on `data_size`.
   - Efficiently handles large datasets by caching computed values and updating only when necessary.

3. **Interactive User Experience**:
   - Select nodes by clicking on rectangles.
   - Expand or collapse nodes using keyboard events.
   - Move nodes within the hierarchy and adjust their sizes interactively.
   - Visualize real-world datasets, like your computer's file system or categorized research papers.

## Challenges and Learnings

This project taught me the importance of:
- **Recursive Programming**: Developing an efficient treemap algorithm that handles hierarchical data in a scalable way.
- **User Interaction**: Implementing a responsive interface that reacts smoothly to user input.
- **Efficient Data Handling**: Optimizing operations on large datasets to maintain performance.

## Future Enhancements

- **Improve Data Handling**: Extend the functionality to support more hierarchical datasets with different attributes.
- **Refine User Interface**: Add features like zooming, panning, and detailed information panels.
- **Optimization**: Explore more efficient algorithms for better performance on extremely large datasets.

## Dependencies

- **Python**: Version 3.6 or higher
- **pygame**: For rendering the graphical display

## Running the Project

To run the project, open a terminal and execute:
```bash
python treemap_visualiser.py
```

Choose between the two provided datasets and watch as the hierarchical data comes to life through beautiful treemap visualizations!

---

I hope you find this project as fascinating as I did while working on it. Feel free to explore the code, modify the visualizations, or extend the project to support new types of hierarchical data. Enjoy exploring the world of hierarchical data with treemaps! 🌳✨
