# DATA STRUCTURES --- ( PYTHON 🐍)

Data structures is a way of storage data in the computer memory for then recovery it. There are different data structures and the one you use in your algorithm must be adapted to the type of program that you must solve, since depending on the structure you use will affect the efficiency of your program.


**For example:** 

if you have a program that manages a huge research catalog and you constantly have to search, update and add new research in different catalog indexes. no matter how efficient your algorithms are to perform these operations if you use the wrong data structure, the program will not be as efficient as it should be ( **BIG O NOTATION** ).


Next I will be explaining as precisely as possible some of the most used data structures.


### CONTENTS:

* [Arrays](#arrays)
* [Linked List](#linked-list)
* [Stacks](#stacks)
* [Queques](#queques)
* [Hash Table](#hash-table)



## ARRAYS

Arrays are the most common implementations of lists in many programming languages.


![arrays](./screenshots/arrays.png)


Depending on the programming language, the arrays have different characteristics such as: you have to define the size they will have, you cannot store different values in the same array, etc.

As I mentioned earlier, these characteristics do not apply to all languages, what we must take into account are the following things:

* The arrays are ordered.
* All the values stored in the array have an index with which we can access their value, this starts from 0.
* It is easy to add elements at the end, the thing is complicated when you must add elements in specific places of the matrix since to do this the other elements that are in front must be pushed, in general this process is usually an O (n).


BIG O NOTATION

**SEARCH** --> O(n)

**ACCESS** --> O(1)

**DELETE** --> O(n)

**INSERT** --> O(n)


**FOR MORE SEE THE FILE arrays.py IN SRC**



## LINKED LIST

Linked lists, unlike arrays, do not handle indexes so you cannot access them in a common way, like this: list [0].

By convention, generally the elements within the linkedlist are called nodes. These nodes contain a value and the reference to the next element.


![Linked List](https://i1.faceprep.in/Companies-1/types-of-linked-list.png)



BIG O NOTATION

**SEARCH** --> O(n)

**ACCESS** --> O(n)

**DELETE** --> O(1)

**INSERT** --> O(1)


**FOR MORE SEE THE FILE linked_list.py IN SRC**



## STACKS

It is another data structure based on a collection of lists, it is associated with the LIFO structure, that is, the last to enter is the first to leave.

We can see it this way, let's imagine that we have a stack of plates, we are placing them one on top of the other and to remove a certain plate from the stack we must first remove the plates that are on top of the plate that we want to extract.


![Stacks](https://res.cloudinary.com/practicaldev/image/fetch/s--s1Qbl8Gf--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/mwcwre09s12vqa3gvl7a.png)



BIG O NOTATION

**SEARCH** --> O(n)

**ACCESS** --> O(n)

**DELETE** --> O(1)

**INSERT** --> O(1)


**FOR MORE SEE THE FILE stack.py IN SRC**



## QUEQUES

It is associated with the FIFO structure, that is, the first to enter is the first to leave.

Imagine that there is a line at the supermarket to obtain a certain product, the people who arrive first are the first to obtain said product and those who arrive later go back to wait their turn.


![Queques](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png)

We must also take into account the priority queques where each "person" is assigned a priority, such as the priority given to people with disabilities or pregnant women, if there are no people who meet these characteristics in the queque. , the first to leave will be the first to be served.

BIG O NOTATION

**SEARCH** --> O(n)

**ACCESS** --> O(n)

**DELETE** --> O(1)

**INSERT** --> O(1)


**FOR MORE SEE THE FILE queque.py IN SRC**



## HASH TABLE


![Hash Table](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/1920px-Hash_table_3_1_1_0_1_0_0_SP.svg.png)


The hash table stores the information associating a key to a certain value, said key can be calculated in different ways, either with the ASCII code or another mathematical function.

Despite being one of the data structures with the fastest access to its elements, it takes up much more space than most. That is why we must evaluate well whether or not to implement a hash table. Also keep in mind that the keys cannot be repeated (collisions) since the hash table is based on sets to store the values, if for some reason there is a collision the new value will replace the previous one.


BIG O NOTATION

**SEARCH** --> O(1)

**ACCESS** --> O(1)

**DELETE** --> O(1)

**INSERT** --> O(1)


**FOR MORE SEE THE FILE maps.py and hash_table.py IN SRC**



## TREES


![Binary Tree](https://austingwalters.com/wp-content/uploads/2014/10/binary-tree-1.png)


Trees are a extension of linkend list, but with some differences. Trees start from a root node 
And said root node points to two child nodes (Left and right), if you remember the linkend list always pointed to the next element, because in trees there are generally two references in each node. 

Like other structures, trees also have their own rules that must always be taken into account:

* A parent node can have two children (Left and Right references) but a child node can only have one parent.
* You should always keep the tree as balanced as possible, this means that we should not add new elements in a single line.
* There should not be cycles within the binary tree, this goes hand in hand with the first point since there should not be two ways to reach the same element.


Tree terms:

* Root: First node Introduced into the tree, From here the child nodes start.
* Levels: Number of connections that it takes from the leaves to the root.
* Leaf: Nodes without childrens (external nodes).
* Edges: A group of connections taken together as a path.
* Height: The height of the node, is the numbers of edges between it and furthest leaf on the tree. The leaves has a height 0.
* Depth: The depth of the node, is the numbers o edges to the root.


Ways to search a node in the tree:


![Ways to search](https://image.slidesharecdn.com/rbolesbinarios-100524143730-phpapp02/95/rboles-binarios-28-728.jpg?cb=1274711920)



BIG O NOTATION

**SEARCH** --> O(n)

**ACCESS** --> O(n)

**DELETE** --> O(n)

**INSERT** --> O(log n)


**FOR MORE SEE THE FILE binary_tree.py and bst.py IN SRC**