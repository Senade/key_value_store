## Agora.co programming test

### Design:

#### 1. Set
`Usage: set key value`
  * key is a string with no spaces
  * value is any string that follows `key` and a space
  * if value is not entered, an error message is displayed

##### Example:
```
set key1 a value
set key2/nestedKey2/nestederKey Double-nested value
set key2/nestedKey1 nested value
```
will be stored as 

```
{
  "key1": "a value",
  "key2": {
    "nestedKey1": "nested value",
    "nestedKey2": {
      "nestederKey": "Double-nested value"
    }
  }
}
```

#### 2. Delete
`Usage: delete key`
  * key is a string with no spaces
  * if the key does not exist in the data store, an error message is displayed

##### Example:
```
set key1 a value
set key2/nestedKey2/nestederKey Double-nested value
set key2/nestedKey1 nested value
delete key2/nestedKey2/nestederKey
```
will result in the following value of the key value store

```
{
  "key1": "a value",
  "key2": {
    "nestedKey1": "nested value",
    "nestedKey2":
  }
}
```

### Run instructions:
  * Requirements: [python 2.7](https://www.python.org/download/releases/2.7/)
  * Preferrably set up a [virtual environment](https://virtualenv.pypa.io/en/stable/)
  * Navigate to `kv_store`
  * Run `sh data_store.sh`

### Other notes:
1. The value string entered by the user is split by `' '` and the whitespace around the `value` is stripped
2. When the data store is empty, `No values in the dictionary` is displayed instead of the data store stucture and most common word
3. Python's `max()` function is used to find the most common word among the data store values. Since, `max` iterates through a dictionary, it isn't clear which word is returned in case of ties
4. A possible mistype of the type `set key1/ val1` is stored as `{'key1': 'val1'}`