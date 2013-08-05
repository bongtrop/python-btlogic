==============
python-btlogic
==============

Python library for management logic minterm and maxterm or
can use Quine–McCluskey algorithm step 1.

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

Import ``term`` from ``btlogic`` and import ``quine`` from ``btlogic``:
    
    >>> from btlogic import term
	>>> from btlogic import quine
    
And create object:

    >>> objectTerm = term(term=<LIST YOURTERM>, type=<"minterm"|"maxterm">, bit=<BIT>)
	>>> objectQuine = quine(objterm=<OBJECT TERM>)
	>>> objectQuine = quine(minterm=<LIST MINTERM>, bit=<BIT>)


term class
==========

-------------------
constructer methods
-------------------

The methods ``term(term=<LIST YOURTERM>, type=<"minterm"|"maxterm">, bit=<BIT>)``,

Example of create object from term:

    >>> objectTerm = term(term=[0,1], type="minterm" bit=2)

--------------------
setTerm methods
--------------------

``setTerm(term=<LIST YOURTERM>, type=<"minterm"|"maxterm">, bit=<BIT>)`` 
set term, type and bit.

Example of setting term:

    >>> object.setTerm(term=[0,1], type="minterm", bit=2)

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
getMintermByAlphabet methods
-----------------

``getMintermByString()`` returns string of minterm by [a-z].

Example of getting string of minterm by [a-z]:

    >>> a = object.getMintermByString()
	>>> print a
	a'b'+a'b

-----------------
getMaxtermByAlphabet methods
-----------------

``getMaxtermByAlphabet()`` returns a string of maxterm by [a-z].

Example of getting string of minterm by [a-z]:

    >>> a = object.getMaxtermByAlphabet()
	>>> print a
	(a'+b)(a'+b')
	
-----------------
getMintermByBinary methods
-----------------

``getMintermByBinary()`` returns string of minterm by Binary.

Example of getting string of minterm by Binary:

    >>> a = object.getMintermByBinary()
	>>> print a
	['00', '01']

-----------------
getMaxtermByBinary methods
-----------------

``getMaxtermByBinary()`` returns a string of maxterm by Binary.

Example of getting string of minterm by Binary:

    >>> a = object.getMaxtermByBinary()
	>>> print a
	['10', '11']


	
----------------
opposite methods
----------------

``opposite()`` not of function input !F

Example of getting details on NC 2008 Gubernatorial election:

    >>> object.opposite()
	>>> object.getMinterm()
	[2,3]

quine class
===========

-------------------
constructer methods
-------------------

The methods ``quine(objterm=<OBJECT TERM>)``

Example of create object from quine:

	>>> objectQuine = quine(objterm=objTerm)
	>>> objectQuine = quine(minterm=[0,1], bit=2)

--------------------
setTerm methods
--------------------

The methods ``setTerm(objterm=<OBJECT TERM>)``

Example of create object from quine:

	>>> objectQuine = quine(objterm=objTerm)
	>>> objectQuine = quine(minterm=[0,1], bit=2)
	
--------------------
start methods
--------------------

The methods ``start()`` use for start use algorithm
it return list of term

Example of create object from quine:

	>>> listTerm = objectQuine.start()
	>>> print listTerm
	['0-']
	
--------------------------
getTermByAlphabet methods
--------------------------

The methods ``getTermByAlphabet(<listTerm>)`` use for start use algorithm
it return list of term

Example of create object from quine:

	>>> print objectQuine.getTermByAlphabet(listTerm)
	a'