# switch_case
Switch case implementation in python

# Usage
```python
x = 7

def say():print('hii')
def do(action):return action()

switch(x).case(7, say).case("do", do, (say,)).default(lambda:print('invalid'))
```
Or

```python
s = switch(x)
s.case(7, say)
s.case("do", do, (say,))
s.default(lambda:print('invalid'))
```
Note: The default function is compulsory
