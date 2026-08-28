To see the different kinds of ﬁelds you can use in a model, see the Django
Model
Field
Reference
at
https://docs.djangoproject.com/en/2.2/ref/models/ﬁelds/. You won’t
need all the information right now, but it will be extremely useful when
you’re developing your own apps.



# How toos

Short Entries: The __str__() method in the Entry model currently appends an
ellipsis to every instance of Entry when Django shows it in the admin site or the shell.
Add an if statement to the __str__() method that adds an ellipsis only if the entry is
longer than 50 characters. Use the admin site to add an entry that’s fewer than 50
characters in length, and check that it doesn’t have an ellipsis when viewed.


Was able to solve it but issues 
>ypeError at /admin/mypett/entry/
'>' not supported between instances of 'str' and 'int'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/admin/mypett/entry/
Django Version:	5.2.16
Exception Type:	TypeError
Exception Value:	
'>' not supported between instances of 'str' and 'int'
Exception Location:	/home/shoyo/Development/python-development/active-python-development/startup/mypett/models.py, line 29, in __str__
Raised during:	django.contrib.admin.options.changelist_view
Python Executable:	/home/shoyo/Development/python-development/active-python-development/startup/.venv/bin/python3
Python Version:	3.11.14
Python Path:	
['/home/shoyo/Development/python-development/active-python-development/startup',
 '/home/shoyo/.local/share/uv/python/cpython-3.11.14-linux-x86_64-gnu/lib/python311.zip',
 '/home/shoyo/.local/share/uv/python/cpython-3.11.14-linux-x86_64-gnu/lib/python3.11',
 '/home/shoyo/.local/share/uv/python/cpython-3.11.14-linux-x86_64-gnu/lib/python3.11/lib-dynload',
 '/home/shoyo/Development/python-development/active-python-development/startup/.venv/lib/python3.11/site-packages']
Server time:	Fri, 28 Aug 2026 01:30:23 +0000
