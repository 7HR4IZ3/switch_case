# switch_case
Switch case implementation in python

# Usage
```python
def get():
    ...

def put(id):
    ...

def post():
    ...

# Pass positional args as tuple in the third parameter
# And dictionary as kwargs in the fourth parameter
switch(request.method).case("post", post).case("put", put, (request.PUT.id,)).default(get)
``
Or

```pythonw

s = switch(request.method)
s.case("post", post)
s.case("put", put, (request.PUT.id,))
s.default(get)
```
Note: The default function is compulsory

# Args, Kwargs and Return
Pass global args and kwargs in the switch instance declaration
```python
def get(request):
    ...

def put(request, id):
    ...

def post(request):
    ...

switch(request.method, args=(request,)).case("post", post).case("put", put, (request.PUT.id,)).default(get)
```
Use _return to return the value of the case function
```python
def get(request):
    return request.GET.id

def post(request):
    return request.POST.id

id = switch(request.method, args=(request,)).case("post", post).default(get)
do_stuff(id)
```
