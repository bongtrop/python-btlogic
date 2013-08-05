#!/usr/bin/python
from btlogic import term

a = term(term=[0,1], type="minterm", bit=2)
print a.getMaxterm()