## Agora.co programming test

### Design

#### 1. Set
`Usage: set key value`
  * key is a string with no spaces
  * value can be a regular string or a json string. If a json string, it will be stored as a nested structure for the corresponding key
  * if value is not entered, an error message is displayed

##### Example:
```
set key1 a value
set key2 {"nestedKey1": "nested value", "nestedKey2": {"nestederKey": "Double-nested value"}}
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
  * if the key does not exists in the key value store, an error message is displayed

##### Example:
```
set key1 a value
set key2 {"nestedKey1": "nested value", "nestedKey2": {"nestederKey": "Double-nested value"}}
delete key2
```
will result in the following value of the key value store

```
{
  "key1": "a value"
}
```

### Other notes:
1. 'common' != 'Common'
2. 'common,' != 'common'
3. what to do about equal cases? who wins?
4. additional white spaces around the value will be removed by strip()
5. The entire multi format
6. Does not print most common word when dict is empty

#### Todo:
1. O() analysis
2. Enumerate all test cases and pytest them
3. document + readme
5. Define what a token is