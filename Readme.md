# Description

This is a simple python 3 script to look at ways to instrospect Directed Acyclic Graphs (DAG)
using the NetworkX python library.

This script, dagfoo.py, creates a Directed Graph and then uses a NetworkX API call to get all
available paths in the graph.  The paths are sorted in descending order and the longest path value
printed to stdout.

# Setup

```pip install networkx```

Optionally...

```pip install matploitlib```

# Running 

```python3 dagfoo.py```

## Displaying The Graph

Optionally, you can install the matploitlib package for viewing the DAG if you'd like.  Simply comment-in the necessary code in the script.

Here's what the graph should look like.

![alt text](https://github.com/jcaple/dagtest/blob/main/graph-screenshot.png?raw=true)
