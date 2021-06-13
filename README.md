# python-jsonparser

This package will help you to reduce your stress :) while parsing json in python.
Follow the steps below for using `python-jsonparser`

1) Install the package from pypi
```python
pip install python-jsonparser
```

2) Now let's assume we have a json object as below.
```python
dummy = {
    "name": {
        "first_name": "ABC",
        "last_name": "EFG"
    },
    "details": {
        "phone":["xxxxxxxxx", "00xxxxxxx", "0000000000"]
    }
}
```

3) Now assume we want `first_name`, `last_name` and only first `phone` number from the list.
For this create a class `TestClass` as below and inherit JSONParser from :
```python
from json_parser import JSONParser

class TestClass(JSONParser):
    first_name = 'name/first_name'
    last_name = 'name/last_name'
    phone = 'details/$1'

```

4) Create instance of your class and pass the json object.
```python
test_obj = TestClass(dummy)
```

5) Now call the validate method from the object created.

```python
output = test_obj.validate()
```

6) You will have following as the output:
```python
{
    'first_name': 'ABC',
    'last_name': 'EFG',
    'phone': '00xxxxxxx'
}
```

7) For getting the range of elements from the list you can use `$x:$y`
```python
from json_parser import JSONParser

class TestClass(JSONParser):
    first_name = 'name/first_name'
    last_name = 'name/last_name'
    phone = 'details/$1:$3' # This will give you 2 values from the list

# Output:
# {
#     'first_name': 'ABC',
#     'last_name': 'EFG',
#     'phone': ['00xxxxxxx', '0000000000']
# }

```

8) This was all about single object. What if you have json list of objects.
In that case set `many=True` while creating the instance of your class.
For example:
```python
test_obj = TestClass(dummy, many=True)
```