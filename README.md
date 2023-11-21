# binStructureDisplayer
A simple tool to help you to display your binary file with structure

## Usage
```
$ python binaryStructure.py
Enter bin file path: <your bin file path>
Enter structure file path: <your binary file structure path>
```

## Structure file example and format
The structure file is designed with json format, so please write your structure with json format

ex.
```json
{
  "First Element": {
    "node1": 1,
    "node2": 5
  },
  "Second Element": [
    {
      "node in array1": 2,
      "node in array2": 3
    }
  ],
  "Third Element": 7
}
```

## Output Example
Use binary file below as an example
```
11 22 33 44 55 66 77 88 99 00 21 22 23 24 25 26
31 32 ...
```

### Output
```
offset | ndoe                                              | value
     0 | First Element.node1                               | 11
     1 | First Element.node2                               | 22 33 44 55 66
     6 | Second Element.0.node in array1                   | 77 88
     8 | Second Element.0.node in array2                   | 99 00 21
    11 | Third Element                                     | 22 23 24 25 26 31 32
--------------------------------------------------
Total Bytes - 18
```
