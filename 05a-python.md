# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are both data structures that allow us to store ordered/indexed collections of values. However, once a tuple is created, they are immutable (cannot be sorted, appended, trimmed, etc.), while lists are mutable after it is created. Storing things in tuples allows Python to more efficiently process the data structure, if one does not wish to ever modify the data structure. We can mimic a dictionary with a list of immutable 2-entry-tuples (key-value pairs).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists and sets are both collections of data. However, sets are not indexed/ordered, while lists are. This allows Python to retrieve data from sets faster than parsing through indexed lists. Thus, finding an element in a set should thus be a lot faster.  
Example:  
Store numbers as an ordered list: `listX = [4, 8, 15, 16, 23 42]`  
Store numbers as an unorderd set: `setX = {4, 8, 15, 16, 23 42}`  
Since sets are unordered, it's much more efficent to perform set operations such as finding unions and intersection. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is an expression used to create an anonymous function in Python. This is useful when one wants to concisely apply a function to an iterable. For example, if we want to sort a list of words `listX = ['Apple', 'Banana', 'orange', 'GRAPEFRUIT]`, but we want to sort it by their first 3 letters (case-insensitive), we can do it with the line `sorted(listX, key = lambda x: lower(x[0:2]))`. Here, we essentially created an anonymous functiont that takes string `x`, and extracts the first 3 letters transformed into lower-case, and then mapped this function to each of the string in the list `listX` as the criterion for sorting the entries.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





