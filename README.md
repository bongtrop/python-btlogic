================
python-logicterm
================

Python library for management logic minterm and maxterm.

Written by Pongsakorn Sommalai <bongtrop@gmail.com>.

All code is under a BSD-style license, see LICENSE for details.

Source: https://github.com/bongtrop/python-btlogic


Requirements
============

python >= 2.7

Installation
============
To install run

    ``python setup.py install``

which will install the library into python's site-packages directory.


Usage
=====

Import ``logicterm`` from ``btlogic``:
    
    >>> from btlogic import logicterm
    
And set your API key:

    >>> object = logicterm(<YOURTERM>, <"minterm"|"maxterm">, <BIT>)

**This have only logicterm

---------------
constructer methods
---------------

The methods ``logicterm(<YOURTERM>, <"minterm"|"maxterm">, <BIT>)``

Example of create object from logicterm:

    >>> object = logicterm(<YOURTERM>, <"minterm"|"maxterm">, <BIT>)

--------------------
setTerm methods
--------------------

``setTerm(<YOURTERM>, <"minterm"|"maxterm">, <BIT>)`` 
set term, type and bit.

Example of setting term:

    >>> object.setTerm([0,1], "minterm", 4)

------------------
getMinterm methods
------------------

``getMinterm()`` returns list of minterm

Example of getting list of minterm:

    >>> a = object.getMinterm()
	>>> print a
	[0,1]

------------------
getMinterm methods
------------------

``getMinterm()`` returns list of maxterm

Example of getting list of maxterm:

    >>> a = object.getMaxterm()
	>>> print a
	[2,3]	

-----------------
getMintermByString methods
-----------------

``getMintermByString()`` returns string of minterm by [a-z].

Example of getting string of minterm by [a-z]:

    >>> a = object.getMintermByString()
	>>> print a
	a'b'+a'b

-----------------
getMaxtermByString methods
-----------------

``getMaxtermByString()`` returns a string of maxterm by [a-z].

Example of getting string of minterm by [a-z]:

    >>> a = object.getMaxtermByString()
	>>> print a
	(a'+b)(a'+b')


----------------
opposite methods
----------------

``opposite()`` not of function input !F

Example of getting details on NC 2008 Gubernatorial election:

    >>> object.opposite()
	>>> object.getMinterm()
	[2,3]

